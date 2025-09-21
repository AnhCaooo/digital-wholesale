from pydantic import BaseModel


class ProductColor(BaseModel):
    """Represents a product color with color ID and color value"""

    id: int
    value: str


class ProductPrice(BaseModel):
    """Represents types of product prices for a product. Currently is Wholesale and Retail price"""

    wholesale: float
    retail: float


class Product(BaseModel):
    """Represents details of a product"""

    id: int
    image_url: str
    name: str
    code: int
    ean: int
    color: ProductColor
    price: ProductPrice
    available_stock: int


# todo: add validation
# todo: add unit test
def cast_to_product(data: dict) -> Product:
    """Cast a dictionary from dict to Product object

    Args:
        data (dict): dictionary containing product details from xls file

    Returns:
        Product: details for product that system could use
    """
    color = ProductColor(id=int(data["Color ID"]), value=data["Color"])

    price = ProductPrice(
        wholesale=float(data["Wholesale price"]), retail=float(data["Retail price"])
    )

    product = Product(
        id=int(data["#"]),
        image_url=data["Product Image"],
        name=data["Product Name"],
        code=int(data["Product code"]),
        ean=int(data["EAN"]),
        color=color,
        price=price,
        available_stock=int(data["Available stock"]),
    )

    return product
