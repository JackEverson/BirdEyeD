#Import necessary libraries
import os, sys
import helpers

from helpers import login_required
from logging import debug
from flask import Flask, redirect, render_template, Response, request, session
from flask_session import Session
from werkzeug.security import check_password_hash 

#Initialize the Flask app
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
           
# creating an SQLalchemy engine to interact with the db
helpers.setup_db()
    
@app.route("/")
@login_required
def index():
    id = session.get("user_id")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        quser_name = request.form.get("username")
        qpassword =  request.form.get("password")

        user = helpers.check_deets(quser_name, qpassword)

        if user == None:
            error = "Username not on record"
            return render_template("login.html", error=error)
        
        if user == "error":
            error = "Username and/or Password incorrect"
            return render_template("login.html", error=error)


        session["user_id"] = user.id
        return redirect("/")

    else: # if GET method
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/video_feed")
@login_required
def video_feed():
    return Response(helpers.gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(use_reloader=True)
