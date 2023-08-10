import time
import os

import torch
import numpy as np
from torchvision import models, transforms

from PIL import Image
from picamera2 import Picamera2
from libcamera import controls

torch.backends.quantized.engine = 'qnnpack'

# setting up camera
picam2 = Picamera2()
config = picam2.create_still_configuration({"size": (224, 224)})
picam2.configure(config)
picam2.start(show_preview=True)
job = picam2.autofocus_cycle(wait=False)
success = picam2.wait(job)

preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

net = models.quantization.mobilenet_v2(pretrained=True, quantize=True)
# jit model to take it from ~20fps to ~30fps
net = torch.jit.script(net)

started = time.time()
last_logged = time.time()
frame_count = 0
photos = 0

with torch.no_grad():
    while True:
        # read frame
        image = picam2.capture_image("main")

        # preprocess
        input_tensor = preprocess(image)

        # create a mini-batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        # run model
        output = net(input_batch)
        # do something with output ...
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        # Read the categories
        with open("imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]
        # Show top categories per image
        top5_prob, top5_catid = torch.topk(probabilities, 5)
        print("\n"*6)
        for i in range(top5_prob.size(0)):
            print(f"{categories[top5_catid[i]]}: {top5_prob[i].item()*100:.2f}%")

        '''
        # saving images
        if photos < 10: 
            picam2.switch_mode_and_capture_file(config, os.path.join("./images/testing/", (str(photos)+".png")))
            photos += 1
        '''


        # log model performance
        frame_count += 1
        now = time.time()
        if now - last_logged > 1:
            print(f"{frame_count / (now-last_logged)} fps")
            last_logged = now
            frame_count = 0
        time.sleep(3)
