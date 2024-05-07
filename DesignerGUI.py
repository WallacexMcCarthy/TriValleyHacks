import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from PyQt5.QtWidgets import *
from PyQt5 import uic


# Global variables for the firebase data
cred = credentials.Certificate('sign-language-user-data-da9ba1b8df23.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
global current_account


class LogInGUI(QMainWindow):

    def __init__(self):

        # opening gui and connecting buttons
        super(LogInGUI, self).__init__()
        uic.loadUi("LogInGUI.ui", self)
        self.show()

        self.login_btn.clicked.connect(self.login)
        self.actionClose.triggered.connect(self.close)
        self.createAccount.clicked.connect(self.createAcc)
        self.showPassword.clicked.connect(self.showPass)

    def login(self):

        # username and password must not be empty
        if self.username.text() == "" or self.password.text() == "":
            message = QMessageBox()
            message.setText("Please Enter a Username and Password")
            message.exec_()
            return

        doc_ref = db.collection("users").document(self.username.text())
        doc = doc_ref.get()

        # username has to exist as a document in the firebase data
        if not doc.exists:
            message = QMessageBox()
            message.setText("Username or password incorrect")
            message.exec_()

        # check for input password matching firebase password
        elif self.password.text() != str(doc.to_dict()["password"]):
            message = QMessageBox()
            message.setText("Username or password incorrect")
            message.exec_()

        # setcurrent account and open menu gui
        else:
            global current_account
            current_account = self.username.text()
            self.window = MainMenu()
            self.hide()
            self.window.show()

    def createAcc(self):
        # opens create account gui
        self.window = CreateAccountGUI()
        self.hide()
        self.window.show()
        # sys.exit()

    def showPass(self):
        # toggles password visibility
        if self.showPassword.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def close(self):
        sys.exit()


class CreateAccountGUI(QMainWindow):

    def __init__(self):
        # opening gui and connecting buttons
        super(CreateAccountGUI, self).__init__()
        uic.loadUi("CreateAccountGUI.ui", self)
        self.show()

        self.create_btn.clicked.connect(self.createAccount)
        self.actionClose.triggered.connect(self.close)
        self.backToLogin.clicked.connect(self.backToLog)
        self.showPassword.clicked.connect(self.showPass)
        self.showPassword_2.clicked.connect(self.showPassConfirm)

    def createAccount(self):
        # passwords must match
        if self.password.text() != self.password_2.text():
            message = QMessageBox()
            message.setText("Passwords do not match")
            message.exec_()

        # username and password must both be longer than 7 chars
        elif len(self.username.text()) < 7 or len(self.password.text()) < 7:
            message = QMessageBox()
            message.setText("Username and password must be more than 7 characters")
            message.exec_()
        else:
            doc_ref = db.collection("users").document(self.username.text())
            doc = doc_ref.get()

            # if the input username matches a document name in the database
            if doc.exists:
                message = QMessageBox()
                message.setText("Username already exists")
                message.exec_()

            # add the given data to a new document in the database
            else:
                data = {"username": self.username.text(), "password": self.password.text()}
                doc_ref.set(data)
                message = QMessageBox()
                message.setText("Account Created")
                message.exec_()
                # opens the login gui
                self.window = LogInGUI()
                self.hide()
                self.window.show()


    def backToLog(self):
        # opens the login gui
        self.window = LogInGUI()
        self.hide()
        self.window.show()

    def showPass(self):
        # toggles visibility for password 1
        if self.showPassword.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def showPassConfirm(self):
        # toggles visibility for password 2
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
        doc_ref = db.collection("users").document(current_account)
        self.level_progress_bar.setValue(0)
        self.welcome_lbl.setText("Welcome " + current_account)


def main():
    main_app = QApplication([])
    window = LogInGUI()
    main_app.exec_()


if __name__ == "__main__":
    main()
