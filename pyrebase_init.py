import pyrebase
from tkinter import messagebox as msg

# FIREBASE PROJECT CONFIG

config = {
  "apiKey": "AIzaSyCicmo8iEL_6kgZblYtfkm1TW1oIv1fW-A",
  "authDomain": "have-a-seat-d9fed.firebaseapp.com",
  "databaseURL": "https://have-a-seat-d9fed-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "have-a-seat-d9fed.appspot.com"
}

# INTEGRATING TO OUR PROJECT BACKEND

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

# GET USER INFO THROUGH UID
def get_user(uid):
    user = dict(db.child('users').child(uid).get().val())
    return user

# REGISTER FUNCTION/FIREBASE
def register_auth(email,password,name,contact,dob,f_name):
    user = auth.create_user_with_email_and_password(email, password)
    data =  {'email':email,'uid': user['localId'] ,'name':name,'father':f_name, 'contact':contact, 'dob':dob,'rides':[1]}
    db.child('users').child(user['localId']).set(data)
    return data


# LOGIN FUNCTION/FIREBASE
def login_auth(email,password):
    user  =auth.sign_in_with_email_and_password(email,password)
    data = dict(db.child('users').child(user['localId']).get().val())
    return data


# POST RIDE FUNCTION/FIREBASE
def post_ride(ride,uid):
    posted_rides  = db.child('rides')
    data = posted_rides.child(ride['code']).set(ride)
    
    user = dict(db.child('users').child(uid).get().val())
    if('rides' in user.keys()):
      if(user['rides'][0]==1):
        user['rides']=user['rides'][1::]
      user['rides'].append(ride['code'])
    else:
      user['rides']=[ride['code']]

    db.child('users').child(uid).set(user)

    return user

# GET ALL POSTED RIDES
def get_rides():
  rides = dict(db.child('rides').get().val())
  return rides

# GET SPECIFIC RIDES FROM GIVEN LIST OF CODE NUMBERS
def get_specific_rides(code):
  rides = []
  for x in code:
    if(x!=None):
      if(x>1):
        r = dict(db.child('rides').child(x).get().val())
        rides.append(r)
  return rides

# BOOK A SEAT FOR A USER
def add_booking_to_ride(code,uid,parent):
    r = dict(db.child('rides').child(code).get().val())
    if(int(r['Available Seats'])>0):
      r['Available Seats']=int(r['Available Seats'])-1
      r['Booked Users'].append(uid)
      db.child('rides').child(code).set(r)
      db.child('users').child(uid).child('booked').set(code)
    else:
      msg.showinfo(' BOOKING FAILED',"SEATS FULL")
    parent.destroy()


