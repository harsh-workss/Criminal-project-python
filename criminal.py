from tkinter import*
from tkinter  import ttk
from PIL import Image,ImageTk


class Criminal:
    def __init__(self,main):
        self.main=main
        self.main.geometry('1530x790+0+0')
        self.main.title("CRIMINAL MANAGEMENT SYSTEM")

        lbl_title = Label(self.main,text='CRIMINAL  MANAGEMENT  SYSTEM  SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='silver')
        lbl_title.place(x=0,y=0,width=1530,height=60)






if __name__ == "__main__":
    main=Tk()
    obj=Criminal(main)
    main.mainloop()

