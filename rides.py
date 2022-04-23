from tkinter import *

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def post_ride(main):
    
    return post_ride



# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()