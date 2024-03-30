import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class LogInGUI(QMainWindow):

    def __init__(self):
        super(LogInGUI, self).__init__()
        uic.loadUi("LogInGUI.ui", self)
        self.show()

        self.login_btn.clicked.connect(self.login)
        self.actionClose.triggered.connect(self.close)
        self.createAccount.clicked.connect(self.createAcc)

    def login(self):

        if self.username.text() != "" and self.password.text() != "":
            sys.exit()
            # self.password.setEchoMode(QLineEdit.Normal)   for setting password to visible probably on a radio button

        else:
            message = QMessageBox()
            message.setText("Please Enter a Username and Password")
            message.exec_()

    def createAcc(self):
        self.window = CreateAccountGUI()
        self.hide()
        self.window.show()
        # sys.exit()

    def close(self):
        sys.exit()


class CreateAccountGUI(QMainWindow):

    def __init__(self):
        super(CreateAccountGUI, self).__init__()
        uic.loadUi("CreateAccountGUI.ui", self)
        self.show()

        self.create_btn.clicked.connect(self.createAccount)
        self.actionClose.triggered.connect(self.close)
        self.backToLogin.clicked.connect(self.backToLog)

    def createAccount(self):

        if self.password.text() != self.password_2.text():
            message = QMessageBox()
            message.setText("Passwords do not match")
            message.exec_()
        else:
            if self.username.text() != "" and self.password.text() != "":
                sys.exit()
            else:
                message = QMessageBox()
                message.setText("Please enter valid username and password")
                message.exec_()

    def backToLog(self) :
        self.window = LogInGUI()
        self.hide()
        self.window.show()

    def close(self):
        sys.exit()


def main():
    app = QApplication([])
    window = LogInGUI()
    app.exec_()


if __name__ == "__main__":
    main()
