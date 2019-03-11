import os
import pyrebase
config = { "apiKey": "AlzaSyZfM5PDT8Fe3uPsyrfdzn6Cx6O7Kwg-3rs",
           "authDomain": "helperglove.firebaseapp.com",
           "databaseURL": "https://helperglove.firebaseio.com",
           "storageBucket": "helperglove.appspot.com"
           
    }
firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
db = firebase.database()
while 1:
    os.system("python3 ser.py")
    f = open("abc.txt", "r")
    msg = f.read()
    msg = msg.replace('b', '')
    msg = msg.replace("'",'')
    f.close()
    print "message"+str(msg)
    data = {"Alert":"No Alert","Name":msg}
                    #data1 = {"Name":"Hello"}
                    
    results = db.child("").set(data)
