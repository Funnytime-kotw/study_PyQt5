# 设计一个主窗口，所有程序将封装到主窗口里面

from PyQt5.QtWidgets import *
from add_app import AddApp
from place_to_center import center_on_screen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("主程序")

        self.resize(400, 400)
        center_on_screen(self)

        self.button_add = QPushButton("加法", self)
        self.button_add.clicked.connect(self.open_add_app)
        self.button_add.move(150, 60)

        self.button_close = QPushButton("关闭", self)
        self.button_close.clicked.connect(self.close)
        self.button_close.move(150, 200)

    def open_add_app(self):
        self.add_app = AddApp()
        self.add_app.show()

