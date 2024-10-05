from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess 

def clear_placeholder(event):
    if user_entry.get() == "Username":
        user_entry.delete(0, END)
        user_entry.config(fg="black")

def set_placeholder(event):
    if user_entry.get() == "":
        user_entry.insert(0, "Username")
        user_entry.config(fg="grey")

def clear_password_placeholder(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, END)
        password_entry.config(fg="black")
        password_entry.config(show='*')

def set_password_placeholder(event):
    if password_entry.get() == "":
        password_entry.insert(0, "Password")
        password_entry.config(fg="grey")
        password_entry.config(show='')

# user login
def user_login():
    if user_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
        return

    cursor = None  
    try:
        # connection to my sql database
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin4444',
            database='login_data'  
        )
        cursor = con.cursor()
        
       
        query = 'SELECT * FROM data WHERE user=%s AND code=%s'
        cursor.execute(query, (user_entry.get(), password_entry.get()))
        
        row = cursor.fetchone()
        
        if row is None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login Successful!')
            # run the criminal.py 
            subprocess.Popen(['python', 'criminal.py']) 
            root.destroy()  

    except mysql.connector.Error as err:
        messagebox.showerror('Error', f'Connection not established: {err}')
    
    finally:
        if cursor is not None:  # Check if cursor was created before closing
            cursor.close()
        if con.is_connected():
            con.close()

# main window
root = Tk()
root.title("CRIMINAL IDENTIFICATION SYSTEM - LOGIN PAGE")
root.geometry("900x700")
root.resizable(False, False)
root.configure(bg="#fff")

# Adding Image
img = PhotoImage(file="./Images/login.png")
Label(root, image=img, bg="white").place(x=10, y=80)

# Login frame
frame = Frame(root, height=350, width=330, bg='white')
frame.place(x=450, y=70)

# Heading
heading = Label(frame, text='Login', bg='white', fg='#57a1f8', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# User entry
user_entry = Entry(frame, width=25, fg="grey", bg="white", border=0, font=("Microsoft YaHei UI Light", 11))
user_entry.place(x=30, y=80)
user_entry.insert(0, "Username")

Frame(frame, width=295, bg="black", height=2).place(x=25, y=107)

# Password entry
password_entry = Entry(frame, width=25, fg="grey", bg="white", border=0, font=("Microsoft YaHei UI Light", 11))
password_entry.place(x=30, y=150)
password_entry.insert(0, "Password")

Frame(frame, width=295, bg="black", height=2).place(x=25, y=177)

# Login button
login_button = Button(frame, width=40, bg="#57a1f8", fg="white", pady=7,
                      border=0, text="Login", command=user_login)
login_button.place(x=35, y=204)

# bind events for placeholders
user_entry.bind("<FocusIn>", clear_placeholder)
user_entry.bind("<FocusOut>", set_placeholder)
password_entry.bind("<FocusIn>", clear_password_placeholder)
password_entry.bind("<FocusOut>", set_password_placeholder)

root.mainloop()