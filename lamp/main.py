from serial import Serial
import random
import time 
import database

port = Serial('COM3', 9600)
port.close()
port.open()


while True:
    final_string  = database.main()
    port.write(str.encode(final_string))
    time.sleep(2)