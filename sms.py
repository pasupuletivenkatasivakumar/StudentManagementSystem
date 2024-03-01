import tkinter.ttk
from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas


#exit
def exitt():
    result=messagebox.askyesno('confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


#export_data

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content= studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is Exported Successfully')

# code formating

def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen
    screen = Toplevel()
    screen.title('Update Student')
    screen.grab_set()
    screen.resizable(0, 0)
    idLabel = Label(screen, text="Id :", font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text="Name :", font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text="Phone :", font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text="Email :", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text="Address :", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text="Gender :", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text="DOB :", font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('calabri', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=7, columnspan=2, pady=15)


    if title=='Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])


# update functionality


def update_data():
    query ='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Updated',f'Id {idEntry.get()} Student date is Successfully updatded',
                        parent=screen)
    screen.destroy()
    show_student()






#show button fucntionality
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)




# delete button funcitonality
def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)





# functionallity of search student


def search_data():
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data= mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)










def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()==''or dobEntry.get()=='':
        messagebox.showerror('Error','All feilds are required',parent=screen)

    else:
        date = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%H:%M:%S')
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),
                                    genderEntry.get(),dobEntry.get(),date,currenttime))

            con.commit()
            result=messagebox.askyesno('Confirm','Confirm to Data added',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return

        query='select *from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            datalist=list(data)
            studentTable.insert('',END,values=datalist)
        print(fetched_data)





#------------------connect database-------------------------------
def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()

        except:
            messagebox.showerror("Error","Invalid Details",parent=connectWindow)
            return

        try:
            query = "create database StudentManagementSystem"
            mycursor.execute(query)
            query = 'use StudentManagementSystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key, name varchar(30),mobile varchar(10),email varchar(30),' \
                   'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query = 'use StudentManagementSystem'
            mycursor.execute(query)

        messagebox.showinfo("Sucess", "Database Connection is Successfull", parent=connectWindow)
        #destroy after use of the connectWindow
        connectWindow.destroy()
        # enabling the buttons
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)

    # we are creating connectwindow as an object of Toplevel() class
    connectWindow=Toplevel()
    connectWindow.grab_set()
    # 470x250 is the size of the window and 730 from y axis and 230 from x axis
    connectWindow.geometry('470x250+430+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)


    backgroundImage1 = PhotoImage(file="bgsmall.png")
    bgLabel1 = Label(connectWindow, image=backgroundImage1)
    bgLabel1.place(x=1.0, y=0.0)


    hostnameLabel=Label(connectWindow,text="Host Name :",font=('Calibri',20,'bold'))
    hostnameLabel.grid(row=0,column=0)
    hostEntry = Entry(connectWindow,font=('Calibri',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=35,pady=20)

    usernameLabel = Label(connectWindow, text="User Name :", font=('Calibri', 20, 'bold'))
    usernameLabel.grid(row=1, column=0,padx=20)
    usernameEntry = Entry(connectWindow, font=('Calibri',15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=35, pady=20)

    passwordLabel = Label(connectWindow, text="Password :", font=('Calibri', 20, 'bold'))
    passwordLabel.grid(row=2, column=0,padx=20)
    passwordEntry = Entry(connectWindow, font=('Calibri',15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=35, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',width=20,command=connect)
    connectButton.grid(row=3,columnspan=2)

#------------------slider FUCTIONS-------------------------------

count =0
text=''
def slider():
    global text,count
    if count == len(s):
        pass
    else:
        text=text+s[count]
        sliderLabel.config(text=text)
        count+=1
        sliderLabel.after(20,slider)



#--------------------------clock---------------------
def clock():
    global date,currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)
#------------------------ROOT-------------------------
#GUI Port
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x680+50+20')
root.title('Student Management System')
root.resizable(0,0)



backgroundImage = PhotoImage(file="bg.png")
bgLabel = Label(root,image=backgroundImage)
bgLabel.place(x=1.0,y=0.0)

#-----------------------DATE -------------------------
datetimeLabel=Label(root,font=('Calabri',11))
datetimeLabel.place(x=1040,y=637)
clock()
#---------------------------SMS---------------------------
s= "STUDENT MANAGEMENT SYSTEM"
sliderLabel = Label(root,font=('Calabri',18,"bold"))
sliderLabel.place(x=350,y=10)
slider()
#--------------------------------button----------------

dataBaseImage = PhotoImage(file='server.png')
connectButton = Button(root,image=dataBaseImage,text= ">>Database",compound=LEFT,font=('Calabri',14,'bold'),
                       fg='white', bg='cornflowerblue', activebackground='lightgreen',
                       activeforeground='cornflowerblue', cursor='hand2',command=connect_database)
connectButton.place(x=880,y=637)

#----------------------------Left frame----------------------------------------------
leftFrame=Frame(root)
leftFrame.place(x=50,y=60,width=1100,height=120)


logo_image=PhotoImage(file='graduate1.png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0, column=0,padx=10,pady=10)


addstudentButton=ttk.Button(leftFrame,text="Add Student",width=10,state=DISABLED,command=lambda :toplevel_data('Add Student','ADD',add_data))
addstudentButton.grid(row=0,column=1,padx=10,pady=10)

searchstudentButton=ttk.Button(leftFrame,text="Search",width=10,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=0,column=2,padx=10,pady=10)

deletestudentButton=ttk.Button(leftFrame,text="Delete",width=10,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=0,column=3,padx=10,pady=10)

updatestudentButton=ttk.Button(leftFrame,text="Update",width=10,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=0,column=4,padx=10,pady=10)

showstudentButton=ttk.Button(leftFrame,text="Show",width=10,state=DISABLED,command=show_student)
showstudentButton.grid(row=0,column=5,padx=10,pady=10)

exportButton=ttk.Button(leftFrame,text="Export",width=10,state=DISABLED,command=export_data)
exportButton.grid(row=0,column=6,padx=10,pady=10)

exitButton=ttk.Button(leftFrame,text="Exit",width=10,command=exitt)
exitButton.grid(row=0,column=7,padx=10,pady=10)



#-------------------------------rightframe-------------------------------------
#-------------------------------Tree view-------------------------------

rightFrame = Frame(root)
rightFrame.place(x=50,y=200,width=1100,height=430)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender',
                                'DOB','Added Date','Added Time'),
                            xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
#creating table in the right frame
studentTable.pack(fill=BOTH,expand =1)

studentTable.heading('Id',text="Id")
studentTable.heading('Name',text="Name")
studentTable.heading('Mobile',text="Mobile No")
studentTable.heading('Email',text="Email Address")
studentTable.heading('Address',text="Address")
studentTable.heading('Gender',text="Gender")
studentTable.heading('DOB',text="DOB")
studentTable.heading('Added Date',text="Added Date")
studentTable.heading('Added Time',text="Added Time")



studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=150,anchor=CENTER)
studentTable.column('Mobile',width=120,anchor=CENTER)
studentTable.column('Email',width=250,anchor=CENTER)
studentTable.column('Address',width=150,anchor=CENTER)
studentTable.column('Gender',width=80,anchor=CENTER)
studentTable.column('DOB',width=100,anchor=CENTER)
studentTable.column('Added Date',width=100,anchor=CENTER)
studentTable.column('Added Time',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',10,'bold'),foreground='white',background='skyblue')
style.configure('Treeview.Heading',font=('arial',8,'bold'),foreground="black")

studentTable.config(show='headings')



root.mainloop()
