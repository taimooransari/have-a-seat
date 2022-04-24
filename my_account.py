from tkinter import *
import tkinter
from tkinter.font import BOLD
from tkinter_custom_button import TkinterCustomButton
my_screen=None

def my_account_screen(screen,user):
    global my_screen


    my_screen = Toplevel(screen)
    screen_size = str(my_screen.winfo_screenwidth())+'x'+str(my_screen.winfo_screenheight())
    my_screen.geometry(screen_size)
    my_screen.title("MY ACCOUNT")
    my_screen.configure(bg="snow3")
    Label(my_screen,text="Account Information Below", bg="DodgerBlue2", width="300", height="2", font=("Calibri", 13)).pack()
    Label(my_screen,text="",bg="snow3",pady=50).pack()
    my_box=Frame(my_screen,borderwidth=0,bg="azure" ,width='100',relief=tkinter.SUNKEN,pady=30,padx=60)
    my_box.pack()
    Label(my_box,text="Name: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
    Label(my_box,text=user['name'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
    Label(my_box,text="Father Name: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
    Label(my_box,text=user['father'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
    Label(my_box,text="Email: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
    Label(my_box,text=user['email'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
    Label(my_box,text="Contact: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
    Label(my_box,text=user['contact'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
    Label(my_box,text="DOB: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
    Label(my_box,text=user['dob'],bg="azure",pady=5,width='100',font=("Calibri", 12)).pack()

    
