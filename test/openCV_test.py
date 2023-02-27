import numpy as np 
import cv2 as cv

cap = cv.isOpened()
if not cap.isOpened():
    print("Cannot open camera")
    exit()