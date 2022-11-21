from tkinter import *
from features.user_Information import *
from urllib.request import urlopen
from PIL import Image, ImageTk


def information():
    Information()


class Information(Frame):
    def user_in(self, user):
        x = Get_user_Information(user)
        print(x)

        All_tweets = ''
        for i, j in x.items():
            All_tweets += f' {i} : {j} \n\n '

        self.canvas.create_text(
            260.0,
            12.0,
            anchor="nw",
            text=All_tweets,
            width=500,
            fill="#000000",
            font=("Montserrat 10 Bold", 18 * -1),
        )

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

        # image_url = "https://pbs.twimg.com/profile_images/1575103661847597065/mG1Vb8Cc_400x400.jpg"
        # u = urlopen(image_url)
        # raw_data = u.read()
        # u.close()
        # self.canvas.L = ImageTk.PhotoImage(data=raw_data)

        # # resized_image = self.canvas.L.resize((300, 205), Image.ANTIALIAS)

        # image_1 = self.canvas.create_image(458.0, 200.0, image=self.canvas.L )

        # # entry_bg_1 = self.canvas.create_image(125.0, 122.0, image=photo)

        entry_User = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_User.insert(-1, 'username ')
        entry_User.place(x=35.0, y=110.0, width=185.0, height=30)

        self.button_Analyze = PhotoImage(file=("assets/Asset_8.png"))
        self.write_tweet_btn = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.user_in(entry_User.get()),
            image=self.button_Analyze,
            cursor='hand2',
            relief="flat",
        )
        self.write_tweet_btn.place(x=20.0, y=200, width=208.0, height=47.0)