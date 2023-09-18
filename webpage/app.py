#Import necessary libraries
from logging import debug
import sqlalchemy
from flask import Flask, render_template, Response, session
from helpers import gen_frames
from werkzeug.security import check_password_hash, generate_password_hash

#Initialize the Flask app
app = Flask(__name__)
app.run(use_reloader=True)
           
@app.route('/')
def index():

    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
