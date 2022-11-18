import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from features.tweets import tweet

class LoginPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626) 
        main_frame.pack(fill="both", expand="true")

        self.geometry("626x431") 
        self.resizable(0, 0)
        title_styles = {"font": ("Trebuchet MS Bold", 16), "background": "blue"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "blue",
                       "foreground": "#E1FFFF"}

        frame_login = tk.Frame(main_frame, bg="blue", relief="groove", bd=2)
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, title_styles, text="search")
        label_title.grid(row=0, column=1, columnspan=1)

        label_user = tk.Label(frame_login, text_styles, text="search:")
        label_user.grid(row=1, column=0)

        entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        entry_user.grid(row=1, column=1)

        button = ttk.Button(frame_login, text="Login", command=lambda: tweets())
        button.place(rely=0.70, relx=0.50)


        def tweets():
            username = entry_user.get()
            # messagebox.showinfo("Say Hello", "Hello World")
            tk.messagebox.showinfo("done","{}".format(tweet(username)))


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)


top = LoginPage()
top.title("Tkinter App Template - Login Page")
root = MyApp()
root.withdraw()
root.title("Tkinter App Template")

root.mainloop()