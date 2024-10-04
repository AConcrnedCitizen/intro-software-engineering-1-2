class Inventory:
    def __init__(self):
        self.inventory = []

    def create_product(self, product):
        self.inventory.append(product)

    def read_products(self):
        return self.inventory

    def update_product(self, index, updated_product):
        if 0 <= index < len(self.inventory):
            self.inventory[index] = updated_product
        else:
            raise IndexError("Product index out of range.")

    def delete_product(self, index):
        if 0 <= index < len(self.inventory):
            del self.inventory[index]
        else:
            raise IndexError("Product index out of range.")
