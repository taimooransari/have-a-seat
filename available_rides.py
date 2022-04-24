# from tkinter import *
# import tkinter
# from tkinter.font import BOLD
# from tkinter_custom_button import TkinterCustomButton
# my_screen=None

# def all_rides(screen,user):
#     r={'Available Seats': '3', 'Booked Users': ['A', 'B', 'C'], 'Host': 'Hfnx1gTWrRaJws81fuxEcOx2qeC3', 'Path': [1, 2, 3, 4, 5, 6, 7], 'Starting Time': 'vania pagal aurat', 'code': 54098}
#     global my_screen
#     my_screen = Toplevel(screen)

#     screen_size = str(my_screen.winfo_screenwidth())+'x'+str(my_screen.winfo_screenheight())
#     my_screen.geometry(screen_size)
#     my_screen.title("AVAILABLE RIDE")
#     my_screen.configure(bg="snow3")

    


#     Label(my_screen,text="AVAILABLE RIDE", bg="DodgerBlue2", width="300", height="2", font=("Calibri", 13)).pack()
#     Label(my_screen,text="",bg="snow3",pady=50).pack()
#     # f = Frame(my_screen)
#     # f.pack()
#     for x in range(10):
#         a =single_ride(r,f)
#         a.pack()
    


#     ksbar=Scrollbar(my_screen, orient=VERTICAL)
#     ksbar.grid(row=0, column=1, sticky="ns")

#     popCanv = Canvas(my_screen, width=600, height = 800,
#                      scrollregion=(0,0,500,800)) 
#     popCanv.grid(row=0, column=0, sticky="nsew") 

#     ksbar.config(command=popCanv.yview)
#     popCanv.config(yscrollcommand = ksbar.set)

    
#     my_screen.rowconfigure(0, weight=1) #added (answer to your question)
#     my_screen.columnconfigure(0, weight=1) #added (answer to your question)



#     # my_box=Frame(my_screen,borderwidth=0,bg="azure" ,width='100',relief=tkinter.SUNKEN,pady=30,padx=60)
#     # my_box.pack()
#     # Label(my_box,text="Name: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
#     # Label(my_box,text=user['name'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     # Label(my_box,text="Father Name: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
#     # Label(my_box,text=user['father'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     # Label(my_box,text="Email: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
#     # Label(my_box,text=user['email'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     # Label(my_box,text="Contact: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
#     # Label(my_box,text=user['contact'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     # Label(my_box,text="DOB: ",pady=5,width='100', font=("Calibri", 15,BOLD),anchor='w' ).pack()
#     # Label(my_box,text=user['dob'],bg="azure",pady=5,width='100',font=("Calibri", 12)).pack()

# r={'Available Seats': '3', 'Booked Users': ['A', 'B', 'C'], 'Host': 'Hfnx1gTWrRaJws81fuxEcOx2qeC3', 'Path': [1, 2, 3, 4, 5, 6, 7], 'Starting Time': 'vania pagal aurat', 'code': 54098}

# def single_ride(ride,master = my_screen):
#     a = Frame(master)
#     Label(a,text='CODE: '+str(ride['code']),bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     Label(a,text='TIME: '+ride['Starting Time'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     Label(a,text='SEATS: '+ride['Available Seats'],bg="azure",pady=5,width='100', font=("Calibri", 12)).pack()
#     return a
    



































# Python Program to make a scrollable frame
# using Tkinter

from tkinter import *

class ScrollBar:
	# constructor
	def __init__(self):
		root = Tk()
		h = Scrollbar(root, orient = 'horizontal')
		h.pack(side = BOTTOM, fill = X)
		v = Scrollbar(root)
		v.pack(side = RIGHT, fill = Y)
		
		for i in range(20):    
		    t = Text(root, width = 15, height = 15, wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)
			t.insert(END,"this is some text\n")
	    	t.pack(side=TOP, fill=X)

		h.config(command=t.xview)
		v.config(command=t.yview)
		root.mainloop()

# create an object to Scrollbar class
s = ScrollBar()
		
