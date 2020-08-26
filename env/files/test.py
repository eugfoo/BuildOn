import cv2
import numpy as np

cap = cv2.VideoCapture(0)

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('window-name', frame)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        cv2.imwrite("frame%d.jpg" % count, frame)
        count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()