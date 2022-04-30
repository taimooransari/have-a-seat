from tkinter import *
import tkinter
from tkinter import messagebox
import register
import login
from tkinter_custom_button import TkinterCustomButton

# FUNCTION INITIALIZING MAIN TKINTER WINDOW 

def main_account_screen():
    global main_screen
    
    main_screen = Tk()
    screen_size = str(main_screen.winfo_screenwidth())+'x'+str(main_screen.winfo_screenheight())
    main_screen.geometry(screen_size)
    main_screen.title("Have A Seat")
    main_screen.configure(bg="snow3")



    Label(text="Proceed from below", bg="DodgerBlue2", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="",bg="snow3",pady=50).pack()
    main_box=Frame(borderwidth=0,bg="azure" ,width=80,relief=tkinter.SUNKEN,pady=30,padx=60)
    main_box.pack()
    button_1 = TkinterCustomButton(master=main_box,text="LOGIN",height=60,width=150 ,corner_radius=10,command=login_temp,fg_color="DodgerBlue2")
    button_1.pack()
    Label(main_box,text="",bg="snow3").pack()

    button_2 = TkinterCustomButton(master=main_box,text="REGISTER",height=60,width=150 ,corner_radius=10, command=register_temp,fg_color="DodgerBlue2")
    button_2.pack()
    Label(main_box,text="",bg="snow3").pack()
    button_3 = TkinterCustomButton(master=main_box,text="ADMIN", corner_radius=10,fg_color="SlateBlue1",hover_color="pale violet red" ,command=admin_temp,height=60,width=150)
    button_3.pack()
    
    Label(text="Designed by: Taimoor, Vania, Ali & Talha.", justify=LEFT,bg="lightblue", width="300", height="2", font=("Calibri", 13)).place(relx = 0.5,  
                   rely = 0.9, 
                   anchor = 'center')
    main_screen.mainloop()

check=False
reg_screen=None
log_screen=None
deposit_screen=None
withdraw_screen=None
admin_screen=None



# EXTRA FUNCTIONS TO AID NAVIGATION 


def admin_temp():
    global admin_screen   
    go_home()
    messagebox.showinfo(" Try again in future","FEATURE UNDER DEVELOPMENT",)


def register_temp():
    global reg_screen
    go_home()
    reg_screen=register(main_screen)


def login_temp():
    global log_screen
    go_home()
    log_screen=login(main_screen)



def go_home():
    if(reg_screen!=None):
        reg_screen.destroy()
    if(log_screen!=None):
        log_screen.destroy()
    if(admin_screen!=None):
        admin_screen.destroy()
        
# MAIN FUNC CALL
main_account_screen()