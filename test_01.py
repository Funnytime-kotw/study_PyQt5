import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Show_01(QWidget):
    def __init__(self):
        super().__init__()

    def show_new_window_01(self):
        new_window = QDialog(self)
        new_window.resize(200, 200)

        button = QPushButton("返回", new_window)
        button.clicked.connect(new_window.close)
        label = QLabel("1 + 1 = 2", new_window)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        new_window.setWindowTitle("这是按钮1")
        new_window.setLayout(layout)
        new_window.exec_()

