from tkinter import Tk

class Root(Tk):
    '''
    Root window of the application. Responsible for setting the window configuration
    
    METHODS:
        __init__(self)
        _center_window(self)
        begin_loop(self)

    ATTRIBUTES:
        WINDOW_WIDTH: int - Width of the window
        WINDOW_HEIGHT: int - Height of the window

    INTERFACE INFO:
        To begin the application, call begin_loop() method
    '''
    
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 500

    def __init__(self) -> None:
        '''
        Initializes the object
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        super().__init__()
        
        self.title("Password Manager")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self._center_window()

    def _center_window(self) -> None:
        '''
        Centers the window on screen
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        x_coord = (self.winfo_screenwidth() // 2) - (self.WINDOW_WIDTH // 2)
        y_coord = (self.winfo_screenheight() // 2) - (self.WINDOW_HEIGHT // 2)
        self.geometry(f'{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{x_coord}+{y_coord}')

    def begin_loop(self) -> None:
        '''
        Begins the main loop of the window
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.mainloop()