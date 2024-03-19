from tkinter import Frame, Label, font, Button, StringVar, Entry
from root import Root

class CreatePasswordView(Frame):
    '''
    Serves as the View for the create password screen of the application

    METHODS:
        __init__(self, root)
        _create_widgets(self)

    ATTRIBUTES:
        label_header: Label - Header label

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
        self.grid_columnconfigure(2, weight=1)
        self.rowconfigure(4, weight=1)
        
        self.label_header = None
        self.button_back = None
        self.label_title = None
        self.var_title = StringVar()
        self.entry_title = None

        self._create_widgets()
    
    def _create_widgets(self) -> None:
        '''
        Create widgets for the view
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        font_header = font.Font(family="Helvetica", size=20, weight="bold")
        font_field = font.Font(family="Helvetica", size=11)

        self.label_header = Label(self, text="Create Password", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")

        self.label_title = Label(self, text="Title:", font=font_field)
        self.label_title.grid(row=1, column=0, padx=(10,0), pady=0, sticky="w")
        self.entry_title = Entry(self, textvariable=self.var_title)
        self.entry_title.grid(row=1, column=1, padx=(10,0), pady=0, sticky="w")

        self.label_title = Label(self, text="URL:", font=font_field)
        self.label_title.grid(row=2, column=0, padx=(10,0), pady=0, sticky="w")
        self.entry_title = Entry(self, textvariable=self.var_title)
        self.entry_title.grid(row=2, column=1, padx=(10,0), pady=0, sticky="w")

        self.label_title = Label(self, text="Username:", font=font_field)
        self.label_title.grid(row=3, column=0, padx=(10,0), pady=0, sticky="w")
        self.entry_title = Entry(self, textvariable=self.var_title)
        self.entry_title.grid(row=3, column=1, padx=(10,0), pady=0, sticky="w")

        self.label_title = Label(self, text="Password:", font=font_field)
        self.label_title.grid(row=4, column=0, padx=(10,0), pady=0, sticky="w")
        self.entry_title = Entry(self, textvariable=self.var_title)
        self.entry_title.grid(row=4, column=1, padx=(10,0), pady=0, sticky="w")

        self.button_clear = Button(self, text="Clear Input", width=15, height=1)
        self.button_clear.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")

        self.button_back = Button(self, text="Exit Without Saving", width=15, height=1)
        self.button_back.grid(row=5, column=1, padx=10, pady=(0, 10), sticky="w")
        
        self.button_submit = Button(self, text="Save and Submit", width=15, height=1)
        self.button_submit.grid(row=5, column=2, padx=10, pady=(0, 10), sticky="w")