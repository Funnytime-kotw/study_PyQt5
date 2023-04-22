from PyQt5.QtWidgets import *

class Show_03(QWidget):
    def __init__(self):
        super().__init__()

    def show_new_window_03(self):
        new_window = QDialog(self)
        new_window.setWindowTitle("第三个窗口")
        new_window.resize(400, 400)

        container = QVBoxLayout(new_window)

        dial = QDial()
        dial.setFixedSize(100, 100)
        spin = QSpinBox()
        spin.setFixedSize(100, 100)
        spin.setMaximum(100)
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spin)
        # 当 spin 的值发生改变时，更新 dial 的值
        spin.valueChanged.connect(dial.setValue)
        # 当 dial 的值发生改变时，更新 spin 的值
        dial.valueChanged.connect(spin.setValue)

        back_btn = QPushButton("返回", new_window)
        back_btn.clicked.connect(new_window.close)

        container.addLayout(layout)
        container.addWidget(back_btn)

        new_window.setLayout(container)
        new_window.exec_()


