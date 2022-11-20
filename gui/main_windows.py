from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
)
from gui.Information import Information
from gui.About import About
from gui.Search import Search
from gui.Trends import Trends
from gui.Tweet import Tweet
from gui.sentiment import Sentiment
# import welcome


def mainWindow():
    MainWindow()


class MainWindow(Toplevel):

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.iconbitmap('favicon.ico')

        self.title("Twitter Story - Lets Go")

        self.geometry("1012x506")
        self.configure(bg="#111D29")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#111D29",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)


        button_image_3 = PhotoImage(file=("assets/button_21.png"))
        self.trends_btn = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.trends_btn, "gue"),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
        )
        self.trends_btn.place(x=7.0, y=183.0, width=208.0, height=47.0)

        
        button_image_2 = PhotoImage(file=("assets/button_3.png"))
        self.search_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.search_btn, "sear"),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
        )
        self.search_btn.place(x=7.0, y=233.0, width=208.0, height=47.0)

#########################  tweet  #######################################

        button_image_10 = PhotoImage(file=("assets/button_7.png"))
        self.user_tweet_btn = Button(
            self.canvas,
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.user_tweet_btn, "tweet"),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
        )
        self.user_tweet_btn.place(x=7.0, y=283.0, width=208.0, height=47.0)

#########################  tweet  #######################################



        button_image_1 = PhotoImage(file=("assets/button_4.png"))
        self.user_Info_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.user_Info_btn, "user"),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
        )
        self.user_Info_btn.place(x=7.0, y=133.0, width=208.0, height=47.0)

#########################  sentiment analysis  #######################################

        button_image_13 = PhotoImage(file=("assets/Asset_1.png"))
        self.sen_btn = Button(
            self.canvas,
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.sen_btn, "Sentiment"),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
        )
        self.sen_btn.place(x=7.0, y=333.0, width=208.0, height=47.0)

#########################  sentiment analysis  #######################################


        button_image_4 = PhotoImage(file=("assets/button_6.png"))
        self.about_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.about_btn, "abt"),
            cursor='hand2', activebackground="#111D29",
            relief="flat",
        )
        self.about_btn.place(x=7.0, y=383.0, width=208.0, height=47.0)

        button_image_5 = PhotoImage(file=("assets/button_23.png"))
        self.exit_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit,
            relief="flat",
        )
        self.exit_btn.place(x=0.0, y=441.0, width=215.0, height=47.0)


        self.heading = self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="Hello",
            fill="#111D29",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            28.0,
            21.0,
            anchor="nw",
            text="Twitter Story",
            fill="#FFFFFF",
            font=("Montserrat Bold", 24 * -1),
        )

        

        # Loop through windows and place them
        self.windows = {
            "sear": Search(self),
            "gue": Trends(self),
            "abt": About(self),
            "user": Information(self),
            "tweet": Tweet(self),
            "Sentiment": Sentiment(self)
            
        }

        self.handle_btn_press(self.user_Info_btn, "user")
        self.sidebar_indicator.place(x=0, y=133)

        self.current_window.place(x=215, y=72, width=1013.0, height=506.0)

        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()

    def place_sidebar_indicator(self):
        pass

    def exit(self):
        confirm = messagebox.askyesno(
            "Confirm exit", "Do you really want to exit?"
        )
        if confirm == True:
            self.destroy()

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

    # def handle_search_refresh(self):
    #     # Recreate the user window
    #     self.windows["sear"] = Search(self)