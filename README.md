# Bird_eyeD

This is a project aimed at setting up an wildlife camera that can identify birds using artificial intelligence. The project will be set up in several stages, I envision it to go in the following manner:

Initial goals
1) Setup a Raspberry Pi 4 with a camera and experiment with taking pictures and recording video.
2) Setup a simple AI to interpret pictures and/or videos and recognise weather they contain a bird.
3) Combine the systems from step 1) and 2) so that a Raspberry Pi and camera will save an image when it recognises a bird in a live feed of a bird feeder.

Future goals
- Adapt and train the AI further so that it can begin to recognise species of birds. 
- Using a stockpile of labeled photos attempt to create and train my own AI (This will likely be for the experience rather than a performance improvement)

To begin this project I have chosen the following hardware for the actual bird camera:
- Raspberry Pi 4 (4GB of RAM)
- Raspberry Pi Camera Module 3 (Wide lens)
- 64 GB SD card with Raspberry Pi OS install (Linux Debian 'Bullseye')

# Development Timeline
## Beginning the project
22FEB2023
I suspect I will be following core electronics 'object recognition guide with OpenCV' to begin with (https://core-electronics.com.au/guides/object-identify-raspberry-pi/ and https://core-electronics.com.au/projects/backyard-birdcam/).  

## Changing the plan
26FEB2023
I have received all hardware but unfortunately, I have been unsuccessful getting core-electronics code to work for me successfully. This maybe due the fact that they are using the 'Buster' OS while I am using the module 3 Raspberry Pi camera which is only compatible which I can only get to work with 'Bullseye'.

