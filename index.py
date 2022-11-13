import tkinter as tk
import tkinter.font as tkFont
from features.tweets import tweet

class App:
    def __init__(self, root):
        #setting title
        root.title("Twitter")
        #setting window size
        width=640
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_315=tk.Button(root)
        GButton_315["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_315["font"] = ft
        GButton_315["fg"] = "#000000"
        GButton_315["justify"] = "center"
        GButton_315["text"] = "search"
        GButton_315.place(x=280,y=150,width=70,height=25)
        GButton_315["command"] = self.GButton_315_command

        GLineEdit_78=tk.Entry(root)
        GLineEdit_78["bg"] = "#999999"
        GLineEdit_78["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_78["font"] = ft
        GLineEdit_78["fg"] = "#91c5f9"
        GLineEdit_78["justify"] = "center"
        GLineEdit_78["text"] = "enter hashtag"
        GLineEdit_78.place(x=170,y=150,width=100,height=25)

        GLabel_209=tk.Label(root)
        GLabel_209["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_209["font"] = ft
        GLabel_209["fg"] = "#333333"
        GLabel_209["justify"] = "center"
        GLabel_209["text"] = "Topic"
        GLabel_209.place(x=10,y=150,width=140,height=25)

        GLabel_981=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_981["font"] = ft
        GLabel_981["fg"] = "#333333"
        GLabel_981["justify"] = "center"
        GLabel_981["text"] = "Wlcome to Twitter story app"
        GLabel_981.place(x=230,y=10,width=190,height=25)

        GLabel_286=tk.Label(root)
        GLabel_286["bg"] = "#fefdfd"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_286["font"] = ft
        GLabel_286["fg"] = "#333333"
        GLabel_286["justify"] = "center"
        GLabel_286["text"] = "By user"
        GLabel_286.place(x=10,y=190,width=140,height=25)

        GLineEdit_410=tk.Entry(root)
        GLineEdit_410["bg"] = "#999999"
        GLineEdit_410["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_410["font"] = ft
        GLineEdit_410["fg"] = "#91c5f9"
        GLineEdit_410["justify"] = "center"
        GLineEdit_410["text"] = "enter username"
        GLineEdit_410.place(x=170,y=190,width=100,height=25)

        GButton_37=tk.Button(root)
        GButton_37["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_37["font"] = ft
        GButton_37["fg"] = "#000000"
        GButton_37["justify"] = "center"
        GButton_37["text"] = "search"
        GButton_37.place(x=280,y=190,width=70,height=25)
        GButton_37["command"] = self.GButton_37_command

        GButton_319=tk.Button(root)
        GButton_319["bg"] = "#58ecf7"
        ft = tkFont.Font(family='Times',size=10)
        GButton_319["font"] = ft
        GButton_319["fg"] = "#000000"
        GButton_319["justify"] = "center"
        GButton_319["text"] = "Top Trends"
        GButton_319.place(x=40,y=60,width=70,height=25)
        GButton_319["command"] = self.GButton_319_command

        GButton_45=tk.Button(root)
        GButton_45["bg"] = "#f971fe"
        ft = tkFont.Font(family='Times',size=10)
        GButton_45["font"] = ft
        GButton_45["fg"] = "#000000"
        GButton_45["justify"] = "center"
        GButton_45["text"] = "Latest"
        GButton_45.place(x=140,y=60,width=70,height=25)
        GButton_45["command"] = self.GButton_45_command

        GButton_833=tk.Button(root)
        GButton_833["bg"] = "#fcfc70"
        ft = tkFont.Font(family='Times',size=10)
        GButton_833["font"] = ft
        GButton_833["fg"] = "#000000"
        GButton_833["justify"] = "center"
        GButton_833["text"] = "Button"
        GButton_833.place(x=240,y=60,width=70,height=25)
        GButton_833["command"] = self.GButton_833_command

        GLabel_356=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_356["font"] = ft
        GLabel_356["fg"] = "#333333"
        GLabel_356["justify"] = "center"
        GLabel_356["text"] = "You want to post Tweet?"
        GLabel_356.place(x=30,y=280,width=180,height=25)

        GLabel_957=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_957["font"] = ft
        GLabel_957["fg"] = "#1e90ff"
        GLabel_957["justify"] = "center"
        GLabel_957["text"] = "Hint:You should sign up first"
        GLabel_957.place(x=220,y=280,width=190,height=25)

        GLineEdit_331=tk.Entry(root)
        GLineEdit_331["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_331["font"] = ft
        GLineEdit_331["fg"] = "#90ee90"
        GLineEdit_331["justify"] = "center"
        GLineEdit_331["text"] = "write your post..."
        GLineEdit_331.place(x=60,y=330,width=190,height=150)

    def GButton_315_command(self):
        # query=self.GLineEdit_78.get()
        # print(tweet(query))
        # return tweet("hello")
        return 1


    def GButton_37_command(self):
        print("2")


    def GButton_319_command(self):
        print("3")


    def GButton_45_command(self):
        print("4")


    def GButton_833_command(self):
        print("command")

if __name__ == "__main__":

    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
