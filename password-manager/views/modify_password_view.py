from tkinter import Frame, Label, font, Button, StringVar, Entry, messagebox
from root import Root

class ModifyPasswordView(Frame):
    '''
    Serves as the View for the modify password screen of the application

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
        self.rowconfigure(6, weight=1)
        
        self.label_header = None
        self.button_back = None
        
        #Title
        self.label_title = None
        self.entry_title = None
        self.var_title = StringVar()

        #URL
        self.label_url = None
        self.entry_url = None
        self.var_url = StringVar()

        #Username
        self.label_username = None
        self.entry_username = None
        self.var_username = StringVar()

        #Password
        self.label_password = None
        self.entry_password = None
        self.var_password = StringVar()

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

        self.label_header = Label(self, text="Modify Password", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")

        self.label_title = Label(self, text="Title:", font=font_field)
        self.label_title.grid(row=1, column=0, padx=(10,0), pady=(0,5), sticky="nw")
        self.entry_title = Entry(self, textvariable=self.var_title)
        self.entry_title.grid(row=1, column=1, padx=(10,0), pady=(0,5), sticky="nw")

        self.label_url = Label(self, text="URL:", font=font_field)
        self.label_url.grid(row=2, column=0, padx=(10,0), pady=(0,5), sticky="nw")
        self.entry_url = Entry(self, textvariable=self.var_url)
        self.entry_url.grid(row=2, column=1, padx=(10,0), pady=(0,5), sticky="nw")

        self.label_username = Label(self, text="Username:", font=font_field)
        self.label_username.grid(row=3, column=0, padx=(10,0), pady=(0,5), sticky="nw")
        self.entry_username = Entry(self, textvariable=self.var_username)
        self.entry_username.grid(row=3, column=1, padx=(10,0), pady=(0,5), sticky="nw")

        self.label_password = Label(self, text="Password:", font=font_field)
        self.label_password.grid(row=4, column=0, padx=(10,0), pady=(0,5), sticky="nw")
        self.entry_password = Entry(self, textvariable=self.var_password)
        self.entry_password.grid(row=4, column=1, padx=(10,0), pady=(0,5), sticky="nw")

        self.button_back = Button(self, text="Exit Without Saving", width=15, height=1)
        self.button_back.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="nw")
        
        self.button_submit = Button(self, text="Save and Update", width=15, height=1)
        self.button_submit.grid(row=6, column=0, padx=10, pady=(0, 10), sticky="nw")

    def show_general_error(self) -> None:
        messagebox.showerror("Error", "Passwords must have a title, username, and password")

    def show_password_length_error(self) -> None:
        messagebox.showerror("Error", "Password field must be between 8 and 16 characters inclusive")

    def show_error_updating_password(self) -> None:
        messagebox.showerror("Error", "Error occured while modifying the password")

    def show_success(self) -> None:
        messagebox.showinfo("Success", "Password updated")