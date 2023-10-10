# BirdEyeD

## Live stream through a local web browser
![pigeon](https://github.com/JackEverson/bird_eyeD/assets/111256162/1a3f9870-0683-409c-a038-9da21bf54f25)

## Save Images
![King_parrot_saved](https://github.com/JackEverson/bird_eyeD/assets/111256162/ce94735e-bd42-492f-b6fb-817e50ac2dba)

## Deploy Tiny-YOLOv3 to capture pictures of birds in your absence
![Screenshot from 2023-10-11 07-50-16](https://github.com/JackEverson/BirdEyeD/assets/111256162/07905c2d-63a2-4ccb-89bf-7fc4cbba1fb8)

# Welcome to BirdEyeD! 
This is a project that utilises Python, OpenCV2, YOLO, and SQLite3 to host a local webpage with a video stream so that images of birds can be captured. The intention is to have it running on small computer (in my case I am using a Raspberry Pi) with an attached webcamera. The visual AI model Tiny-YOLOv3 is utilised through OpenCV2 to allow for the automatic taking of photos without the need for a human user.

This is project is inspired by [BirdNET](https://birdnet.cornell.edu) and the implementation to a Raspberry Pi done by [Core Electronics](https://core-electronics.com.au/projects/bird-calls-raspberry-pi/). 

# Setup of BirdEyeD
This project was targeted to run on a Raspberry Pi 4 with 4GB of RAM and a 64GB microsd card (total space occupied after everything was up and running was about 3.4GB, I just wanted to take a lot of pictures). The operating system is Raspberry Pi OS 11 "bullseye". I chose to buy a cheap webcamera for this project but I believe the official Raspberry Pi camera Module v2 should work to (PLEASE NOTE: the Raspberry Pi Camera Module v3 is not compatible with OpenCV2 which this project depends on). Testing was also done with my laptop running Ubuntu v22.04.3 LTS (Jammy Jellyfish) using its build in camera (and the purchased webcamera) and everything worked correctly.

## Quick Start
Assuming you have all the dependencies and requirements you can clone this repository with:

`git clone -b main https://github.com/JackEverson/BirdEyeD.git`

Change into the project directory:

`cd BirdEyeD`

and then run the flask server (where <ip_address> is the local ip address of the device):

`flask run -h <ip_address>`

You can then type the ip address of the device into a browser on any machine that is attached to the local network. The default username is "sushi" and the default password is "birdeyed".

## Setup and requirements
After a fresh install it is good to make sure everything is up to date by running the command:

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

or if you are using conda:

`conda install -c anaconda flask`

`conda install -c conda-forge flask-session`

`conda install -c anaconda numpy`

`conda install -c anaconda sqlalchemy`

`conda install -c conda-forge werkzeug`

`- conda install -c conda-forge matplotlib`

`- conda install -c anaconda requests`


### Cloning respository 
To clone the respository you just need to run the following command:

`git clone -b cs50 https://github.com/JackEverson/BirdEyeD.git`

From there you can change into the project directory and should be able to run the web page with the command:

`flask run`

or if you want to access the feed from a different device from the one you are running BirdEyeD on:

`flask run -h <ip_address>`

# Running BirdEyeD 

A webpage should now be available at the IP address that was used to run flask. Once open you can login with username "sushi" and password "birdeyed". 

PLEASE NOTE: This password should be changed immediately through the settings menu. While it is unlikely (depending who is on your local network) for the webpage to be hacked you should be aware that while this program is running you are essentially offering any camera attached to this computer to your local network. Please be aware of this while operating.  

To capture images you can click on the "Capture Image" button (this button should autofocus so you can also just hit enter). All images are saved as a png file in the images directory in the project file and follow the format year-month-day-hour-minute-second. 

To Activate the YOLO simply click the "Activate AI camera" button. Depending on your hosting system this may dramatically reduce the framerate (This is particularly noticable on a Raspberry Pi). All of Tiny-YOLOv3's outputs will now be displayed to the screen using blue boundary boxes. BirdEyeD will only take a photo if a 'bird' object is detected (this photo will not include the blue boundary box). The AI camera mode also has a cooldown of 5 seconds so photo's are not taken too frequently. When the AI saves an image the letters AI will appear at the end of the file name to let you know that it was not taken by a human.

The settings menu can be accessed by pushing the three bars in the top right corner of the webpage and then selecting Settings. Here you can change your password and select a different camera if you have multiple camera's attached to your system.

# Trouble shooting

Just a few points about the program that may help:
- The default username is "sushi" and the default password is "birdeyed"
- If no camera is attached the program will fail to run as OpenCV will return an empty array
- images will be saved in the images directory in the project folder
- The AI camera is setup to only take photos if a 'bird' object is seen
- The AI camera has a cooldown of 5 seconds and will not include the blue boundary box in the saved image

# Tiny-YOLO 

The AI model used is the Tiny You Only Look Once version 3 (YOLOv3-Tiny). This is currently packaged in the repo but this is likely to modified and retrained in the future as it seems to be  with Australian birds. Information on YOLO is available at: https://pjreddie.com/darknet/yolo/

@article{yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal = {arXiv},
  year={2018}
}

# Future Plans

- Retraining YOLOv3-Tiny on captured photos to improve the AI recognition of Australian birds in my area
- Ability to view captured images through the web browser
- Adding the ability to record videos

Checkout the dev branch to see what is currently being worked on:

https://github.com/JackEverson/BirdEyeD/tree/dev
