from serial import Serial
import random
import time 
import data
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


port = Serial('COM3', 9600)
port.close()
port.open()
cred = credentials.Certificate("admin_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://sfasdf-e46a2-default-rtdb.firebaseio.com/'
})

root = db.reference() 

def main():
    my_dict = root.get('/')[0]
    final_string = str(my_dict['red'])+","+str(my_dict['green'])+","+str(my_dict['blue'])+","+my_dict['message']
    port.write(str.encode(final_string))


while True:
    main()
    time.sleep(2)