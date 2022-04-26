import pyrebase

config = {
  "apiKey": "AIzaSyCicmo8iEL_6kgZblYtfkm1TW1oIv1fW-A",
  "authDomain": "have-a-seat-d9fed.firebaseapp.com",
  "databaseURL": "https://have-a-seat-d9fed-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "have-a-seat-d9fed.appspot.com"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def register_auth(email,password,name,contact,dob,f_name):
    user_details = db.child('users')
    user = auth.create_user_with_email_and_password(email, password)
    data =  {'email':email,'uid': user['localId'] ,'name':name,'father':f_name, 'contact':contact, 'dob':dob,'rides':[1]}
    user_details.child(user['localId']).set(data)
    return data

def login_auth(email,password):
    user_details = db.child('users')
    user  =auth.sign_in_with_email_and_password(email,password)
    data = dict(user_details.child(user['localId']).get().val())
    # print('===========================',data)
    return data


def post_ride(ride,uid):
    # user_details = db.child('users')

    posted_rides  = db.child('rides')
    data = posted_rides.child(ride['code']).set(ride)
    
    user = dict(db.child('users').child(uid).get().val())
    user['rides'].append(ride['code'])
    # print(user)
    db.child('users').child(uid).set(user)

    return user


def get_rides():
  rides = dict(db.child('rides').get().val())
  return rides

def get_specific_rides(code):
  rides = []
  for x in code:
    r = dict(db.child('rides').child(x).get().val())
    rides.append(r)
  return rides



















# print(login('ma07595@st.habib.edu.pk','gasdgagduka'))




# data = user_details.get().val()         
# print(data['8GqHzbCxodfTQsvMSraC8B1peeh1']['name'])
# print(register('ma07727@st.habib.edu.pk','gasdgagduka'))





# auth = firebase.auth()
# user = auth.create_user_with_email_and_password('taimoor.shuja132@gmail.com', '12345678')
# auth.send_email_verification(user['idToken'])
# db = firebase.database()
# data = {"name": "Mortimer 'Morty' Smith"}
# v = db.child("users").push(data)
# print(v)
# db.child("users").child("Morty")
# data = {"name": "Muhammad 'Taimoor' Ansari"}
# db.child("users").child("Morty").set(data)

# data = db.child('users').get().val()

# print(data['Morty'])