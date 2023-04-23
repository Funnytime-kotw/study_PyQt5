import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, \
    QMessageBox
from test_add import add_function

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(300, 300, 300, 200)

        self.button1 = QPushButton('按钮1', self)
        self.button1.clicked.connect(self.open_add_app)
        self.button1.move(100, 80)

    def open_add_app(self):
        self.add_app = AddApp()
        self.add_app.show()

class AddApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Add Two Numbers')
        self.setGeometry(500, 500, 300, 200)

        layout = QVBoxLayout()

        self.label1 = QLabel('Number 1:', self)
        layout.addWidget(self.label1)

        self.lineEdit1 = QLineEdit(self)
        layout.addWidget(self.lineEdit1)

        self.label2 = QLabel('Number 2:', self)
        layout.addWidget(self.label2)

        self.lineEdit2 = QLineEdit(self)
        layout.addWidget(self.lineEdit2)

        self.addButton = QPushButton('Add', self)
        self.addButton.clicked.connect(self.on_click)
        layout.addWidget(self.addButton)

        self.setLayout(layout)

    def on_click(self):
        num1 = float(self.lineEdit1.text())
        num2 = float(self.lineEdit2.text())
        result = add_function(num1, num2)

        QMessageBox.information(self, 'Result', f'The sum of {num1} and {num2} is {result}')

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
