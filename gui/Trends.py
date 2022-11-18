from tkinter.constants import ANCHOR, N
from tkinter import Frame, Canvas, Entry, PhotoImage, N
from features.trends import trends



def trend():
    Trends()

def jo_Trend():
    jo='''
    '''
    ww='''
    '''
    for i in range (5):
        jo+=f'''{trends()[0][i]} \n
                        '''
        ww+=f'''{trends()[1][i]} \n
        '''
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
        canvas.create_text(
            250,
            100,
            anchor="nw",
            text=jo_Trend()[0],
            fill="#000000",
            font=("Montserrat Bold", 24 * -1),
        )

        canvas.place(x=0, y=0)
