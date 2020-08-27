from flask import Flask, render_template, Response, redirect, url_for
from camera import VideoCamera
import numpy as np
import requests
import cv2
import pyzbar
import time
import json

app=Flask(__name__)
test = ""

@app.route('/')
def index():
    return "Hello World"

@app.route("/upload")
def upload_qrcode():
    return render_template("upload_qr.html")    

def gen(camera, info, face):
    while True:
        if info is None:
            frame = camera.get_qrframe(info)
            info = frame[1]
            print(info)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n\r\n')
        if info is not None:
            # call safe_access_entry
            frame = camera.get_loading() # calls loading function after scanning QR Code 
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n\r\n')
            break

    while True:
        if face is None:
            frame = camera.get_faceframe(face)
            face = frame[1]
            # call safe_access_face
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n\r\n')
        if face is not None:

            break

@app.route('/video_feed')
def video_feed():
    info = None
    face = None
    return Response(gen(VideoCamera(), info, face), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/qrResultant")
def qr_resultant():
    return render_template("results.html")  

@app.route("/phototemp")
def return_results():
    return render_template("phototemp.html")   

if __name__ == '__main__':
    app.run(debug = True)