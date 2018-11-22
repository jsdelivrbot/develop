import serial
import time

def main():
    ser = serial.Serial('/dev/ttyACM0',9600,timeout = 0.1)
    String_data = ser.read()
    int_data = int.from_bytes(String_data , 'big')
    int_data = int_data * 2
    print(int_data)

if __name__ == "__main__":
    while True:
        main()

ser.close
