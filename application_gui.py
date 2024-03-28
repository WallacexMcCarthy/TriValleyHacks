from PyQt5.QtWidgets import *

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(200, 200, 300, 300)

    label = QLabel(window)
    label.setText("Hello")
    label.show()

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
