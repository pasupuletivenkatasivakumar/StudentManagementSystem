from tkinter import *
from tkinter import messagebox

def login():
    if usernameEntry.get() ==''or passwordEntry.get()=='':
        messagebox.showerror('Error','Filds cannot be empty')
    elif usernameEntry.get()=='12005605' and passwordEntry.get()=='Siva2003@':
        messagebox.showinfo('Success',"wellcome")
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Invalid Credentials')

  #only for jpg image
# create object window to the tk class
# this class "tk" help you use the grafical user interface in python
window = Tk()

# geomety widh and hight of the gui window
# size of the window 1280x700 and for to fix the window at same position 0+0
window.geometry('1280x700+120+50')
window.title('Login SMS')
window.resizable(False,False) # it disable the maximize button
#-------------------------------------------------------------------------------
# for inseting image we have to import pillow and download that  in terminal

backgroundImage = PhotoImage(file="bg.png")
bgLabel = Label(window,image=backgroundImage)
bgLabel.place(x=1.0,y=0.0)


# use one method mainloop insie tk class9
# mainloop do keep window on loop we can see continuesly

smsLogo = Frame(window)
smsLogo.place(x=380,y=100)

smsLabel = Label(smsLogo,text= "Lovely Professional University",compound=LEFT
                      ,font=('Calabri',20,'bold'))
smsLabel.grid(row=0,column=0,pady=10,padx=60)
#------------------------------------------------------------------------------
loginFrame = Frame(window)
loginFrame.place(x =450,y = 200)

logoImage =PhotoImage(file='graduate1.png')
logolabel =Label(loginFrame,image=logoImage)
logolabel.grid(row=0,column=0,columnspan=2,pady=10,padx=10)




#---------------------------USERNAME ---------------------------------
usernameImage = PhotoImage(file='profile.png')
usernameLabel = Label(loginFrame,image=usernameImage,text= "Username :",compound=LEFT
                      ,font=('Calabri',14,'bold'))
usernameLabel.grid(row=1,column=0,pady=10,padx=20)


usernameEntry =Entry(loginFrame,font=('Calabri',11),bd=3)
usernameEntry.grid(row=1,column =1,pady=10,padx=20)

#---------------------PASWORD LABEL --------------------------------
passwordImage = PhotoImage(file='reset-password.png')
passwordLabel = Label(loginFrame,image=passwordImage,text= "Password :",compound=LEFT
                      ,font=('Calabri',14,'bold'))
passwordLabel.grid(row=2,column=0,pady=10,padx=20)


passwordEntry =Entry(loginFrame,font=('Calabri',11),bd=3)
passwordEntry.grid(row=2,column =1,pady=10,padx=20)


#-----------------------------Login button ---------------------
loginButton = Button(loginFrame,text="Login",font=('Calabri',11,'bold'),width =15
                     ,fg='white',bg ='cornflowerblue',activebackground='lightgreen',
                     activeforeground='cornflowerblue',cursor ='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()
