import string

import cv2
import os
import time
import uuid
from PIL import Image
from tensorflow.keras import models
import numpy as np

class_names = list(string.ascii_lowercase[:26].replace('z', ''))
images = []
good = []

mac_cam = cv2.VideoCapture(0)

while True:
    retrieve, frames = mac_cam.read()
    cv2.imshow('Try2Catch', frames)
    for imgnum in range(5):
        ret, frame = mac_cam.read()
        imgname = os.path.join('images/' + '' + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        images.append(imgname)
        print(imgnum)
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    for image in images:
        im = Image.open(image)
        im = im.resize((28, 28))
        imgname = os.path.join('images/corrected/' + '' + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        good.append(imgname)
        im.save(imgnum)
        cv2.imwrite(imgname, im)

    for goods in good:
        img = cv2.imread(goods)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        model = models.load_model('image_classification.keras')
        prediction = model.predict(np.array([img] / 255))
        index = np.argmax(prediction)
        print('Prediction is: ', class_names[index])


    mac_cam.release()