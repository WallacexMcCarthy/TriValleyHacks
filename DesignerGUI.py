import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("BasicLogin2.ui", self)
        self.show()

        self.login_btn.clicked.connect(self.login)

    def login(self):

        if self.username.text() != "" and self.password.text() != "":
            sys.exit()
        else:
            message = QMessageBox()
            message.setText("Please Enter a Username and Password")
            message.exec_()


def main():
    app = QApplication([])
    window = GUI()
    app.exec_()


if __name__ == "__main__":
    main()
