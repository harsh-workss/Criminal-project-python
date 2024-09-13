from tkinter import*
from tkinter import ttk
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

        # upper frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',20,'bold'),bg='white',fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels Entry

        # Case id
        Caseid=Label(upper_frame,text='Case ID:',font=('arial',12,'bold'),bg='white')
        Caseid.grid(row=0,column=0,padx=2,sticky=W)

        Caseentry=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        Caseentry.grid(row=0,column=1,padx=2,sticky=W)

        # Criminal Number
        lbl_Criminal_no=Label(upper_frame,font=('arial',12,'bold'),text='Criminal No:',bg='white')
        lbl_Criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_Criminal_no=ttk.Entry(upper_frame,width=24,font=('arial',11,'bold'))
        txt_Criminal_no.grid(row=0,column=3,padx=2,pady=7)  

        # Criminal Name
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text='Criminal Name:',bg='white') 
        lbl_Name.grid(row=1,column=0,sticky=W,padx=5,pady=7)

        txt_Name=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)  

        # Nickname
        lbl_nickname=Label(upper_frame,font=('arial',12,'bold'),text='Nick name:',bg='white') 
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nickname=ttk.Entry(upper_frame,width=22,font=('arial',12,'bold'))
        txt_nickname.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        # Arrest date
        lbl_arrestDate=Label(upper_frame,font=('arial',12,'bold'),text='Arrest Date:',bg='white')
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,width=20,font=('arial',12,'bold'))
        txt_arrestDate.grid(row=2,column=1,sticky=W,padx=2,pady=7)  
        
        # Date of Crime
        lbl_Dateofarrest=Label(upper_frame,font=('arial',12,'bold'),text='Date of Crime:',bg='white')
        lbl_Dateofarrest.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_Dateofarrest=ttk.Entry(upper_frame,width=22,font=('arial',12,'bold'))
        txt_Dateofarrest.grid(row=2,column=3,sticky=W,padx=2,pady=7)  

        # Address
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text='Address:',bg='white')
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,font=('arial',12,'bold'))
        txt_address.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        # Age
        lbl_age=Label(upper_frame,font=('arial',12,'bold'),text='Age:',bg='white')
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(upper_frame,font=('arial',12,'bold'),width=22)
        txt_age.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #occupation
        lbl_occupation=Label(upper_frame,font=('arial',12,'bold'),text='Occupation:',bg='white')
        lbl_occupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_occupation=ttk.Entry(upper_frame,width=20,font=('arial',12,'bold'))
        txt_occupation.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        # Crime type
        lbl_crimetype=Label(upper_frame,font=('arial',12,'bold'),text='Crime Type:',bg='white')
        lbl_crimetype.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_crimetype=ttk.Entry(upper_frame,width=22,font=('arial',12,'bold'))
        txt_crimetype.grid(row=4,column=3,sticky=W,padx=2,pady=7)

        # Father name
        lbl_fathername=Label(upper_frame,font=('arial',12,'bold'),text='Father Name:',bg='white')
        lbl_fathername.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        txt_fathername=ttk.Entry(upper_frame,width=22,font=('arial',12,'bold'))
        txt_fathername.grid(row=0,column=6,sticky=W,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame,font=('arial',12,'bold'),text='Gender:',bg='white')
        lbl_gender.grid(row=1,column=5,sticky=W,padx=2,pady=7)

              
        
        # Most Wanted
        lbl_mostwanted=Label(upper_frame,font=('arial',12,'bold'),text='Most Wanted:',bg='white')
        lbl_mostwanted.grid(row=2,column=5,sticky=W,padx=2,pady=7)

        # Radio Button Gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=765,y=45,width=190,height=35)

        male=Radiobutton(radio_frame_gender,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,sticky=W,padx=2,pady=5)

        female=Radiobutton(radio_frame_gender,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,sticky=W,padx=2,pady=5)


        # Radio Button MostWanted
        radio_frame_mostwanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_mostwanted.place(x=765,y=85,width=190,height=35)

        yes=Radiobutton(radio_frame_mostwanted,text='YES',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        no=Radiobutton(radio_frame_mostwanted,text='NO',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,padx=2,pady=5,sticky=W)


        # Button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=190,width=630,height=45)

        # Add button
        button_add=Button(button_frame,text='Record Save',font=('arial',13,'bold'),bg='blue',fg='white',width=14)
        button_add.grid(row=0,column=0,padx=3,pady=5)

        #update button
        button_update=Button(button_frame,text='Update',font=('arial',13,'bold'),bg='blue',fg='white',width=14)
        button_update.grid(row=0,column=1,padx=3,pady=5)

        #delete button
        button_delete=Button(button_frame,text='Delete',font=('arial',13,'bold'),bg='blue',fg='white',width=14)
        button_delete.grid(row=0,column=2,padx=3,pady=5)

        #clear Buttom
        button_clear=Button(button_frame,text='Clear',font=('arial',13,'bold'),bg='blue',fg='white',width=14)
        button_clear.grid(row=0,column=3,padx=3,pady=5)

        # Background right side image
        img_crime=Image.open('Images/thief.jpg')
        img_crime=img_crime.resize((470,245),Image.FILTERED)
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=1000,y=0,width=470,height=245)


        # down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information table',font=('times new roman',18,'bold'),bg='white',fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        # search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal record',font=('tiems of roman',15,'bold'),bg='white',fg='red')
        search_frame.place(x=0,y=0,width=1470,height=60)

        # search by frame
        lbl_search_by=Label(search_frame,font=('arial',11,'bold'),text='Search by:',bg='red',fg='white')
        lbl_search_by.grid(row=0,column=0,sticky=W,padx=5)

        # combo search box
        combo_search_box=ttk.Combobox(search_frame,font=('arial',11,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # entry feild
        search_txt=ttk.Entry(search_frame,width=18,font=('arial',12,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search button
        button_search=Button(search_frame,text='Search',font=('arial',13,'bold'),bg='blue',fg='white',width=14)
        button_search.grid(row=0,column=3,sticky=W,padx=5)

        # search all Buttom
        button_all=Button(search_frame,text='Show all',font=('arial',13,'bold'),bg='blue',fg='white',width=14)
        button_all.grid(row=0,column=4,sticky=W,padx=5)


        # Table frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview) 

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='Crime No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Date of Crime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Crime Type')
        self.criminal_table.heading('11',text='Father Name')
        self.criminal_table.heading('12',text='Gender')
        self.criminal_table.heading('13',text='Wanted')
        
        
        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)


        self.criminal_table.pack(fill=BOTH,expand=1)
 



if __name__ == "__main__":
    main=Tk()
    obj=Criminal(main)
    main.mainloop()

