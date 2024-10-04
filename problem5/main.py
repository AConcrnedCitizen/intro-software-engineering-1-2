import model
import view
from controller import Inventory


a = Inventory()

def dummy_data():
    a.create_product(model.Groceries("1", "Apple", 1.99, "Fresh apple", "C:\\Users\\Conall\\Documents\\Projects\\intro-software-engineering-1-2\\problem5\\a.png", "2021-12-31"))
    

dummy_data()

view = view.GraphicalUserInterface(a)
view.run()

