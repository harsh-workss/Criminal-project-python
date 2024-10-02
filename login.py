from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("CRIMINAL IDENTIFICATION SYSTEM - LOGIN PAGE")
root.geometry("800x600")
root.resizable(False,False)
root.configure(bg="#fff")

# Adding Image
img = PhotoImage(file = "./Images/login.png")
Label(root,image=img,bg="white").place(x=10,y=80)

#login frame
frame = Frame(root,height=350,width=330,bg='white')
frame.place(x=450,y=70)

#heading
heading = Label(frame,text='Login',bg='white',fg='#57a1f8',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

# user entry
user = Entry(frame,width=25,fg="black",bg="white",border=0,font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")

Frame(frame,width=295,bg="black",height=2).place(x=25,y=107)

# Password entry
code = Entry(frame,width=25,fg="black",bg="white",border=0,font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,"Password")

Frame(frame,width=295,bg="black",height=2).place(x=25,y=177)

# Button frame
Button(frame,width=40,bg="#57a1f8",fg="white",pady=7,border=0,text="Login").place(x=35,y=204)

#############

def clear_placeholder(event):
    if user.get() == "Username":
        user.delete(0, END)  # Clear the entry
        user.config(fg="black")  # Change text color to black

def set_placeholder(event):
    if user.get() == "":
        user.insert(0, "Username")  
        user.config(fg="grey")  

############

def clear_holder(event):
    if code.get() == "Password":
        code.delete(0,END)
        code.config(fg="black")

def set_holder(event):
    if code.get() == "":
        code.insert(0,"Password")
        code.config(fg="grey")

        
# Bind events
user.bind("<FocusIn>", clear_placeholder)  
user.bind("<FocusOut>", set_placeholder)  

#  Bind for code
code.bind("<FocusIn>", clear_holder) 
code.bind("<FocusOut>", set_holder)  




root.mainloop()
