from tkinter.constants import ANCHOR, N
from tkinter import Frame, Canvas, Entry, PhotoImage, N ,Button, PhotoImage, messagebox
from features.trends import trends



def trend():
    Trends()

def jo_Trend():
    jo=''
    
    ww=''
   
    for i in range (5):
        jo+=f" {trends()[0][i]} \n\n"
                        
        ww+=f' {trends()[1][i]} \n\n'
      
    return jo,ww


class Trends(Frame):
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
        jo,ww=jo_Trend()
        canvas.pack()

        self.entry_image_5 = PhotoImage(file=("assets/trends_1.png"))
        entry_bg_5 = canvas.create_image(198, 230.0, image=self.entry_image_5)

        canvas.create_text(
            120.0,
            60.0,
            anchor="nw",
            text="# Jordan",
            fill="#1D9BF0",
            font=("Montserrat Bold", 25 ),
        )

        canvas.create_rectangle(
            80.0, 125.0, 310.0, 127.0, fill="#777777", outline=""
        )

        canvas.create_text(155, 282,font=('Helvetica','15','bold'), text=jo ,fill='#1D9BF0')







        self.entry_image_6 = PhotoImage(file=("assets/trends_1.png"))
        entry_bg_5 = canvas.create_image(565, 230.0, image=self.entry_image_6)

        canvas.create_text(
            465.0,
            60.0,
            anchor="nw",
            text="# WorldWide",
            fill="#1D9BF0",
            font=("Montserrat Bold", 25 ),
        )

        canvas.create_rectangle(
            447.0, 125.0, 677.0, 127.0, fill="#777777", outline=""
        )


        canvas.create_text(522, 282,font=('Helvetica','15','bold'), text=ww ,fill='#1D9BF0')

        
        
        canvas.place(x=0, y=0)