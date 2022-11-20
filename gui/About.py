from tkinter import ttk
from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox


def about():
    About()


class About(Frame):
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

#################### Farah #############################

        self.image_image_1 = PhotoImage(file=("assets/image_3.png"))
        image_1 = self.canvas.create_image(203.0, 100.0, image=self.image_image_1)
    
     
        self.canvas.create_text(
            56.0,
            50.0,
            anchor="nw",
            text="Farah ",
            fill="#1D9BF0",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            56.0,
            82.0,
            anchor="nw",
            text="Eilouti",
            fill="#1D9BF0",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            56.0,
            120.0,
            anchor="nw",
            text="Artificial Intelligence",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )


        self.canvas.create_rectangle(
            56.0, 112.0, 169.0, 114.0, fill="#FFFFFF", outline=""
        )

        self.image_image_Farah = PhotoImage(file=("assets/Farah.png"))
        image_profile_1 = self.canvas.create_image(310.0, 100.0, image=self.image_image_Farah)


#################### Mohammad #############################

        self.image_image_2 = PhotoImage(file=("assets/image_3.png"))
        image_2 = self.canvas.create_image(565.0, 100.0, image=self.image_image_2)
    
     
        self.canvas.create_text(
            418.0,
            50.0,
            anchor="nw",
            text="Mohammad",
            fill="#1D9BF0",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            418.0,
            82.0,
            anchor="nw",
            text="AlGhzawi",
            fill="#1D9BF0",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            418.0,
            120.0,
            anchor="nw",
            text="Artificial Intelligence",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )


        self.canvas.create_rectangle(
            418.0, 112.0, 531.0, 114.0, fill="#FFFFFF", outline=""
        )

        self.image_image_Mohd = PhotoImage(file=("assets/Mohd.png"))
        image_profile_2 = self.canvas.create_image(670.0, 100.0, image=self.image_image_Mohd)


#################### Amani  #############################

        self.image_image_3 = PhotoImage(file=("assets/image_3.png"))
        image_3 = self.canvas.create_image(203.0, 230.0, image=self.image_image_3)
    
    
        self.canvas.create_text(
            56.0,
            180.0,
            anchor="nw",
            text="Amani ",
            fill="#1D9BF0",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            56.0,
            212.0,
            anchor="nw",
            text="AlZoubi",
            fill="#1D9BF0",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            56.0,
            250.0,
            anchor="nw",
            text="Software Developer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )


        self.canvas.create_rectangle(
            56.0, 242.0, 169.0, 244.0, fill="#FFFFFF", outline=""
        )

        self.image_image_Amani = PhotoImage(file=("assets/Amani.png"))
        image_profile_3 = self.canvas.create_image(310.0, 230.0, image=self.image_image_Amani)

#################### Omar  #############################

        self.image_image_4 = PhotoImage(file=("assets/image_3.png"))
        image_4 = self.canvas.create_image(565.0, 230.0, image=self.image_image_4)
    
     
        self.canvas.create_text(
            418.0,
            180.0,
            anchor="nw",
            text="Omar",
            fill="#1D9BF0",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            418.0,
            212.0,
            anchor="nw",
            text="Ali",
            fill="#1D9BF0",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            418.0,
            250.0,
            anchor="nw",
            text="Artificial Intelligence",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )


        self.canvas.create_rectangle(
            418.0, 242.0, 531.0, 244.0, fill="#FFFFFF", outline=""
        )

        self.image_image_Omar = PhotoImage(file=("assets/Omar.png"))
        image_profile_4 = self.canvas.create_image(670.0, 230.0, image=self.image_image_Omar)

#################### Ashar  #############################

        self.image_image_5 = PhotoImage(file=("assets/image_3.png"))
        image_5 = self.canvas.create_image(203.0, 360.0, image=self.image_image_5)
    
    
        self.canvas.create_text(
            56.0,
            310.0,
            anchor="nw",
            text="Ashar",
            fill="#1D9BF0",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            56.0,
            342.0,
            anchor="nw",
            text="AlMomani",
            fill="#1D9BF0",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            56.0,
            380.0,
            anchor="nw",
            text="Software Developer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )


        self.canvas.create_rectangle(
            56.0, 372.0, 169.0, 374.0, fill="#FFFFFF", outline=""
        )

        self.image_image_Ashar = PhotoImage(file=("assets/Ashar.png"))
        image_profile_5 = self.canvas.create_image(310.0, 360.0, image=self.image_image_Ashar)

#################### Ismail  #############################
        self.image_image_6 = PhotoImage(file=("assets/image_3.png"))
        image_6 = self.canvas.create_image(565.0, 360.0, image=self.image_image_6)
    
     
        self.canvas.create_text(
            418.0,
            310.0,
            anchor="nw",
            text="Ismail",
            fill="#1D9BF0",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            418.0,
            342.0,
            anchor="nw",
            text="AlAmir",
            fill="#1D9BF0",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            418.0,
            380.0,
            anchor="nw",
            text="Software Developer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )


        self.canvas.create_rectangle(
            418.0, 372.0, 531.0, 374.0, fill="#FFFFFF", outline=""
        )

        self.image_image_Ismail = PhotoImage(file=("assets/Ismail.png"))
        image_profile_6 = self.canvas.create_image(670.0, 360.0, image=self.image_image_Ismail)
