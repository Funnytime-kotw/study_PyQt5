import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyWindow():
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("test_01.ui")
        print(self.ui.__dict__)
        self.user_name = self.ui.lineEdit  # 用户名输入框
        self.user_password = self.ui.lineEdit_2  # 用户密码框
        self.login_btn = self.ui.pushButton  # 登录按钮
        self.login_btn.clicked.connect(self.login)
        self.textBrowser = self.ui.textBrowser

        self.ui.show()

    def login(self):
        user_name_t = self.user_name.text()
        user_password_t = self.user_password.text()
        if user_name_t == "admin" and user_password_t == "123":
            self.textBrowser.setText("欢迎%s " % user_name_t)
            self.textBrowser.repaint()
        else:
            self.textBrowser.setText("用户名或密码错误")
            self.textBrowser.repaint()
        print(user_name_t)
        print(user_password_t)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    app.exec()
