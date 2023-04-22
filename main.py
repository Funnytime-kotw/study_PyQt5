import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from test_01 import Show_01
from test_02 import Show_02
from test_03 import Show_03

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 500)
        layout = QVBoxLayout()
        layout.setSpacing(50)
        layout.setContentsMargins(50, 50, 50, 50)

        btn_01 = QPushButton("这是第一个程序", self)
        btn_01.clicked.connect(self.show_new_window_01)
        btn_02 = QPushButton("这是第二个程序", self)
        btn_02.clicked.connect(self.show_new_window_02)
        btn_03 = QPushButton("这是第三个程序", self)
        btn_03.clicked.connect(self.show_new_window_03)

        layout.addWidget(btn_01)
        layout.addWidget(btn_02)
        layout.addWidget(btn_03)

        self.setLayout(layout)

    def show_new_window_01(self):
        sw = Show_01()
        sw.show_new_window_01()

    def show_new_window_02(self):
        sw = Show_02()
        sw.show_new_window_02()

    def show_new_window_03(self):
        sw = Show_03()
        sw.show_new_window_03()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle("这是一个测试程序")
    w.show()
    app.exec_()

