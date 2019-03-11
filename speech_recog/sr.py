import speech_recognition as sr
import RPi.GPIO as GPIO
from time import sleep
import os
#from ser import command
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

##from pyrebase
##firebase = firebase.FirebaseApplication("https://helperglove.firebaseio.com",None)
##db = firebase.database()
##data = {"Name":"Abhay"}
##db.child().push(data)
import pyrebase
config = { "apiKey": "AlzaSyZfM5PDT8Fe3uPsyrfdzn6Cx6O7Kwg-3rs",
           "authDomain": "helperglove.firebaseapp.com",
           "databaseURL": "https://helperglove.firebaseio.com",
           "storageBucket": "helperglove.appspot.com"
           
    }
firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
db = firebase.database()
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
#db.child("users").push(data)
##os.system("python3 ser.py")
##f = open("abc.txt", "r")
##msg = f.read(3)
#print "message"+ f.read(3)
#data = {"Alert":"No alert","Name": 'L'}
#results = db.child("").set(data)

mic_name = "USB PnP Sound Device"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
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
    
    #data = {"Alert":"No Alert","Name":msg}
    with sr.Microphone(device_index = 002, sample_rate = sample_rate, chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print ("say something")
        audio = r.listen(source)
        
        try:
                text = r.recognize_google(audio)
            
                print ("you said:" + text)
                if text=="Abhijeet" or text=="Shivansh" or text =="stop" or text=="wait":
                    print("Alert")
                    os.system("python3 ser.py")
                    f = open("abc.txt", "r")
                    msg = f.read()
                    msg = msg.replace('b', '')
                    msg = msg.replace("'",'')
                    f.close()
                    print "message"+str(msg)
    #data = {"Alert":"No Alert","Name":msg}
                    data = {"Alert":text,"Name":msg}
                    #data1 = {"Name":"Hello"}
                    
                    results = db.child("").set(data)
                    GPIO.output(23,1)
                    sleep(2)
                    GPIO.output(23,0)
                    sleep(2)
                    GPIO.output(23,1)
                    sleep(2)
                    GPIO.output(23,0)
                    
                    #goto l
                #results = db.child("").set(data1)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results ,{0}".format(e))
            
