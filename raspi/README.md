'''
following guide from:
https://pytorch.org/tutorials/intermediate/realtime_rpi.html

need to add the following to the /boot/config.txt file:
start_x=1 # enables features such as the camera
gpu_mem=128 # only if this is a smaller number, gives camera 128M for processing
camera_auto_detect=1

install the following:
pip install torch torchvision torchaudio
pip install opencv-python
pip install numpy --upgrade
sudo apt install -y python3-picamera2 (or "sudo apt install -y python3-picamera2 --no-install-recommends" for gui-less application)
''' 
