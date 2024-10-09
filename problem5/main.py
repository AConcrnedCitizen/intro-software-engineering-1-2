'''
*******************************
Author:
u3275885
Assignment:
Assessment 2 - Problem 5
4/10/2024
*******************************
'''

import model
import view
from controller import Inventory

# Create an instance of the Inventory class
inv = Inventory()

# Create an instance of the GraphicalUserInterface class
view = view.GraphicalUserInterface(inv)
# Start the main loop
view.run()

