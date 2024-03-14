from tkinter import Frame, Label

class CreatePasswordView(Frame):
   def __init__(self, root):
      super().__init__(root)
      self.grid(row=0, column=0, sticky="nsew")
      self.grid_columnconfigure(0, weight=1)