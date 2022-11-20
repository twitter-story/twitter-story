from tkinter.constants import ANCHOR, N
from tkinter import *
from features.manage_tweets import write_tweet



def tweet():
    Tweet()


class Tweet(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.pack()
        self.entry_image_2 = PhotoImage(file="assets/button_3.png")
        entry_User= Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_User.insert(0, 'Write your tweet ')
        entry_User.place(x=35.0, y=110.0, width=600.0, height=100)
        self.write_tweet_btn = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: write_tweet(entry_User.get()),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
    )
        self.write_tweet_btn.place(x=427.0, y=250, width=208.0, height=47.0)
    
        
        canvas.place(x=0, y=0)
