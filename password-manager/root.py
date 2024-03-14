from tkinter import Tk

class Root(Tk):
    '''
    Serves as the root window configuration for the application
    '''
    WINDOW_WIDTH: int = 1080
    WINDOW_HEIGHT: int = 640

    def __init__(self) -> None:
        super().__init__()
        
        self.title("Password Manager")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self._center_window()

    def _center_window(self) -> None:
        x_coord = (self.winfo_screenwidth() // 2) - (self.WINDOW_WIDTH // 2)
        y_coord = (self.winfo_screenheight() // 2) - (self.WINDOW_HEIGHT // 2)
        self.geometry(f'{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{x_coord}+{y_coord}')

    def begin_loop(self) -> None:
        self.mainloop()