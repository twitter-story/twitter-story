from tkinter import *
from features.sentiment_analysis import *
from features.userName_tweets import *
from PIL import Image,ImageTk


def fact():
    Fact()


class Fact(Frame):
    
    def show_img(self,username):
        df=user_tweets(username)
        tweets=sentiment_analysis(df)
        percentage(tweets)
        self.canvas.delete('item')

        img= (Image.open("Sentiment_Analysis.png"))

        resized_image= img.resize((475,350))
        self.new_image= ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(250,20, anchor=NW, image=self.new_image,tag='item')

    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")
        self.canvas = Canvas(
                self,
                bg="#FFFFFF",
                height=432,
                width=797,
                bd=0,
                highlightthickness=0,
                relief="ridge",
            )
        self.canvas.place(x=0, y=0)

        self.entry_image_2 = PhotoImage(file="assets/Asset_3.png")
        self.canvas.create_image(120, 120.0, image=self.entry_image_2)
        entry_User= Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_User.insert(0,'write your text ')
        entry_User.place(x=35.0, y=110.0, width=185.0, height=30)



        self.button_Analyze = PhotoImage(file=("assets/Asset_8.png"))
        self.write_tweet_btn = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_img(entry_User.get()),
            image=self.button_Analyze,
            cursor='hand2',
            relief="flat",
    )
        self.write_tweet_btn.place(x=20.0, y=200, width=208.0, height=47.0)