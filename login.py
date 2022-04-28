from tkinter import *
from tkinter import messagebox as msg
import sys
import tkinter
from tkinter.font import BOLD
from map import show_path
from tkinter_custom_button import TkinterCustomButton
from pyrebase_init import login_auth
from my_account import my_account_screen
from create_rides import create_ride
from available_rides import all_rides
from my_rides import my_rides


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
    edges = [
    ('Gulistan-e-Jauhar', 'Habib University', 2.8),
    ('Airport', 'Habib University', 7.5),
    ('Pehelwan Goth', 'Habib University', 2.9),
    ('Scheme 33', 'Pehelwan Goth', 7.7),
    ('Gulshan-e-Jamal', 'Gulistan-e-Jauhar', 3.7),
    ('Gulshan-e-Iqbal', 'Gulistan-e-Jauhar', 5),
    ('Gulzar-e-Hijri', 'Gulistan-e-Jauhar', 6),
    ('Scheme 33', 'Gulzar-e-Hijri', 0.5),
    ('Gulshan-e-Jamal', 'Rashid Minhas', 3.8),
    ('Scheme 33', 'Gulshan-e-Iqbal', 5.4),
    ('Rashid Minhas', 'Gulshan-e-Iqbal', 3),
    ('Nazimabad', 'Gulshan-e-Iqbal', 9.7),
    ('North Karachi', 'Gulshan-e-Iqbal', 8.3),
    ('Shahra-e-Faisal', 'Airport', 12),
    ('Surjani Town', 'Nazimabad', 17),
    ('Surjani Town', 'North Karachi', 8.3),
    ('Clifton', 'Shahra-e-Faisal', 17),
    ('Saddar', 'Shahra-e-Faisal', 12),
    ('Defense', 'Shahra-e-Faisal', 14),
    ('Defense', 'Korangi', 6.2),
    ('Korangi', 'Shahra-e-Faisal', 9.6),
    ('Garden East', 'Saddar', 3.1),
    ('Garden West', 'Saddar', 2.7),
    ('Kharadar', 'Saddar', 4.7),
    ('Gulshan-e-Hadeed', 'Landhi Town', 19),
    ('Landhi Town', 'Shahra-e-Faisal', 19),
    ('Gulberg', 'Gulshan-e-Iqbal', 4.9),
    ('Gulberg', 'Nazimabad', 8),
    ('Samanabad', 'Gulshan-e-Iqbal', 6.7),
    ('Samanabad', 'Gulberg', 1.8),
    ('Samanabad', 'Yaseenabad', 2.8),
    ('Yaseenabad', 'Gulshan-e-Iqbal', 6.4),
    ('Liaquatabad', 'Federal B Area', 3.1),
    ('Federal B Area', 'Gulshan-e-Iqbal', 8.9),
    ('Federal B Area', 'Yaseenabad', 3.1),
    ('Liaquatabad', 'Azizabad', 4.3),
    ('Azizabad', 'Yaseenabad', 1.8),
    ('Azizabad', 'Gulshan-e-Iqbal', 7.2),
    ('Malir Cantt', 'Shahra-e-Faisal', 20),
    ('Malir Cantt', 'Gulzar-e-Hijri', 13),
    ('Malir Cantt', 'Gulistan-e-Jauhar', 13)
]
    login_success_screen = Toplevel(main_sc)
    login_success_screen.title("User: "+ user['name'])
    login_success_screen.geometry(screen_size)
    Label(login_success_screen,text="Manage User", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(login_success_screen, text="",pady=50).pack()
    button1 = TkinterCustomButton(master=login_success_screen,text="My Account", height=60,width=150 ,corner_radius=0, command=my_account_temp,fg_color="maroon",hover_color="violet red")
    button2 = TkinterCustomButton(master=login_success_screen,text="Available Rides", height=60,width=150 ,corner_radius=0, command=lambda : all_rides(login_success_screen,user),fg_color="maroon",hover_color="violet red")
    button3 = TkinterCustomButton(master=login_success_screen,text="My Rides", height=60,width=150 ,corner_radius=0, command=lambda: my_rides(login_success_screen,user['uid']) ,fg_color="maroon",hover_color="violet red")
    button4 = TkinterCustomButton(master=login_success_screen,text="MAP", height=60,width=150 ,corner_radius=0, command=lambda: show_path(edges).visualize() ,fg_color="maroon",hover_color="violet red")


    nodes = ['Airport', 'Azizabad', 'Clifton', 'Defense', 'Federal B Area', 'Garden East', 'Garden West', 'Gulberg', 'Gulistan-e-Jauhar', 'Gulshan-e-Hadeed', 'Gulshan-e-Iqbal', 'Gulshan-e-Jamal', 'Gulzar-e-Hijri',  'Kharadar', 'Korangi', 'Landhi Town', 'Liaquatabad', 'Malir Cantt', 'Nazimabad', 'North Karachi', 'Pehelwan Goth', 'Rashid Minhas', 'Saddar', 'Samanabad', 'Scheme 33', 'Shahra-e-Faisal', 'Surjani Town', 'Yaseenabad']

    
    global time_var
    global ride_type
    global point
    global seats



    time_var = StringVar()
    ride_type = StringVar()
    point = StringVar()
    seats = StringVar()

    main_box = Frame(login_success_screen)
    main_box.configure(width='350',bg='lightblue')
    main_box.pack()

    type_label = Label(main_box,font=('Calibri',16,BOLD), text="Type :",bg='lightblue')
    type_label.pack()
    ride_type.set('incoming')
    type_box = OptionMenu(main_box, ride_type, *['incoming','outgoing'])
    type_box.config(width=10,height=1,font=('Calibri',12))
    type_box.pack()
    Label(main_box, text="",bg='lightblue').pack()
    point_label = Label(main_box,font=('Calibri',16,BOLD), text="Point :",bg='lightblue')
    point_label.pack()
    point.set(nodes[0])
    point_box = OptionMenu(main_box, point, *nodes)
    point_box.config(width=10,height=1,font=('Calibri',12))
    point_box.pack()
    Label(main_box, text="",bg='lightblue').pack()
    time_label = Label(main_box,font=('Calibri',16,BOLD), text="Time :",bg='lightblue')
    time_label.pack()
    time_entry =  Entry(main_box,width="20",  borderwidth=15, relief=tkinter.FLAT,font=("Calibri",13),textvariable=time_var)
    time_entry.pack()
    Label(main_box, text="",bg='lightblue').pack()
    seats_label = Label(main_box,font=('Calibri',16,BOLD), text="Seats :",bg='lightblue')
    seats_label.pack()  
    seats.set('1')
    seat_box = OptionMenu(main_box, seats, *['1','2','3'])
    seat_box.config(width=10,height=1,font=('Calibri',12))
    seat_box.pack()
    Label(main_box, text="",bg='lightblue').pack()
    button = TkinterCustomButton(master=main_box,text="POST",height=50,width=80 ,corner_radius=10, command=post_ride_temp,fg_color="green yellow",text_color='black',hover_color="lime green")
    button.pack()


    button1.place(relx=0,rely=0.068)
    button2.place(relx=0,rely=0.16)
    button3.place(relx=0,rely=0.24)
    button4.place(relx=0,rely=0.33)
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

    Label(login_screen,text="Login to continue", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()

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
        try:
            user = login_auth(email_verify.get(),password_verify.get())
        except :
            msg.showinfo(' LOGIN FAILED',"Check your credentials")
        else:
            login_success(user)

sys.modules[__name__] = login
 