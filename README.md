# Bird eyeD

## Live stream through a local web browser
![pigeon](https://github.com/JackEverson/bird_eyeD/assets/111256162/1a3f9870-0683-409c-a038-9da21bf54f25)

## Save Images
![King_parrot_saved](https://github.com/JackEverson/bird_eyeD/assets/111256162/ce94735e-bd42-492f-b6fb-817e50ac2dba)


## Welcome to BirdEyeD! 
This is a project that utilises python, openCV2, and SQLite3 to allow for the settup of a local webpage that will display a video stream of an available webcamera so that images of birds can be captured. The intention is to have it running on small computer (in my case I am using a Raspberry Pi) with an attached webcamera for ease of use and to prevent high expense.

This is project is inspired by [BirdNET](https://birdnet.cornell.edu) and the implementation to a Raspberry Pi done by [Core Electronics](https://core-electronics.com.au/projects/bird-calls-raspberry-pi/). 
This branch of the project has been submitted as the final assessment of Harvard's CS50 course. I intend to work on this project further and make it AI capable so I am able to collect photo's of birds without having to manually push a button. Follow the main branch [here](https://github.com/JackEverson/bird_eyeD).

# Running Bird eyeD
## General requirements:
SQLite3
```
sudo apt-get install sqlite3
```

## python requirements for web app:
1) flask
2) flask-session
3) OpenCV2
4) SQLAlchemy
5) Werkzeug

```
pip install Flask Flask-Session opencv-python SQLAlchemy Werkzeug
```
