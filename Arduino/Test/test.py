import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600,timeout=0.1)
while True:
    line = ser.readline()
    if line != b"":
        print(line)
    else:
        print("wait")

ser.close()
