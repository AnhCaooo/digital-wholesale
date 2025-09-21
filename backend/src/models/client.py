class Client:
    """Client model represents client information"""

    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code


# Mock clients code db. Use set to not allow duplicated client codes
CLIENT_DB = {Client("A", "1609"), Client("B", "2309")}
