import serial
import time
import cv2
import numpy
import os

ser = serial.Serial('COM3',9800,timeout=1)
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

            elif (line[0]) == 'C':


                video = cv2.VideoCapture(0)

                face = cv2.load_image_file("One.jpg")
                faceencoding = cv2.face_encodings(face)[0]

                face_encodings_list = [
                    faceencoding]

                face_encodings = []
                s = True
                face_coordinates=[]


                while True:
                    _,frame = video.read()

                    resized_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                    resized_frame_rgb = frame[:, :, ::-1]


                    if s:
                        face_coordinates = cv2.face_locations(resized_frame_rgb)
                        face_encodings = cv2.face_encodings(resized_frame_rgb, face_coordinates)

                        for faces in face_encodings:
                            matches = cv2.compare_faces(face_encodings_list, faces)
                            if matches[0] == True:
                                video.release()
                                cv2.destroyAllWindows()
                                main_function()

                    cv2.imshow('Face Scan', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                video.release()
                cv2.destroyAllWindows()
