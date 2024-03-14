from tkinter import Frame, Label, Button, font

class IndexView(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        font_header = font.Font(family="Helvetica", size=20, weight="bold")

        self.label_header = Label(self, text="Manage Your Passwords", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(90, 10), sticky="ew")

        self.button_enter = Button(self, text="Enter", width=20, height=1)
        self.button_enter.grid(row=1, column=0, padx=10, pady=10)