import serial
import time
import re

val_size = 3;
values = [0 for x in range(val_size)]
isValids = [False for x in range(val_size)]
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)

while True:
    headByte = ser.read()  # 1文字読み込み
    head = int.from_bytes(headByte, 'big')
    if head == 128:
        isValids = [False for x in range(val_size)]

    for i in range(val_size):
        if head == 128+i:
            highByte = ser.read()  # 1文字読み込み
            lowByte = ser.read()  # 1文字読み込み
            high = int.from_bytes(highByte, 'big')
            low = int.from_bytes(lowByte, 'big')
            values[i] = (high<<7) + low;
            if 0 <= values[i] and values[i] <= 1023 :
                isValids[i] = True;
                #print(values[i])

    if all(i == True for i in isValids):
        print(values)
