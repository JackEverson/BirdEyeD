#Import necessary libraries
from logging import debug
import sqlalchemy
from flask import Flask, render_template, Response, session
from flask_session import Session
from helpers import gen_frames
from werkzeug.security import check_password_hash 

#Initialize the Flask app
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
           
@app.route('/')
def index():
    id = session.get("user_id")
    print(id)
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(use_reloader=True)
