import email
from tkinter import *
from tkinter import messagebox as msg
import sys
import tkinter
from tkinter.font import BOLD
from turtle import width
from venv import create
from tkinter_custom_button import TkinterCustomButton
from pyrebase_init import login_auth
from my_account import my_account_screen
from create_rides import create_ride
from available_rides import all_rides

main_sc=None
login_success_screen = None
user_info=None
def login_success(user):
    login_screen.destroy()
    global main_sc
    global login_success_screen
    global check
    global login_success_screen
    global user_info
    user_info=user
    check = True
    login_success_screen = Toplevel(main_sc)
    login_success_screen.title("User: "+ user['name'])
    login_success_screen.geometry(screen_size)
    Label(login_success_screen,text="Manage User", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_success_screen, text="",pady=50).pack()
    button1 = TkinterCustomButton(master=login_success_screen,text="My Account", height=60,width=150 ,corner_radius=0, command=my_account_temp,fg_color="maroon",hover_color="violet red")
    button2 = TkinterCustomButton(master=login_success_screen,text="Available Rides", height=60,width=150 ,corner_radius=0, command=lambda : all_rides(login_success_screen,user),fg_color="maroon",hover_color="violet red")
    button3 = TkinterCustomButton(master=login_success_screen,text="Connections", height=60,width=150 ,corner_radius=0, command=logout,fg_color="maroon",hover_color="violet red")
    

    # login_success_screen = Frame(login_success_screen,bg="lightblue", width=250)
    # login_success_screen.pack()
    # btn = TkinterCustomButton(master=login_success_screen,text="change", height=60,width=150 ,corner_radius=0, command=change_screens,fg_color="maroon",hover_color="violet red")
    # btn.pack()
    nodes = [
        "DHA",
        "GULSHAN",
        "JAUHAR"
        ]
    
    global time_var
    global ride_type
    global point
    global seats



    time_var = StringVar()
    ride_type = StringVar()
    point = StringVar()
    seats = StringVar()
    type_label = Label(login_success_screen,font=('Calibri',16,BOLD), text="Type :")
    type_label.pack()
    ride_type.set('incoming')
    type_box = OptionMenu(login_success_screen, ride_type, *['incoming','outgoing'])
    type_box.config(width=10,height=1,font=('Calibri',12))
    type_box.pack()
    Label(login_success_screen, text="").pack()
    point_label = Label(login_success_screen,font=('Calibri',16,BOLD), text="Point :")
    point_label.pack()
    point.set(nodes[0])
    point_box = OptionMenu(login_success_screen, point, *nodes)
    point_box.config(width=10,height=1,font=('Calibri',12))
    point_box.pack()
    Label(login_success_screen, text="").pack()
    time_label = Label(login_success_screen,font=('Calibri',16,BOLD), text="Time :")
    time_label.pack()
    time_entry =  Entry(login_success_screen,width="20",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=time_var)
    time_entry.pack()
    Label(login_success_screen, text="").pack()
    seats_label = Label(login_success_screen,font=('Calibri',16,BOLD), text="Seats :")
    seats_label.pack()  
    seats.set('1')
    seat_box = OptionMenu(login_success_screen, seats, *['1','2','3'])
    seat_box.config(width=10,height=1,font=('Calibri',12))
    seat_box.pack()
    Label(login_success_screen, text="").pack()
    button = TkinterCustomButton(master=login_success_screen,text="POST",height=50,width=80 ,corner_radius=10, command=post_ride_temp,fg_color="green yellow",text_color='black',hover_color="lime green")
    button.pack()

# ===========================================

    button1.place(relx=0,rely=0.068)
    button2.place(relx=0,rely=0.15)
    button3.place(relx=0,rely=0.24)
    button = TkinterCustomButton(master=login_success_screen,text="Logout",height=60,width=150 ,corner_radius=0, command=logout,fg_color="maroon",hover_color="violet red")
    button.place(relx=0,rely=0.85)

def post_ride_temp():
    global user_info
    user_info = create_ride(user_info,time_var.get(),ride_type.get(),point.get(),seats.get())
    msg.showinfo(user_info['rides'][-1],'Ride -- POSTED SUCCESFULLY')
    return user

def change_screens(index=2,a=login_success_screen):
    dct ={0:'Hello',1:'world',2:'how r u'}
    a.label['text']=dct[index]
    
def my_account_temp():
    global login_success_screen
    account_screen  = my_account_screen(login_success_screen,user)

def logout():
    login_success_screen.destroy()

def login(main_screen):
    global main_sc
    main_sc=main_screen
    global login_screen
    global screen_size
    login_screen = Toplevel(main_screen)
    screen_size = str(main_screen.winfo_screenwidth())+'x'+str(main_screen.winfo_screenheight())
    login_screen.configure(bg="snow3")

    login_screen.title("Login")
    login_screen.geometry(screen_size)

    # if(check):
    #     login_success()
    #     return login_screen
    Label(login_screen,text="Login to continue", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()

    # Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="",bg="snow3",pady=50).pack()
   
 
    global email_verify
    global password_verify
 
    email_verify = StringVar()
    password_verify = StringVar()
 
    global email_login_entry
    global password_login_entry
 
    Label(login_screen, text="Email :",bg="snow3",font=(16)).pack()
    email_login_entry = Entry(login_screen, textvariable=email_verify,width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13))
    email_login_entry.pack()
    Label(login_screen, text="",bg="snow3").pack()
    Label(login_screen, text="Password :",bg="snow3",font=(16)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*',width="35",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13))
    password_login_entry.pack()
    Label(login_screen, text="",bg="snow3").pack()
    button_2 = TkinterCustomButton(master=login_screen,text="Login",height=60,width=150 ,corner_radius=10, command=verify_auth,fg_color="DodgerBlue2")
    button_2.pack()
    return login_screen

user = None
    
def verify_auth():
        global user
        # global check 
        try:
            # if user exists and credentials are correct
            # function to check auth from db
            # ---------------------------------------------------------------
            user = login_auth(email_verify.get(),password_verify.get())
            # user = login_auth('taimoor@gmail.com','12345678')
        except:
            errorType=1
            if(errorType==1):
                msg.showinfo(' LOGIN FAILED',"Check your credentials")
            elif(errorType==2):
                msg.showinfo(' LOGIN FAILED',"User Doesn't exist. \n Register first.")
        else:
            login_success(user)

sys.modules[__name__] = login
 