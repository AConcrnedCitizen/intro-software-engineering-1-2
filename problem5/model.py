class Item:
    def __init__(self, id, name, price, description, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nPrice: {self.price}\nDescription: {self.description}\nQuantity: {self.quantity}\n"
    
    

