from tkinter import *
from features.user_Information import *
import urllib.request
import io
from PIL import Image, ImageTk


def information():
    Information()


class Information(Frame):
    def user_in(self, user):

        self.canvas.delete('del')
        
        x = Get_user_Information(user)
        # print(x)

        All_tweets = ''
        for i, j in x.items():
            if i!='Profile_image':
                if j!='':
                    All_tweets += f'{i} : {j}\n\n'
            else:
                image_url = j

                with urllib.request.urlopen(image_url) as u:
                    raw_data = u.read()
                image = Image.open(io.BytesIO(raw_data))
                resized_image= image.resize((100,100))

                self.image = ImageTk.PhotoImage(resized_image)
                self.canvas.create_image(360.0, 62.0, image=self.image , tags='del')

        self.canvas.create_text(
            430.0,
            12.0,
            anchor="nw",
            text=All_tweets,
            width=300,
            fill="#111D29",
            font=("Montserrat 10 Bold", 18 * -1),
            tags='del',
        )
        
        
        self.entry_User.destroy()


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

        self.canvas.create_rectangle(
            280.0, 12.0, 282.0, 500.0, fill="#777777", outline=""
        )


        self.entry_image_2 = PhotoImage(file="assets/Asset_3.png")
        self.canvas.create_image(140, 170.0, image=self.entry_image_2)
        entry_User= Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_User.insert(0,'username')
        entry_User.place(x=60.0, y=155.0, width=185.0, height=30)

        self.button_Analyze = PhotoImage(file=("assets/Get_Info.png"))
        self.write_tweet_btn = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.user_in(entry_User.get()),
            image=self.button_Analyze,
            cursor='hand2',
            relief="flat",
        )
        self.write_tweet_btn.place(x=35.0, y=300, width=208.0, height=47.0)