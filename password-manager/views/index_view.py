'''
Primary Author: Kent Pawson
Contributor(s): N/A
'''

import tkinter as tk
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

        self.label_captcha = Label(self, text="CAPTCHA the flag", font=font_subscript)
        self.label_captcha.grid(row=2, column=0, padx=10, pady=(10, 0))

        self._create_captcha_canvas()

    def _create_captcha_canvas(self) -> None:
        self.canvas_game = Canvas(self, width=360, height=280, bg="lightgrey", highlightthickness=0)
        self.canvas_game.grid(row=3, column=0, padx=10, pady=0)

        self.image_red_flag = tk.PhotoImage(file='./assets/redflag.gif')
        self.image_green_flag = tk.PhotoImage(file='./assets/greenflag.gif')
        self.image_player = tk.PhotoImage(file='./assets/player.gif')
        
        flag_x = random.randint(20,300)
        flag_y = random.randint(20,300)

        player_x = random.randint(50,260)
        player_y = random.randint(50,260)

        distance = 100

        #Prevents flag from spawning on player
        while(abs(flag_x - player_x) < distance and abs(flag_y - player_y) < distance):
            flag_x = random.randint(20,300)
            flag_y = random.randint(20,300)

        self.green_flag = self.canvas_game.create_image((flag_x, flag_y), image=self.image_green_flag)
        self.red_flag = self.canvas_game.create_image((flag_x, flag_y), image=self.image_red_flag)
        self.player = self.canvas_game.create_image((player_x, player_y), image=self.image_player)

        self.canvas_game.focus_set()

    def show_captcha_error(self) -> None:
        messagebox.showerror("Error", "Please complete the captcha to enter the application")