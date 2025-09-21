from .product import Product


class Stock:
    """Represents stock information for specific client and the status of products nailed for them"""

    def __init__(self, client_code: str, products: set[Product]):
        self.client_code = client_code
        self.products = products
