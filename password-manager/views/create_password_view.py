from tkinter import Frame, Label, font

class CreatePasswordView(Frame):
   def __init__(self, root):
      super().__init__(root)
      self.grid(row=0, column=0, sticky="nsew")
      self.grid_columnconfigure(0, weight=1)

      font_header = font.Font(family="Helvetica", size=20, weight="bold")

      self.label_header = Label(self, text="Create Password", font=font_header)
      self.label_header.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")