from PyQt5.QtWidgets import *
from test_add_app import add_function
from place_to_center import center_on_screen

class AddApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("加法")

        self.resize(300, 300)
        center_on_screen(self)

        container = QVBoxLayout()

        # 设置垂直布局器
        v_layout = QVBoxLayout()

        v_layout.addStretch(1)
        self.label_01 = QLabel('数字1：')
        self.label_01.move(200, 200)
        v_layout.addWidget(self.label_01)
        v_layout.addStretch(1)
        self.lineEdit_01 = QLineEdit(self)
        v_layout.addWidget(self.lineEdit_01)
        v_layout.addStretch(2)
        self.label_02 = QLabel('数字2：')
        v_layout.addWidget(self.label_02)
        v_layout.addStretch(1)
        self.lineEdit_02 = QLineEdit(self)
        v_layout.addWidget(self.lineEdit_02)
        v_layout.addStretch(1)

        # 设置水平布局器
        h_layout = QHBoxLayout()
        self.addButton = QPushButton("执行", self)
        self.addButton.clicked.connect(self.on_click)
        h_layout.addWidget(self.addButton)
        self.addButton = QPushButton("返回", self)
        self.addButton.clicked.connect(self.close)
        h_layout.addWidget(self.addButton)

        container.addLayout(v_layout)
        container.addLayout(h_layout)

        self.setLayout(container)

    def on_click(self):
        try:
            num1 = float(self.lineEdit_01.text())
            num2 = float(self.lineEdit_02.text())
            result = add_function(num1, num2)
            QMessageBox.information(self, '结果', f'{num1} + {num2} = {result}')
        except ValueError:
            QMessageBox.warning(self, '错误', '请输入两个数字')

