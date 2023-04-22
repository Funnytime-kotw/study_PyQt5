from PyQt5.QtWidgets import *

class Show_02(QWidget):
    def __init__(self):
        super().__init__()

    def show_new_window_02(self):
        new_window = QDialog(self)
        new_window.setWindowTitle("第二个窗口")
        new_window.resize(200, 200)

        back_btn = QPushButton("返回", new_window)
        back_btn.clicked.connect(new_window.close)
        layout = QVBoxLayout(self)
        layout.addWidget(back_btn)

        new_window.setLayout(layout)
        new_window.exec_()

