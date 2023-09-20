import cv2
import os
import sys

from flask import redirect, session
from functools import wraps
import flask_session
from werkzeug.security import check_password_hash 

def gen_frames():  
    '''
    for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' for local webcam use cv2.VideoCapture(0)
    '''
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

 
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

# SQL and SQLAlchemy code 
from sqlalchemy import Integer, create_engine, engine, insert, String, Column, select
from sqlalchemy.orm import Mapped, Session, declarative_base

def establish_ORM():
    Base = declarative_base()
    class User(Base):
        __tablename__ = "users"

        id= Column(Integer,primary_key=True)
        user_name= Column(String(30), nullable=False, unique=True)
        hash= Column(String(), nullable=False, unique=True)

        def __repr__(self) -> str:
            return f"users(id={self.id!r}, user_name={self.user_name!r}, hash={self.hash!r})"


    engine = create_engine("sqlite:///bird.db", echo=True)
    Base.metadata.create_all(engine)
    return engine, User


def setup_db():
    if not os.path.isfile("./bird.db"):
        create_db = True
    else:
        create_db = False

    engine, User = establish_ORM()

    if create_db:
        print("User database not found, creating new database")
        with Session(engine) as session:
            sushi = User(
                    user_name="sushi",
                    hash="pbkdf2:sha256:600000$ImcpaqcSmppVQOVD$b1967fe4454e10e3d693e7854c9d6828d7c5f5d05dbebdbba65602e8bba1800c"
                    )
            session.add_all([sushi])
            session.commit()
            print("database has been created, please ensure the default password is changed imediately")
    else: 
        print("User database has been found, database ready")

def check_deets(qusername, qpassword):
    engine, User = establish_ORM()
    stmt = select(User).where(User.user_name == qusername)
    with Session(engine) as session:
        user = session.execute(stmt).fetchone()[0]
    if user == None:
        return "error"
    correct = check_password_hash(user.hash, qpassword)
    if correct:
        return user
    else:
        return "error"
