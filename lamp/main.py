from serial import Serial
import random
import time 
import data

port = Serial('COM3', 9600)
port.close()
port.open()
while True:
    redval = str(250)
    greenval = str(0)
    blueval = str(0)
    message = "hello"
    final_string  = redval+","+greenval+","+blueval+","+message
    port.write(str.encode(final_string))
    time.sleep(2)