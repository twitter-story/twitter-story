from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from features.tweets import tweet as t


class Tweet(tk.Tk):


    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Twitter Story")

        self.geometry("1012x506")

        self.canvas = Canvas(
            self,
            bg="#5E95FF", 
            height=1000,
            width=1012,
      
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )
        entry_image = PhotoImage(file="gui/entry_2.png")
        entry_bg = self.canvas.create_image(736.0, 229.0, image=entry_image)
        entry = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry.place(x=568.0, y=192.0, width=336.0, height=0)

    
        self.canvas.create_text(
            573.0,
            204.0,
            anchor="nw",
            text="search",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )


        self.canvas.create_text(
            553.0,
            66.0,
            anchor="nw",
            text="Search tweets",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        button_image_1 = PhotoImage(file=("gui/button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_Tweets,
            relief="flat",
        )
        button_1.place(x=641.0, y=412.0, width=190.0, height=48.0)

        self.canvas.create_text(
            80.0,
            77.0,
            anchor="nw",
            text="Twitter Story",
            fill="#FFFFFF",
            font=("Montserrat Bold", 50 * -1),
        )

        self.canvas.create_text(
            553.0,
            109.0,
            anchor="nw",
            text="Enter any keywords or user",
            fill="#CCCCCC",
            font=("Montserrat Bold", 16 * -1),
        )


        entry_image_3 = PhotoImage(file=("gui/entry_3.png"))
        entry_bg_3 = self.canvas.create_image(736.0, 241.0, image=entry_image_3)
        self.search = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
        )
        self.search.place(x=573.0, y=229.0, width=326.0, height=22.0)

        self.canvas.create_text(
            90.0,
            431.0,
            anchor="nw",
            text="© twitter story",
            fill="#FFFFFF",
            font=("Montserrat Bold", 18 * -1),
        )

        # self.resizable(False, False)
        self.mainloop()


    def result(self,quary):
        self.canvas.create_text(
            341.0,
            213.0,
            anchor="nw",
            text=f(quary),
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )
    def print_Tweets(self):
        quary = self.search.get()
        x=t(quary)
        All_tweets='''
        '''
        for tweet in x :
            All_tweets+=f'''
            {tweet}
            '''
        return x


    def search_Tweets(self):
        self.canvas.create_text(
            556.0,
            300.0,
            anchor="nw",
            text=self.print_Tweets(),
            fill="#5E95FF",
            font=("Montserrat Bold", 12 * -1),
        )
    

root = Tweet()

root.mainloop()