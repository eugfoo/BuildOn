from flask import Flask, render_template
app=Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/upload")
def upload_qrcode():
    return render_template("upload_qr.html")    


@app.route("/phototemp")
def return_results():
    return render_template("phototemp.html")   

if __name__ == '__main__':
    app.run(debug = True)