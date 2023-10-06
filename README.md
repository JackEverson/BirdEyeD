# BirdEyeD

## Live stream through a local web browser
![pigeon](https://github.com/JackEverson/bird_eyeD/assets/111256162/1a3f9870-0683-409c-a038-9da21bf54f25)

## Save Images
![King_parrot_saved](https://github.com/JackEverson/bird_eyeD/assets/111256162/ce94735e-bd42-492f-b6fb-817e50ac2dba)

# Welcome to BirdEyeD! 
This is a project that utilises Python, OpenCV2, and SQLite3 to host a local webpage with a video stream so that images of birds can be captured. The intention is to have it running on small computer (in my case I am using a Raspberry Pi) with an attached webcamera. 

This is project is inspired by [BirdNET](https://birdnet.cornell.edu) and the implementation to a Raspberry Pi done by [Core Electronics](https://core-electronics.com.au/projects/bird-calls-raspberry-pi/). 
I wanted to use a Raspberry Pi and a cheap webcamera to make the project easily accessable and affordable.

# Setup of BirdEyeD
This project was targeted to run on a Raspberry Pi 4 with 4GB of RAM and a 64GB microsd card (total space occupied after everything was up and running was about 3.4GB, I just wanted to take a lot of pictures). The operating system is Raspberry Pi OS 11 "bullseye". I chose to buy a cheap webcamera for this project but I believe the official Raspberry Pi camera Module v2 should work to (PLEASE NOTE: the Raspberry Pi Camera Module v3 is not compatible with OpenCV2 which this project depends on). Testing was also done with my laptop running Ubuntu v22.04.3 LTS (Jammy Jellyfish) using its build in camera (and the purchased webcamera) and everything worked correctly.

## Setup and requirements
First thing you should always do after a fresh install is to run the command:

`sudo apt update && sudo apt upgrade -y`

### Git 
Git is needed to clone this respository (unless you just want to download the project as a zip file). Git can be installed with following command:

`sudo apt-get install git`

### SQLite3
SQLite3 is required for the user and password management. I wanted to use SQL (and with it SQLAlchemy) to expand my knowledge with databases and to learn how to use Object Relational Mapper (ORM) tools. It will be valuable to have SQL if this application is required to be scaled. SQLite3 can be installed with the following command:

`sudo apt-get install sqlite3`

### OpenCV2

OpenCV2 is used to interact with the camera and can be installed with:

`sudo apt install python3-opencv`

### Python3
Python3 is also necessary, the version I am using on my Raspberry Pi is Python 3.9.2. It should be installed as default to a fresh Raspberry Pi OS install but incase it is not you can use the following command:

`sudo apt install python3`

There are also a number of Python libraries that need to be installed. We first need to install pip if it isn't installed:

`sudo apt install python3-pip`

Then we need the following libraries:
- Flask
- Flask-session
- SQLAlchemy
- Werkzeug

They can all be installed with the command:

`sudo pip install Flask Flask-Session SQLAlchemy Werkzeug`

or with conda:

`conda install -c anaconda flask`

`conda install -c conda-forge flask-session`

`conda install -c anaconda numpy`

`conda install -c anaconda sqlalchemy`

`conda install -c conda-forge werkzeug`


### Cloning respository 
To clone the respository you just need to run the following command:

`git clone -b cs50 https://github.com/JackEverson/BirdEyeD.git`

From there you can change into the project directory and should be able to run the web page with the command:

`flask run -h <ip_address_of_device>`


# Running BirdEyeD 

A webpage should now be available at the IP address that was used to run flask. Once open you can login with username "sushi" and password "birdeyed". 

PLEASE NOTE: This password should be changed immediately through the settings menu. While it is unlikely (depending who is on your local network) for the webpage to be hacked you should be aware that while this program is running you are essentially offering any camera attached to this computer to your local network. Please be aware of this while operating.  

The settings menu can be accessed by pushing the three bars in the top right corner of the webpage and then selecting Settings. If you have multiple camera's attached you can also change your camera selection from this menu. 

If you select the three bars in the top right corner and then select Video Feed you will see the current feed from the selected camera. You can take a photo at anytime by selecting the 'Capture image' button (this should autofocus so you can also just hit enter). Photo's are stored in the images directory in the project folder and will be named after the date and time they were taken.

# Trouble shooting

Just a few points about the program that may help:
- The default username is "sushi" and the default password is "birdeyed"
- If no camera is attached the program will fail to run as OpenCV will return an empty array
- images will be saved in the images directory in the project folder

# Need to add to documentation
- Quick start guide
- Packages for AI 
- conda install -c conda-forge matplotlib
- conda install -c anaconda requests

The AI model used is the Tiny You Only Look Once version 3 (YOLOv3-Tiny). This is currently packaged in the repo but will become a download requirement in future. The AI model is likely to change in future (I am looking to train my own model for Australian birds). 

@article{yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal = {arXiv},
  year={2018}
}