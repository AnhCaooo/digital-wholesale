import azure.functions as func
import logging
import json
from ...models import CLIENT_DB, Product, cast_to_product
import xlrd
import os

BASE_DIR = os.path.dirname(__file__)

# Mock stocks db.
STOCKS_RESOURCE = [
    {
        "client_code": "1609",  # Client A
        "source": os.path.join(BASE_DIR, "../../static", "ClientA.xls"),
    },
    {
        "client_code": "2309",  # Client B
        "source": os.path.join(BASE_DIR, "../../static", "ClientB.xls"),
    },
]


def get_stocks(req: func.HttpRequest) -> func.HttpResponse:
    """Retrieve stocks for specific client based on their code found in request header.

    **NOTE**: This is not a PROD level code. Therefore some areas will be simplified such as
    - Read data directly from excel files instead of real DB
    - No caching implementation (in-memory or distributed cache) and expired time of cache

    Args:
        req (func.HttpRequest): An HTTP request object.

    Returns:
        200: if client's stock found and returned successfully
        400: invalid request
        401: unauthorized request such as missing or invalid client code
        404: stock not found for that client
    """
    headers = req.headers
    if not headers:
        return func.HttpResponse(
            body=json.dumps({"message": "Invalid request"}), status_code=400
        )
    client_code = headers["Authorization"]
    if not client_code:
        return func.HttpResponse(
            body=json.dumps({"message": "Unauthorized request"}), status_code=401
        )
    if client_code:
        # Validate the client code if it valid and exists in mock db. If not valid, return 401
        if any(client.code == client_code for client in CLIENT_DB):
            for resource in STOCKS_RESOURCE:
                if resource["client_code"] == client_code:
                    source = resource["source"]
                    # Read data from excel file
                    stock = xlrd.open_workbook(source)
                    sheet = stock.sheet_by_index(0)
                    # Get all header_keys values by reading the first row
                    header_keys = [
                        sheet.cell(0, col_index).value
                        for col_index in range(sheet.ncols)
                    ]

                    stock_list: list[Product] = []
                    for row_index in range(1, sheet.nrows):
                        # 1. Loop through all columns in a row
                        # 2. Get key name from header column
                        # 3. Get value for specific row + column
                        d = {
                            header_keys[col_index]: sheet.cell(
                                row_index, col_index
                            ).value  # (2): (3)
                            for col_index in range(sheet.ncols)  # (1)
                        }
                        product = cast_to_product(data=d)
                        stock_list.append(product)

                    return func.HttpResponse(
                        body=json.dumps([p.model_dump() for p in stock_list]),
                        status_code=200,
                    )
            logging.warning(f"Stock resource for client code {client_code} not found")
            return func.HttpResponse(
                body=json.dumps({"message": "Stock resource not found"}),
                status_code=404,
            )
        else:
            logging.warning(
                f"Client code does not exist -> unauthorized: {client_code}"
            )
            return func.HttpResponse(
                body=json.dumps({"message": "Client does not exist"}), status_code=401
            )
    else:
        return func.HttpResponse(
            body=json.dumps({"message": "Invalid request"}), status_code=400
        )
