from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
