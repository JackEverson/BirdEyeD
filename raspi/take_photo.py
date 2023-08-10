from picamera2 import Picamera2
from libcamera import controls
import time

# setting up camera
picam2 = Picamera2()
config = picam2.create_still_configuration({"size": (224, 224)})
picam2.configure(config)

debug = False

if debug == True:
    picam2.start(show_preview=True)
else: 
    picam2.start(show_preview=False)
time.sleep(1)
print("Camera started")

print("Camera focus started")
job = picam2.autofocus_cycle(wait=False)
# Now do some other things, and when you finally want to be sure the autofocus
# cycle is finished:

# taking an image
success = picam2.wait(job)
print(f"Camera focusing success: {success}")

img = picam2.capture_image("main")
picam2.switch_mode_and_capture_file(config, "image.png")

print("program completed successfully")
exit(0)
