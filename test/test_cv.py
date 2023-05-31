import cv2

from imutils.video import VideoStream

vs = VideoStream(src=0).start()
img = vs.read()
cv2.imshow('image', img)
cv2.waitKey(0)

