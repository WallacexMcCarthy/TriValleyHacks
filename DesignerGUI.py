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
        self.showPassword.clicked.connect(self.showPass)

    def login(self):
        if self.username.text() != "" and self.password.text() != "":
            self.window = MainMenu()
            self.hide()
            self.window.show()
        else:
            message = QMessageBox()
            message.setText("Please Enter a Username and Password")
            message.exec_()

    def createAcc(self):
        self.window = CreateAccountGUI()
        self.hide()
        self.window.show()
        # sys.exit()

    def showPass(self):
        if self.showPassword.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

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
        self.showPassword.clicked.connect(self.showPass)
        self.showPassword_2.clicked.connect(self.showPass_2)

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

    def backToLog(self):
        self.window = LogInGUI()
        self.hide()
        self.window.show()

    def showPass(self):
        if self.showPassword.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def showPass_2(self):
        if self.showPassword_2.isChecked():
            self.password_2.setEchoMode(QLineEdit.Normal)
        else:
            self.password_2.setEchoMode(QLineEdit.Password)

    def close(self):
        sys.exit()


class MainMenu(QMainWindow):
    def __init__(self):
        username: str

        super(MainMenu, self).__init__()
        uic.loadUi("MainMenu.ui", self)
        self.show()
        username = "Isaac"
        self.level_progress_bar.setValue(0)
        self.welcome_lbl.setText("Welcome " + username)


def main():
    app = QApplication([])
    window = LogInGUI()
    app.exec_()


if __name__ == "__main__":
    main()
