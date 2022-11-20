from tkinter import *
from features.sentiment_analysis import *
from features.userName_tweets import *


def sentiment():
    Sentiment()





class Sentiment(Frame):
    
    def show_img(self,username):
        df=user_tweets(username)
        tweets=sentiment_analysis(df)
        percentage(tweets)
        canvas = Canvas(
                self,
                bg="#FFFFFF",
                height=432,
                width=797,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )
        canvas.place(x=0, y=0)
        canvas.pack()
        self.image_sen= PhotoImage(file=("Sentiment_Analysis.png"))
        canvas.create_image(300, 200,image=self.image_sen)


    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        
        self.entry_image_2 = PhotoImage(file="assets/button_3.png")
        entry_User= Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_User.insert(-1, 'username ')
        entry_User.place(x=35.0, y=110.0, width=208.0, height=47)
        self.write_tweet_btn = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_img(entry_User.get()),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
    )
        self.write_tweet_btn.place(x=35.0, y=200, width=208.0, height=47.0)
        
