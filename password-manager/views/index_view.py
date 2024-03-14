from tkinter import Frame, Label, Button

class IndexView(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Manage Your Passwords")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.enter_btn = Button(self, text="Enter")
        self.enter_btn.grid(row=2, column=0, padx=10, pady=10)