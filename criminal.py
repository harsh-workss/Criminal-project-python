from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk


class Criminal:
    def __init__(self,main):
        self.main=main
        self.main.geometry('1530x790+0+0')
        self.main.title("CRIMINAL MANAGEMENT SYSTEM")

        lbl_title = Label(self.main,text='CRIMINAL IDENTIFICATION SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=60)

        # NCR logo
        img_logo=Image.open('Images/logo.png')
        img_logo=img_logo.resize((80,60))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.main,image=self.photo_logo)
        self.logo.place(x=150,y=5,width=80,height=50)

        # Image Frame

        img_frame=Frame(self.main,bd=2,relief=RIDGE,bg='White')
        img_frame.place(x=0,y=60,width=1530,height=130)

        # Frame Image

        img2=Image.open('Images/img_2.jpg')
        img2=img2.resize((500,150),Image.FILTERED)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=0,y=0,width=500,height=150)

        # img 3

        img3=Image.open('Images/Img_3.jpg')
        img3=img3.resize((500,160),Image.FILTERED)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=501,y=0,width=500,height=150)

        # img 4

        img4=Image.open('Images/Img_4.jpg')
        img4=img4.resize((530,160),Image.FILTERED)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(img_frame,image=self.photo4)
        self.img_4.place(x=1001,y=0,width=530,height=150)

        # main frame

        Main_frame=Frame(self.main,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)

        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',20,'bold'),bg='white',fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)






        





if __name__ == "__main__":
    main=Tk()
    obj=Criminal(main)
    main.mainloop()

