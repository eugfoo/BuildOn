from flask import Flask, render_template, Response, redirect, url_for
from camera import VideoCamera
import numpy as np
import requests
import time



app=Flask(__name__)
test = ""

@app.route('/')
def index():
    return "Hello World"

@app.route("/upload")
def upload_qrcode():
    return render_template("upload_qr.html")    

def gen(camera, hashnric):
    while True:
        if hashnric is None:
            frame = camera.get_qrframe(hashnric)
            hashnric = frame[1]
            print(hashnric)
            # call miltons API gateway here...
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n\r\n')
        if hashnric is not None:
            frame = camera.get_loading() # calls loading function after scanning QR Code 
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n\r\n')
            break
    while True:
        frame = camera.get_faceframe()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame[0] + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    hashnric = None
    return Response(gen(VideoCamera(), hashnric), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/qrResultant")
def qr_resultant():
    return render_template("results.html")  

@app.route("/phototemp")
def return_results():
    return render_template("phototemp.html")   

if __name__ == '__main__':
    app.run(debug = True)