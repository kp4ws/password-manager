from tkinter import Frame, Label, Button, font, Scrollbar, Listbox, END, VERTICAL

class HomeView(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        font_header = font.Font(family="Helvetica", size=20, weight="bold")
        font_sub_header = font.Font(family="Helvetica", size=16)

        self.label_header = Label(self, text="Home", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")

        self.button_create = Button(self, text="Create Password", width=15, height=1)
        self.button_create.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        self.button_modify = Button(self, text="Modify Password", width=15, height=1)
        self.button_modify.grid(row=2, column=0, padx=10, pady=(0, 40), sticky="w")

        self.label_saved_passwords = Label(self, text="Saved Passwords", font=font_sub_header)
        self.label_saved_passwords.grid(row=3, column=0, padx=10, pady=(0,10), sticky="nw")

        self.listbox_saved_passwords = Listbox(self)
        self.listbox_saved_passwords.grid(row=4, column=0, padx=(10,200), pady=(0,10), sticky="nsew")

        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.listbox_saved_passwords.yview)
        self.scrollbar.grid(row=4, column=0, padx=(10,200), pady=(0,10), sticky="nse")

        self.label_password_details = Label(self, text="Password Details", font=font_sub_header)
        self.label_password_details.grid(row=3, column=1, padx=(0,100), pady=(0,10), sticky="nw")

        self.frame_password_details = Frame(self, highlightbackground="gray", highlightthickness=1)
        self.frame_password_details.grid(row=4, column=1, padx=10, pady=(0, 10), sticky="nsew")

        self.label_selected_title = Label(self.frame_password_details, text="Title:")
        self.label_selected_title.grid(row=4, column=1, padx=(0,100), pady=0, sticky="nw")

        self.listbox_saved_passwords.config(yscrollcommand=self.scrollbar.set)

        passwords = [
            {
                "title": "Password 123",
                "password": "123"
            },
            {
                "title": "Password fdsf",
                "password": "***"
            },
            {
               "title": "Password 342",
                "password": "fsdf"
            }
        ]

        for password in passwords:
            self.listbox_saved_passwords.insert(END, password['title'])
        
        self.listbox_saved_passwords.bind("<<ListboxSelect>>", self.on_select)

        self.rowconfigure(4, weight=1)

    def on_select(self, event):
        # Get the selected item from the listbox
        selection = self.listbox_saved_passwords.curselection()
        if selection:
            index = selection[0]
            selected_item = self.listbox_saved_passwords.get(index)
            # Update the password details label with the selected item
            self.label_selected_title.config(text=f"Title: {selected_item}")