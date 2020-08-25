from flask import Flask, render_template, Response
from camera import VideoCamera
import requests
app=Flask(__name__)
test = ""
count = 0

@app.route('/')
def index():
    return "Hello World"

@app.route("/upload")
def upload_qrcode():
    return render_template("upload_qr.html")    

def gen(camera):
    while True:
        if count == 0:
            frame = camera.get_qrframe()
            
        else:
            frame = camera.get_faceframe()
            # print("Temperature scanning")
            # print("Finished")
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/phototemp")
def return_results():
    return render_template("phototemp.html")   

if __name__ == '__main__':
    app.run(debug = True)