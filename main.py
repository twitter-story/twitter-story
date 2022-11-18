import tkinter as tk
from gui.welcome import welcome

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window

# root.iconbitmap("assets/favicon.ico")


if __name__ == "__main__":
    root.iconbitmap("favicon.ico")

    welcome()
    # mainWindow()
    

    root.mainloop()