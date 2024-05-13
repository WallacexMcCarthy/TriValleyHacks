import sys
from PyQt5.QtWidgets import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import cv2
import os
import time
import uuid
from PIL import Image


cred = credentials.Certificate('firebase/firebase-sdk.json')
firebase_admin.initialize_app(cred)
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
login_button = QPushButton("Log In")
username_box = QTextEdit()
password_box = QTextEdit()
new_user_button = QPushButton("Sign Up")
images = []


def main():
    window.setWindowTitle("Login")
    window.setGeometry(25, 25, 500, 750)
    username_box.setFixedSize(500, 25)

    password_box.setFixedSize(500, 25)

    login_button.clicked.connect(lambda: login(username_box.toPlainText(), password_box.toPlainText()))
    new_user_button.clicked.connect(lambda: sign_up(username_box.toPlainText(), password_box.toPlainText()))

    layout.addWidget(username_box)
    layout.addWidget(password_box)
    layout.addWidget(login_button)
    layout.addWidget(new_user_button)


    window.setLayout(layout)
    window.show()
    app.exec_()


def open_application():
    login_button.deleteLater()
    username_box.deleteLater()
    password_box.deleteLater()
    new_user_button.deleteLater()

    mac_cam = cv2.VideoCapture(0)

    while True:
        retrieve, frames = mac_cam.read()
        cv2.imshow('Try2Catch', frames)
        for imgnum in range(5):
            ret, frame = mac_cam.read()
            imgname = os.path.join('images/' + '' + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            images.insert(imgnum)
            print(imgnum)
            cv2.imwrite(imgname, frame)
            im = Image.open(imgnum)
            frame = im.resize((28, 28))
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        mac_cam.release()


def login(username, password):
    open_application()
    # if(username == "wallace@gmail.com" and password == "wallace1230"):
    #     open_application()

def sign_up(username, password):
    print([username, password])
    try:
        user = auth.create_user(email=username, password=password)
    except:
        print("exception")
    print([username, password])


if __name__ == '__main__':
    main()
