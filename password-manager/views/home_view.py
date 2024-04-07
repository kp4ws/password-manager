'''
Primary Author: Kent Pawson
Contributor(s): N/A
'''

from tkinter import Frame, Label, Button, font, Scrollbar, Listbox, END, VERTICAL, messagebox
from root import Root

class HomeView(Frame):
    '''
    Serves as the View for the index screen of the application

    METHODS:
        __init__(self, root)
        _create_widgets(self)

    ATTRIBUTES:
        label_header: Label - Header label
        label_saved_passwords: Label - Saved passwords label
        label_password_details: Label - Password details label
        label_selected_title: Label - Selected title label
        listbox_saved_passwords: Listbox - Listbox with saved passwords
        scrollbar: Scrollbar - Scrollbar associated with the Listbox
        frame_password_details: Frame - Frame associated with the password details
        button_create: Button - Create button
        button_modify: Button - Modify button

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
        self.rowconfigure(5, weight=1)
        
        self._create_widgets()
    
    def _create_widgets(self) -> None:
        '''
        Create widgets for the view
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        font_header = font.Font(family="Helvetica", size=20, weight="bold")
        font_sub_header = font.Font(family="Helvetica", size=16)

        self.label_header = Label(self, text="Home", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")

        self.button_create = Button(self, text="Create Password", width=15, height=1)
        self.button_create.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        self.button_modify = Button(self, text="Modify Password", width=15, height=1)
        self.button_modify.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

        self.button_delete = Button(self, text="Delete Password", width=15, height=1)
        self.button_delete.grid(row=3, column=0, padx=10, pady=(0, 30), sticky="w")

        self.label_saved_passwords = Label(self, text="Saved Passwords", font=font_sub_header)
        self.label_saved_passwords.grid(row=4, column=0, padx=10, pady=(0,10), sticky="nw")

        self.listbox_saved_passwords = Listbox(self, width=30)
        self.listbox_saved_passwords.grid(row=5, column=0, padx=(10,50), pady=(0,10), sticky="nsew")

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.listbox_saved_passwords.yview)
        self.scrollbar.grid(row=5, column=0, padx=(10,50), pady=(0,10), sticky="nse")

        self.listbox_saved_passwords.config(yscrollcommand=self.scrollbar.set)

        self.label_password_details = Label(self, text="Password Details", font=font_sub_header)
        self.label_password_details.grid(row=4, column=1, padx=(0,10), pady=(0,10), sticky="nw")

        self.frame_password_details = Frame(self, width=350, height=100, highlightbackground="gray", highlightthickness=1)
        self.frame_password_details.grid(row=5, column=1, padx=(0,10), pady=(0, 10), sticky="nsew")
        self.frame_password_details.grid_propagate(False)

        self.label_selected_title = Label(self.frame_password_details, text="Title:")
        self.label_selected_title.grid(row=5, column=1, padx=(0,250), pady=0, sticky="nw")

        self.label_selected_url = Label(self.frame_password_details, text="URL:")
        self.label_selected_url.grid(row=6, column=1, padx=(0,250), pady=0, sticky="nw")

        self.label_selected_username = Label(self.frame_password_details, text="Username:")
        self.label_selected_username.grid(row=7, column=1, padx=(0,250), pady=0, sticky="nw")

        self.label_selected_password = Label(self.frame_password_details, text="Password:")
        self.label_selected_password.grid(row=8, column=1, padx=(0,250), pady=0, sticky="nw")

        self.label_selected_date = Label(self.frame_password_details, text="Date Created:")
        self.label_selected_date.grid(row=9, column=1, padx=(0,250), pady=0, sticky="nw")

    def show_selection_error(self) -> None:
        messagebox.showerror("Error", "No password selected")

    def show_delete_error(self) -> None:
        messagebox.showerror("Error", "Error occurred while deleting password, try again")

    def show_delete_confirmation_message(self, password_title) -> str:
        confirmation = messagebox.askquestion("Confirmation", f'Are you sure you want to delete {password_title} ?')
        return confirmation

    def show_delete_success(self) -> None:
        messagebox.showinfo("Success", "Password deleted")