from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
from turtle import width
from map import show_path
from tkinter_custom_button import TkinterCustomButton
from pyrebase_init import get_rides
from pyrebase_init import get_user,add_booking_to_ride
top=None

# ALL RIDES SCREEN
    
def all_rides(root,user):
    global top
    allRides = get_rides()
    top  =  Toplevel(root)
    screen_size = str(root.winfo_screenwidth()-50)+'x'+str(root.winfo_screenheight())
    top.geometry(screen_size)
    top.title("AVAILABLE RIDE")
    top.configure(bg="snow3")
    main_frame = Frame(top)
    Label(top,text="ALL RIDES", bg="lightblue", width="300", height="2", font=("Calibri", 13)).pack()
    main_frame.pack(fill = BOTH, expand = 1,anchor='c')

    canvas = Canvas(main_frame)
    canvas.pack(side = LEFT, fill = Y, anchor=CENTER,expand = 1)


    scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL,command = canvas.yview)
    scrollbar.pack(side = RIGHT, fill = Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    second_frame = tk.Frame(canvas)
    
    canvas.configure()
    canvas.create_window((0, 0), window = second_frame, anchor = "n")
    for code in allRides:
        if(int(allRides[code]['Available Seats'])>0 and user['uid'] not in allRides[code]['Booked Users'] and user['uid']!=allRides[code]['Host'] ):
            a = single_ride(allRides[code],user['uid'],second_frame)
            a.pack(anchor=CENTER)
            Label(a,pady=5,height=1, font=("Calibri", 12)).pack(fill=X)


# SINGLE RIDE FRAME DISPLAYING THE RIDES INFO
def single_ride(ride,uid,master):
    path= ride['Path'][0][0]+' --------> '+ ride['Path'][-1][-1]
    u = get_user(ride['Host'])
    a = Frame(master)
    a.configure(bg='azure',width='270')
    Label(a,text='CODE: '+str(ride['code']),bg="azure",pady=5, font=("Calibri", 12)).pack(fill = X)
    Label(a,text='TIME: '+ride['Starting Time'],bg="azure",pady=5, font=("Calibri", 12)).pack(fill = X)
    Label(a,text='SEATS: '+str(ride['Available Seats']),bg="azure",pady=5, font=("Calibri", 12)).pack(fill = X)
    Label(a,text='HOST: '+u['name']+'/'+u['contact'],bg="azure",pady=5, font=("Calibri", 12)).pack(fill = X)
    Label(a,text=path,bg="azure",pady=5, font=("Calibri", 12)).pack(fill = X)
    path_btn = TkinterCustomButton(master = a,text="Path",height=40,width=60 ,corner_radius=10,command=lambda: show_path(ride['Path']).visualize())
    btn = TkinterCustomButton(master = a,text="Book",height=40,width=60 ,corner_radius=10,command=lambda: add_booking_to_ride(ride['code'],uid,a))
    path_btn.pack()
    Label(a,pady=5,height='1',bg='azure', font=("Calibri", 12)).pack(fill=X)
    btn.pack()

    
    return a
    


































