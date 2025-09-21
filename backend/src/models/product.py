
class ProductColor:
    """Represents a product color with color ID and color value
    """
    def __init__(self, id: int, value: str):
        self.id = id
        self.value = value
        
class ProductPrice: 
    """Represents types of product prices for a product. Currently is Wholesale and Retail price
    """
    def __init__(self, wholesale: float, retail: float):
        self.wholesale = wholesale
        self.retail = retail

class Product:
    """Represents details of a product
    """
    def __init__(self, image_url: str, name: str, code: int, ean: int, color: ProductColor, price: ProductPrice, available_stock: int):
        self.image_url = image_url
        self.name = name
        self.code = code
        self.ean = ean
        self.color = color
        self.price = price
        self.available_stock = available_stock


