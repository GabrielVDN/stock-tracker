import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox

class DeleteProd(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Scan barcode")
        label.grid(row=0, columnspan=2, pady=8)

        # Add some buttons.
        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=1, padx=8, pady=8, sticky="NE")

        delete_button = ttk.Button(
            self,
            text="Delete",
            command=lambda: self.aks_delete(),
            width=20
        )
        delete_button.grid(row=2, columnspan=2)

        self.entry_barcode = ttk.Entry(self, font=("TkDefaultFont", 20))
        self.entry_barcode.grid(row=1, columnspan=2, pady=40)


    def focus_on_entry(self):
        self.entry_barcode.focus()

    def aks_delete(self):
        if messagebox.askokcancel("Delete", "Are you sure you want delete this?!") == True:
            print("This item has bean deleted!!!")
        self.entry_barcode.focus()
