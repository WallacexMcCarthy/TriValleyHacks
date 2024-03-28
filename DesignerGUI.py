from PyQt5.QtWidgets import *
from PyQt5 import uic


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("BasicLogin.ui", self)
        self.show()


def main():
    app = QApplication([])
    window = GUI()
    app.exec_()


if __name__ == "__main__":
    main()
    