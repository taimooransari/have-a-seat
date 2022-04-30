from tkinter import *
from tkinter import messagebox as msg
import sys
import tkinter
from tkinter_custom_button import TkinterCustomButton
from pyrebase_init import register_auth


# MAIN REGISTER USER SCREEN WITH ENTRY FORM
def register(main):
    global register_screen
    register_screen = Toplevel(main)
    register_screen.title("Register")
    register_screen.configure(bg='snow3')
    screen_size = str(main.winfo_screenwidth())+'x'+str(main.winfo_screenheight())
    register_screen.geometry(screen_size)

    global username
    global password
    global password2
    global email
    global contact
    global fathername
    global dob

    username = StringVar()
    password = StringVar()
    password2 = StringVar()
    dob = StringVar()
    email = StringVar()
    contact = StringVar()
    fathername = StringVar()
 
    Label(register_screen,text="REGISTER YOURSELF", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(register_screen,bg='snow3', text="").pack()
    username_lable = Label(register_screen,bg='snow3',font=(16), text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=username)
    username_entry.pack()
    contactnumber_lable = Label(register_screen,bg='snow3',font=(16), text="Contact number * ")
    contactnumber_lable.pack()
    contactnumber_entry =  Entry(register_screen,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=contact)
    contactnumber_entry.pack()
    fathername_lable = Label(register_screen,bg='snow3',font=(16), text="Father Name * ")
    fathername_lable.pack()
    fathername_entry =  Entry(register_screen,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=fathername)
    fathername_entry.pack()
    dateofbirth_lable = Label(register_screen,bg='snow3',font=(16), text="Date of Birth (DD-MM-YYYY) * ")
    dateofbirth_lable.pack()
    dateofbirth_entry =  Entry(register_screen,width="35", borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=dob)
    dateofbirth_entry.pack()
    emailid_lable = Label(register_screen,font=(16),bg='snow3', text="Email * ")
    emailid_lable.pack()
    emailid_entry =  Entry(register_screen,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=email)
    emailid_entry.pack()
    password_lable = Label(register_screen,bg='snow3',font=(16), text="Password * ")
    password_lable.pack()
    password_entry =  Entry(register_screen,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=password,show="*")
    password_entry.pack()
    password_lable2 = Label(register_screen,bg='snow3',font=(16), text="Confirm Password * ")
    password_lable2.pack()
    password_entry2 =  Entry(register_screen,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=password2,show="*")
    password_entry2.pack()
    Label(register_screen,bg='snow3', text="").pack()
    button = TkinterCustomButton(master=register_screen,text="Register",height=60,width=150 ,corner_radius=10, command=test_reg,fg_color="DodgerBlue2",text_color='black')
    button.pack()
    return register_screen


# REGISTER HELPER FUNCTION TO CHECK VALIDATIONS AND THEN CALL REGISTER AUTH FUNCTION FROM FIREBASE
def test_reg():
    try:
        if(password.get()==password2.get() and len(password2.get())>=6):
            e=False
            user = register_auth(email.get(),password.get(),username.get(),contact.get(),dob.get(),fathername.get())
        else:
            e = True
            raise Exception('PASSWORD NOT SAME OR PASSWORD WEAK. RE-ENTER!')
    except:
        if(e):
            msg.showerror('REGISTER FAILED',"PASSWORD NOT SAME OR PASSWORD WEAK. RE-ENTER!")  
        else:  
            msg.showerror('REGISTER FAILED',"Check your credentials")
    else:
        register_screen.destroy()
        msg.showinfo(user['name'],'REGISTERED SUCCESFULLY')

sys.modules[__name__] = register