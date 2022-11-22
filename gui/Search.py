from tkinter import *
from features.tweets import *
from features.userName_tweets import user_tweets
from features.user_Hashtag import search_by_UserAndHashtag
from tkinter import ttk




def search():
    Search()


class Search(Frame):
    
    def result_Hashtag(self,hashtag):
        self.canvas.delete('del')
        txt=tweet(hashtag)
        text = Text(self, height=18,width=50,font=("Montserrat 10 Bold", 18 * -1))
        text.place(x=256, y=20)
        text.insert("1.0", txt)
        text_scroll = ttk.Scrollbar(self, orient="vertical", command=text)
        text_scroll.place(x=750, y=12, sticky="ns")
        text["yscrollcommand"] = text_scroll.set
        
    def result_User(self,user):
        self.canvas.delete('del')
        data=user_tweets(user)['Tweets']
        #print(data)
        All_tweets=''
    
        for i in range(10):
            All_tweets+=f'tweet {i+1} : {data[i]} \n\n '


        text = Text(self, height=18,width=50,font=("Montserrat 10 Bold", 18 * -1))
        text.place(x=256, y=20)
        text.insert("1.0", All_tweets)
        text_scroll = ttk.Scrollbar(self, orient="vertical", command=text)
        text_scroll.place(x=750, y=12, sticky="ns")
        text["yscrollcommand"] = text_scroll.set

    def result_User_Hash(self,user,Hash):
            self.canvas.delete('del')
            data= search_by_UserAndHashtag(user, Hash)
            
            text = Text(self , height=18,width=50,font=("Montserrat 10 Bold", 18 * -1))
            text.place(x=256, y=20)
            text.insert("1.0", data)
            text_scroll = ttk.Scrollbar(self, orient="vertical", command=text)
            text_scroll.place(x=750, y=12, sticky="ns")
            text["yscrollcommand"] = text_scroll.set
            self.entry_Username.delete()
            self.entry_Hash.delete()

        
        


    def search_Bar(self,e):
        
        if e=="#          hashtag         ":
            self.canvas.delete('my_tag')
            self.entry_image_2 = PhotoImage(file="assets/Asset_3.png")
            entry_bg_1 = self.canvas.create_image(140.0, 170.0, image=self.entry_image_2)
            entry_Hashtag= Entry(
                self,
                bd=0,
                bg="#EFEFEF",
                highlightthickness=0,
                font=("Montserrat Bold", 18 * -1),
                foreground="#777777",
            )
            entry_Hashtag.insert(-1, 'Hashtag')
            entry_Hashtag.place(x=60.0, y=155.0 ,width=185.0, height=30.0)

            self.button_search_3 = PhotoImage(file=("assets/Asset_7.png"))
            self.search_Hashtag_btn = Button(
                self.canvas,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.result_Hashtag(entry_Hashtag.get()),
                image=self.button_search_3,
                cursor='hand2', 
                relief="flat",
        )
            self.search_Hashtag_btn.place(x=35.0, y=300, width=208.0, height=47.0)
            self.entry_Hash.destroy()


        if e=="👤          user         ":
            self.canvas.delete('my_tag')
            self.entry_image_2 = PhotoImage(file="assets/Asset_3.png")
            entry_bg_1 = self.canvas.create_image(140.0, 170.0, image=self.entry_image_2)
            entry_User= Entry(
                self,
                bd=0,
                bg="#EFEFEF",
                highlightthickness=0,
                font=("Montserrat Bold", 18 * -1),
                foreground="#777777",
            )
            entry_User.insert(-1, 'username')
            entry_User.place(x=60.0, y=155.0, width=185.0, height=30.0)

            self.button_search_2 = PhotoImage(file=("assets/Asset_7.png"))
            self.search_User_btn = Button(
                self.canvas,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.result_User(entry_User.get()),
                cursor='hand2', 
                image=self.button_search_2,
                relief="flat",
        )
            self.search_User_btn.place(x=35.0, y=300, width=208.0, height=47.0)
            self.entry_Hash.destroy()
        

        if e=="#👤      user & keywords      #":

            self.entry_image_2 = PhotoImage(file="assets/Asset_3.png")
            entry_bg_1 = self.canvas.create_image(140.0, 170.0, image=self.entry_image_2)
            entry_Username= Entry(
                self,
                bd=0,
                bg="#EFEFEF",
                highlightthickness=0,
                font=("Montserrat Bold", 18 * -1),
                foreground="#777777",
            )
            entry_Username.insert(-1, 'username')
            entry_Username.place(x=60.0, y=155.0, width=185.0, height=30.0)


            self.entry_image_5 = PhotoImage(file="assets/Asset_3.png")
            self.entry_bg_5 = self.canvas.create_image(140.0, 248.0, image=self.entry_image_5,tags='my_tag')
            

            self.entry_Hash= Entry(
                self,
                bd=0,
                bg="#EFEFEF",
                highlightthickness=0,
                font=("Montserrat Bold", 18 * -1),
                foreground="#777777",
            )
            self.entry_Hash.insert(-1, 'Hashtag')
            self.entry_Hash.place(x=60.0, y=233.0, width=185.0, height=30.0)

            self.button_search_3 = PhotoImage(file=("assets/Asset_7.png"))
            self.search_User_Hashtag_btn = Button(
            self.canvas,
            image=self.button_search_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.result_User_Hash(entry_Username.get(),self.entry_Hash.get()),
            cursor='hand2', 
            relief="flat",
        )
            self.search_User_Hashtag_btn.place(x=35.0, y=300.0, width=208.0, height=47.0)

                

    def handle_btn_press(self,feature,  name):
        if feature=='S_hashtag':
            self.y==tweet(name)["Tweets"][0]
        
      

    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.x=''
        self.y='Tweet Result'
        self.data = {"usr": "", "user & keywords": "", "keywords": ""}


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
        
        
        # self.canvas.create_rectangle(
        #     280.0, 12.0, 282.0, 500.0, fill="#777777", outline=""
        # )


        variable = StringVar(self.parent)
        # variable.config(bg='#555555')
        variable.set("Search")
        option_menu = OptionMenu(parent, variable,"👤          user         ",
                                "#          hashtag         ", "#👤      user & keywords      #",
                                command=self.search_Bar)

        option_menu.place(x=259.0, y=149.0,width=190.0, height=40.0),
        option_menu.configure(bg="#1D9BF0",
            bd=0,
            highlightthickness=0,
            relief="ridge",
            font=("Montserrat Bold", 14 * -1),
            activebackground="#1D9BF0",
            fg="#FFF")

