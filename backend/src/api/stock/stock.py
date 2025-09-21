import azure.functions as func
import logging
import json
from ...models import CLIENT_DB
import xlrd
import os

BASE_DIR = os.path.dirname(__file__)

# Mock stocks db. 
STOCKS_RESOURCE = [
    {
        "client_code": "1609", # Client A
        "source": os.path.join(BASE_DIR, "../../static", "ClientA.xls"),
    },
    {
        "client_code": "2309", # Client B 
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
            body=json.dumps({"message": "Invalid request"}),
            status_code=400
        )
    client_code = headers["Authorization"]
    if not client_code:
        return func.HttpResponse(
                body=json.dumps({"message": "Unauthorized request"}),
                status_code=401
            )
    if client_code:
        # Validate the client code if it valid and exists in mock db. If not valid, return 401
        if any(client.code == client_code for client in CLIENT_DB):
            for resource in STOCKS_RESOURCE:
                if resource["client_code"] == client_code:
                    source = resource["source"]
                    # Read data from excel file 
                    logging.info(f"Reading stock data from {source}")
                    stock = xlrd.open_workbook(source)
                    logging.info("The number of worksheets is {0}".format(stock.nsheets))
                    logging.info("Worksheet name(s): {0}".format(stock.sheet_names()))
                    return func.HttpResponse(
                        body=json.dumps({
                            "access_token": client_code,
                            "message": "ok"
                        }),
                        status_code=200
                    )                
            logging.warning(f"Stock resource for client code {client_code} not found")
            return func.HttpResponse(
                body=json.dumps({"message": "Stock resource not found"}),
                status_code=404
            )
        else:
            logging.warning(f"Client code does not exist -> unauthorized: {client_code}")
            return func.HttpResponse(
                body=json.dumps({"message": "Client does not exist"}),
                status_code=401
            )
    else:
        return func.HttpResponse(
            body=json.dumps({"message": "Invalid request"}),
            status_code=400
        )
