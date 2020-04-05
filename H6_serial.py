#Python koodi sarjaportista tulevan datan lukemiseen
import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600, timeout=0)
tauko=10

while True:
    try:
        data=ser.readline()
        temp1=''
        for value in data:
            #debug
            #print(chr(value))
            temp1=temp1+chr(value)
        print(temp1)
        temp1=0
    except IOError:
        print('Error tuli')
    time.sleep(tauko)