import sys
from PyQt5.QtWidgets import *
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()
