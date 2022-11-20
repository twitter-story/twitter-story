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


        self.entry_image_10 = PhotoImage(file="assets/Asset_5.png")
        entry_bg_4 = canvas.create_image(330.0, 160.0, image=self.entry_image_10)
        entry_User= Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_User.insert(0, 'Write your tweet ')
        entry_User.place(x=70.0, y=110.0, width=500.0, height=100)
        
        self.button_tweet = PhotoImage(file=("assets/Asset_4.png"))
        self.write_tweet_btn = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: write_tweet(entry_User.get()),
            image=self.button_tweet,
            cursor='hand2', activebackground="#111D29",
            relief="flat",
    )
        self.write_tweet_btn.place(x=427.0, y=250, width=208.0, height=47.0)
    
        
        canvas.place(x=0, y=0)
