import serial
import time
import numpy
import os

ser = serial.Serial('COM4',9600,timeout=1)
time.sleep(2)



def main_function():
    print("correct password")


    
text=[]

while True:
    line = ser.readline().decode("utf-8")
    if line =="":
        pass
    else:
        try:
            text.append(int(line))
            print(text)
        except:
            if (line[0])== 'A':
                if text == []:
                    pass
                else:
                    text.pop()
                    print(text)

            if (line[0])== 'B':
                if text == []:
                    pass
                else:
                    if text==[3,1,2]:
                        print("correct passsword")
                    else:
                        print("incorrect password")

            