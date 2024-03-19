from tkinter import Frame, Label, font
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
      
        self.label_header = Label(self, text="Modify Password", font=font_header)
        self.label_header.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="w")