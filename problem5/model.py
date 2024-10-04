class Item:
    def __init__(self, id, name, price, description, image_path):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.image_path = image_path

    def __str__(self):
        return self.name


class Groceries(Item):
    def __init__(self, id, name, price, description, image_path, expiry_date):
        super().__init__(id, name, price, description, image_path)
        expiry_date = expiry_date

    
class Electronics(Item):
    def __init__(self, id, name, price, description, image_path, warranty):
        super().__init__(id, name, price, description,image_path)
        self.warranty = warranty

    
class Toys(Item):
    def __init__(self, id, name, price, description, image_path, age_group):
        super().__init__(id, name, price, description,image_path)
        self.age_group = age_group
        