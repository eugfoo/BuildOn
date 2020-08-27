import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import uuid

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
info = None
face = ""
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")


while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        #print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
        info = str(obj.data)
    
    if info is not None:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            face = "Face Detected"
            break
        uniqueID = uuid.uuid1()
        print("here: " + face)
        if face is not None:
            # do something here
            cv2.imwrite("%s.jpg" % uniqueID, frame)
            
            

    cv2.imshow("LOL", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break