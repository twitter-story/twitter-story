from pathlib import Path
from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from gui.main_windows import *




def welcome():
    Welcome()



class Welcome(Toplevel):

    def welcome_function(self):
        self.destroy()
        mainWindow()
        return


    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        #self.iconbitmap('../assets/favicon.ico')
        self.iconbitmap("favicon.ico")

        self.title("Welcome - Twiter Story")

        self.geometry("1012x506")
        self.configure(bg="#111D29")

        self.canvas = Canvas(
            self,
            bg="#111D29",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#1D9BF0", outline=""
        )


        button_image_1 = PhotoImage(file=("assets/button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.welcome_function,
            relief="flat",
        )
        button_1.place(x=600.0, y=210.0, width=272.0, height=65.0)

        self.canvas.create_text(
            75.0,
            77.0,
            anchor="nw",
            text="Twitter Story",
            fill="#FFFFFF",
            font=("Montserrat Bold", 50 * -1),
        )

     




        self.canvas.create_text(
            80,
            431.0,
            anchor="nw",
            text="© Twitter Story, 2022",
            fill="#FFFFFF",
            font=("Montserrat Bold", 18 * -1),
        )

        image_image_1 = PhotoImage(file=("assets/logo.png"))
        image_1 = self.canvas.create_image(458.0, 326.0, image=image_image_1)

        self.canvas.create_text(
            80.0,
            150.0,
            anchor="nw",
            text='''
Twitter Story App 
give you abilites to
see the trends 
search about what do you want 
make a tweet 
and more ...             
''',
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )


        self.resizable(False, False)
        self.mainloop()