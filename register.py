from tkinter import *
from tkinter import messagebox as msg
import sys
import tkinter
from tkinter_custom_button import TkinterCustomButton
from pyrebase_init import register_auth

def register(main):
    global register_screen
    register_screen = Toplevel(main)
    register_screen.title("Register")
    register_screen.configure(bg='snow3')
    screen_size = str(main.winfo_screenwidth())+'x'+str(main.winfo_screenheight())
    register_screen.geometry(screen_size)

    global username
    global password
    global email
    global contact
    global fathername
    global dob

    username = StringVar()
    password = StringVar()
    dob = StringVar()
    email = StringVar()
    contact = StringVar()
    fathername = StringVar()
 
    Label(register_screen,text="REGISTER YOURSELF", bg="lime green", width="300", height="2", font=("Calibri", 13)).pack()
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
    dateofbirth_lable = Label(register_screen,bg='snow3',font=(16), text="Date of Birth (YYYY-MM-DD) * ")
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
    Label(register_screen,bg='snow3', text="").pack()
    button = TkinterCustomButton(master=register_screen,text="Register",height=60,width=150 ,corner_radius=10, command=test_reg,fg_color="green yellow",text_color='black',hover_color="lime green")
    button.pack()
    return register_screen

def test_reg():
    user = register_auth(email.get(),password.get(),username.get(),contact.get(),dob.get(),fathername.get())
    # print(user)
    register_screen.destroy()
    msg.showinfo(user['name'],'REGISTERED SUCCESFULLY')

sys.modules[__name__] = register