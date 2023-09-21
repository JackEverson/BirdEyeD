# Bird eyeD

This is a simple machine learning project that is being setup to collect photos of birds. The intention is to use a predefined model (for example MobileNet v2) or to train a model with a already existing data set (for example cifar10) that can generally recognise birds. From there I will set up a Raspberry Pi with a camera to collect bird photo's. These photo's will then be used to train a new network that can begin to recognise species of birds more specifically.

## Live stream through a local web browser
![pigeon](https://github.com/JackEverson/bird_eyeD/assets/111256162/1a3f9870-0683-409c-a038-9da21bf54f25)

## Save Images
![King_parrot_saved](https://github.com/JackEverson/bird_eyeD/assets/111256162/ce94735e-bd42-492f-b6fb-817e50ac2dba)

The steps towards achieving this goal are:
1) Set up a simple webpage that can stream a camera feed. Need the ability to take and save photo's to disk and potentially look up photos that have been taken.
2) Research an AI model that is capable of recognising that a bird is in an image. This is likely to take the form of an "image recognition" model rather than an "object model". (This is likely to use something like YOLO).
3) Give an option to deploy the AI model while camera feed is running. If the AI model recognises a bird in in an image it writes that image to disk.
4) (potential long term) Use the images collected to train a new AI model that can potentially recognise species of birds.
