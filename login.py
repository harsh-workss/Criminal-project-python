from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("LOGIN PAGE")
root.geometry("800x600")
root.resizable(False,False)
root.configure(bg="#fff")

img = PhotoImage(file="./Images/login.png")
Label(root,image=img,bg="white").place(x=10,y=80)

frame = Frame(root,height=350,width=330,bg='white')
frame.place(x=450,y=70)

heading = Label(frame,text='Login',bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)




root.mainloop()
