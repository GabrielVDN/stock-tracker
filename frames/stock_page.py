import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas
import requests


class StockPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(1, weight=1)

        # Add some buttons.
        button_1 = ttk.Button(
            self,
            text="Add New Product",
            command=lambda: controller.show_frame("AddNewProd"),
            width=19
        )
        button_1.grid(row=0, column=0, padx=(70, 10), pady=8, sticky="E")

        button_2 = ttk.Button(
            self,
            text="Delete Product",
            command=lambda: controller.show_frame("DeleteProd"),
            width=19
        )
        button_2.grid(row=0, column=1, pady=8, sticky="W")

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=3, padx=8, pady=8, sticky="NE")


    def redraw_tables(self):
        # The data from th API
        self.request = requests.get("http://127.0.0.1:8000/products/", auth=("gabriel", "1"))

        # Transform the API's data to the TableCanvas' form.
        # Use the unique index for the rows in the TableCanvas.
        data = {}
        for i in self.request.json():
            data[self.request.json().index(i)] = i

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=2, columnspan=4)
        self.table = TableCanvas(
            tframe,
            data=data,
            read_only=True,
            width=1300,
            height=600,
            cellwidth=330,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            rowselectedcolor=None,  # Get rid of the row selection.
            selectedcolor=None, # Get rid of the cell selection.
            thefont=('Arial', 15),
            borderwidht=10
        )
        self.table.show()
        
        
    def focus_on_entry(self):
        pass