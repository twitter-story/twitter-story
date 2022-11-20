from tkinter.constants import ANCHOR, N
from tkinter import Frame, Canvas, Entry, PhotoImage, N
from features.trends import trends



def trend():
    Trends()

def jo_Trend():
    jo='Trends in Jordan \n\n'
    
    ww='Trends in the world \n\n'
   
    for i in range (5):
        jo+=f"{i+1}) {trends()[0][i]} \n\n"
                        
        ww+=f'{i+1}) {trends()[1][i]} \n\n'
      
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
        #jo,ww=jo_Trend()
        canvas.pack()
        canvas.create_rectangle(10, 10, 340, 500, fill="#1D9BF0", outline="#1D9BF0")
        canvas.create_text(110, 200,font=('Helvetica','15','bold'), text='jo',fill='white')

        canvas.create_rectangle(390, 10, 770, 500, fill="#1D9BF0", outline="#1D9BF0")
        canvas.create_text(590, 200,font=('Helvetica','15','bold'), text='ww',fill='white')

        
        
        canvas.place(x=0, y=0)
