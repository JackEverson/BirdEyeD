import cv2
import numpy
import time

def load_model():
    net = cv2.dnn.readNet("./yolo/yolov3-tiny.weights", "./yolo/yolov3-tiny.cfg")
    return net


def yolo_run(img, net):

    classes = []
    with open("./yolo/coco.names", 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    layer_name = net.getLayerNames()
    output_layer = [layer_name[i - 1] for i in net.getUnconnectedOutLayers()]
    colours = numpy.random.uniform(0, 255, size=(len(classes), 3))

    # img = cv2.imread("./yolo/nmr.jpg")
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channel = img.shape

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0,0,0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layer)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = numpy.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    objects = []
    for i in indexes:
        objects.append(classes[class_ids[i]])
    # print(objects)
    # print("\n")
    
    if 'bird' in objects:
        bird = True
        bird_time = time.time()
    else:
        bird = False
        bird_time = 0

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(objects)
            colour = colours[i]
            cv2.rectangle(img, (x,y), (x+y, y+h), colour, 2)
            cv2.putText(img, label, (x, y), font, 1, colour, 1)

    return img, bird, bird_time
