from tkinter import Tk, Label, Button, Entry, messagebox, Listbox, END, Frame, PhotoImage
import controller

class GraphicalUserInterface:
    def __init__(self, controller: controller.Inventory):
        self.controller = controller
        self.window = Tk()
        self.window.title("Inventory Management System")
        self.window.geometry("800x500")
        self.window.resizable(False, False)
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
        # self.image 
        self.product_frame = Frame(self.window)
        
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
        
        self.image = PhotoImage(file=product.image_path)
        
        Label(self.product_frame, image=self.image).grid(row=3, column=0)
        
        
        

    
    def load_inventory(self):
        # Clear the listbox
        self.listbox.delete(0, END)
        
        for product in self.controller.read_products():
            self.listbox.insert(END, product)
            
        
    def run(self):
        self.window.mainloop()