from tkinter import Tk, Label, Button, Entry, Listbox, END, Frame, PhotoImage, StringVar, DoubleVar, Toplevel
import controller
import model
import os

class GraphicalUserInterface:
    # Constructor
    def __init__(self, controller: controller.Inventory):
        # Make the controller an instance variable
        self.controller = controller
        # Create the main window
        self.window = Tk()
        # Set the title, size, and make it non-resizable
        self.window.title("Inventory Management System")
        self.window.geometry("800x500")
        self.window.resizable(False, False)
        # Create the listbox
        self.listbox = None
        self.create_gui()
    
    def create_gui(self):
        print("Creating GUI")
        label = Label(self.window, text="Inventory Management System", font=("Arial", 14)).pack()
        # List on the left
        self.listbox: Listbox = Listbox(self.window, width=30, height=500)
        # Make the listbox clickable, only one item can be selected at a time
        self.listbox.bind("<<ListboxSelect>>", self.load_view)
        self.listbox.pack(side="left")
        self.load_inventory()
        self.product_frame = Frame(self.window)
        
        button_frame = Frame(self.window)
        button_frame.pack(side="bottom")
        # buttons to manage the inventory item(s)
        Button(button_frame, text="Add Product", command=self.add_product_menu).pack()
        Button(button_frame, text="Delete Product", command=lambda: self.delete_product(self.listbox.curselection()[0])).pack()
        Button(button_frame, text="Update Product", command=self.update_product_menu).pack()
        Button(button_frame, text="Exit", command=self.window.quit).pack()
        
    def update_product_menu(self):
        # Create a new popup window
        popup = Toplevel(self.window)
        popup.title("Update Product")
        popup.geometry("400x300")
        
        # Variables to hold the input values
        product_name = StringVar()
        product_price = DoubleVar() 
        product_descripton = StringVar()
        product_image_par = StringVar()
        
        # Get the selected index
        index = self.listbox.curselection()[0]
        product = self.controller.read_products()[index]
        
        # Set the default values
        product_name.set(product.name)
        product_price.set(product.price)
        product_descripton.set(product.description)
        product_image_par.set(product.image_path)
        
        # Labels and Entry fields for product details
        Label(popup, text="Product Name").grid(row=0, column=0)
        name_entry = Entry(popup, textvariable=product_name)
        name_entry.grid(row=0, column=1)

        Label(popup, text="Price").grid(row=1, column=0)
        price_entry = Entry(popup, textvariable=product_price)
        price_entry.grid(row=1, column=1)

        Label(popup, text="Description").grid(row=2, column=0)
        description_entry = Entry(popup, textvariable=product_descripton)
        description_entry.grid(row=2, column=1)

        Label(popup, text="Image Path").grid(row=3, column=0)
        image_path_entry = Entry(popup, textvariable=product_image_par)
        image_path_entry.grid(row=3, column=1)
        
        Button(popup, text="Save", command=lambda: self.save_updated_product(popup, index, product_name, product_price, product_descripton, product_image_par)).grid(row=4, column=0)
        Button(popup, text="Cancel", command=popup.destroy).grid(row=4, column=1)
        
    def save_updated_product(self, popup, index, product_name, product_price, product_descripton, product_image_par):
        # Get the entered values
        name = product_name.get()
        price = product_price.get()
        description = product_descripton.get()
        image_path = product_image_par.get()
        
        # Create a new instance of the class with the updated values
        updated_product = model.Item(id=index + 1, name=name, price=price, description=description, image_path=image_path)
        
        # Update the product in the inventory
        self.controller.update_product(index, updated_product)
        
        # Reload the inventory list to reflect the updated product information
        self.load_inventory()
        
        popup.destroy()
        
    def add_product_menu(self):
        # Create a new popup window. Same as the update product menu
        popup = Toplevel(self.window)
        popup.title("Add Product")
        popup.geometry("400x300")
        
        product_name = StringVar()
        product_price = DoubleVar()
        product_descripton = StringVar()
        product_image_par = StringVar()
        
        Label(popup, text="Product Name").grid(row=0, column=0)
        name_entry = Entry(popup, textvariable=product_name)
        name_entry.grid(row=0, column=1)

        Label(popup, text="Price").grid(row=1, column=0)
        price_entry = Entry(popup, textvariable=product_price)
        price_entry.grid(row=1, column=1)

        Label(popup, text="Description").grid(row=2, column=0)
        description_entry = Entry(popup, textvariable=product_descripton)
        description_entry.grid(row=2, column=1)

        Label(popup, text="Image Path").grid(row=3, column=0)
        image_path_entry = Entry(popup, textvariable=product_image_par)
        image_path_entry.grid(row=3, column=1)
        
        Button(popup, text="Save", command=lambda: self.save_product(popup, product_name, product_price, product_descripton, product_image_par)).grid(row=4, column=0)
        Button(popup, text="Cancel", command=popup.destroy).grid(row=4, column=1)

    def save_product(self, popup, product_name, product_price, product_descripton, product_image_par):
        # Get the entered values
        name = product_name.get()
        price = product_price.get()
        description = product_descripton.get()
        image_path = product_image_par.get()

        # Create a new instance of the class
        new_product = model.Item(id=len(self.controller.read_products()) + 1, name=name, price=price, description=description, image_path=image_path)
        
        self.add_product(new_product)
        self.load_inventory()
        popup.destroy()

        
    def delete_product(self, index):
        self.controller.delete_product(index)
        self.load_inventory()
        
    def add_product(self, product):
        self.controller.create_product(product)
        
    def load_view(self, event):
        # Get the selected index
        index = self.listbox.curselection()[0]
        product = self.controller.read_products()[index]
        
        self.product_frame.pack_forget()
        
        self.product_frame = Frame(self.window)
        self.product_frame.pack()
        
        Label(self.product_frame, text=f"Name: {product.name}").grid(row=0, column=0)
        Label(self.product_frame, text=f"Price: ${product.price}").grid(row=1, column=0)
        Label(self.product_frame, text=f"Description: {product.description}").grid(row=2, column=0)

        if not os.path.exists(product.image_path):
            raise FileNotFoundError(f"Image file not found: {product.image_path}")

        self.image = PhotoImage(file=product.image_path)
        
        Label(self.product_frame, image=self.image).grid(row=3, column=0)
        
        
    def load_inventory(self):
        # Clear the listbox
        self.listbox.delete(0, END)
        
        for product in self.controller.read_products():
            self.listbox.insert(END, product)
        
    def run(self):
        self.window.mainloop()