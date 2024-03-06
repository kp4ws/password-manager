import tkinter as tk
from gui import MainWindow

def _main() -> None:
    root: tk.Tk = tk.Tk()
    app: MainWindow = MainWindow(root)
    root.mainloop()
    print(type(app))

if __name__ == '__main__':
    _main()