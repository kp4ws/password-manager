from tkinter import Frame, Label, Button, font, DISABLED, Canvas, messagebox
from root import Root
import random

class IndexView(Frame):
    '''
    Serves as the View for the index screen of the application

    METHODS:
        __init__(self, root)
        _create_widgets(self)

    ATTRIBUTES:
        label_header: Label - Header label
        button_enter: Button - Enter button

    INTERFACE INFO:
        N/A
    '''
    
    def __init__(self, root: Root) -> None:
        '''
        Initializes the object
        :arg self: Required by python
        :arg root: Root window of the application
        :except No exceptions thrown by this method
        :return None
        '''
        super().__init__(root)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        self._create_widgets()
    
    def _create_widgets(self) -> None:
        '''
        Create widgets for the view
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        font_header = font.Font(family="Helvetica", size=20, weight="bold")
        font_subscript = font.Font(family="Helvetica", size=8, slant="italic")

        self.label_header = Label(self, text="Manage Your Passwords", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(50, 10), sticky="ew")

        self.button_enter = Button(self, text="Enter", width=20, height=1, state=DISABLED)
        self.button_enter.grid(row=1, column=0, padx=10, pady=(0,10))

        self.label_captcha = Label(self, text="CAPTCHA: To enter, touch the red square using the arrow keys", font=font_subscript)
        self.label_captcha.grid(row=2, column=0, padx=10, pady=(10, 0))

        self._create_captcha_canvas()

    def _create_captcha_canvas(self) -> None:
        self.canvas_game = Canvas(self, width=360, height=280, bg="white")
        self.canvas_game.grid(row=3, column=0, padx=10, pady=0)

        self.goal = self.canvas_game.create_rectangle(80, 80, 130, 130, fill="red")
        self.player = self.canvas_game.create_rectangle(160, 160, 210, 210, fill="blue")

        self.canvas_game.focus_set()

    def show_captcha_error(self) -> None:
        messagebox.showerror("Error", "Please complete the captcha to enter the application")

    def show_captcha_success(self) -> None:
        messagebox.showinfo("Success", "Captcha completed!")