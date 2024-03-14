from tkinter import Frame, Label

class HomeView(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="HOME")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


        