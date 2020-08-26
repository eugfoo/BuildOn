# import the necessary packages
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import uuid
import time


# defining face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor=0.6
font = cv2.FONT_HERSHEY_PLAIN


class VideoCamera(object):
    def __init__(self):
        self.hashnric = ""
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()

    def get_qrframe(self,hashnric):
        success, image = self.video.read()
        image = cv2.resize(image,None,fx=ds_factor,fy=ds_factor, interpolation=cv2.INTER_AREA)

        # Algo to scan QR codes
        decodedObjects = pyzbar.decode(image)
        for obj in decodedObjects:
            #print("Data", obj.data)
            cv2.putText(image, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)   
            hashnric = str(obj.data)
            print(hashnric)
            print("QR SCANNED!")
    
        ret, jpeg = cv2.imencode('.jpg', image)
        list1=[jpeg.tobytes(), hashnric]
        return list1

    def get_faceframe(self):
        success, image = self.video.read()
        image = cv2.resize(image,None,fx=ds_factor,fy=ds_factor, interpolation = cv2.INTER_AREA)
        # face detection
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        face_rects=face_cascade.detectMultiScale(gray,1.3,5)
        # uniqueID = uuid.uuid1()
        for (x,y,w,h) in face_rects:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            # cv2.imwrite("%s.jpg" % uniqueID, image)
            break
        ret, jpeg = cv2.imencode('.jpg', image)
        list3 = [jpeg.tobytes()]
        return list3

    def get_loading(self):
        image = cv2.imread("images/loading.jpg")
        ret, jpeg = cv2.imencode('.jpg', image)
        list2 = [jpeg.tobytes()]

        return list2