This section of code has now become somewhat legacy. Initially I acquired a Raspberry Pi camera module V3 which is not compatible with OpenCV2 (it can only run with picamera2 library). This was greatly complicating the process as it would mean I needed to sets of working code (one for OpenCV and one for picamera2). I have since acquired a cheap webcamera that is working excellently with the OpenCV python library.

need to add the following to the /boot/config.txt file:
start_x=1 # enables features such as the camera
gpu_mem=128 # only if this is a smaller number, gives camera 128M for processing
camera_auto_detect=1

install the following:
pip install torch torchvision torchaudio
pip install opencv-python
pip install numpy --upgrade
sudo apt install -y python3-picamera2 (or "sudo apt install -y python3-picamera2 --no-install-recommends" for gui-less application)
