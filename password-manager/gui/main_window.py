import tkinter as tk

class MainWindow:
    '''
    Serves as the MainWindow for the application
    '''
    WINDOW_WIDTH: int = 400
    WINDOW_HEIGHT: int = 300

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Password Manager")
        self.root.resizable(False, False)
        self._center_window()

    def _center_window(self) -> None:
        x_coord = (self.root.winfo_screenwidth() // 2) - (self.WINDOW_WIDTH // 2)
        y_coord = (self.root.winfo_screenheight() // 2) - (self.WINDOW_HEIGHT // 2)
        self.root.geometry(f'{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{x_coord}+{y_coord}')
