import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


def login_pressed(username, password):

    print([username, password])
    sys.exit()


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Login")
    window.setGeometry(960, 540, 500, 500)

    layout = QVBoxLayout()

    username_box = QTextEdit()
    username_box.setFixedSize(500, 25)

    password_box = QTextEdit()
    password_box.setFixedSize(500, 25)

    login_button = QPushButton("Log In")
    login_button.clicked.connect(lambda: login_pressed(username_box.toPlainText(), password_box.toPlainText()))

    layout.addWidget(username_box)
    layout.addWidget(password_box)
    layout.addWidget(login_button)

    window.setLayout(layout)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
