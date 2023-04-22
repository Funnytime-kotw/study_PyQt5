# study_PyQt5

## ==信号与槽==

信号（signal）：事件（按钮点击、窗口关闭等）或状态（选中、切换等）。当程序触发了某种状态或者发生了某种事件（比如：按钮被点击了, 内容改变等等），那么即可发射出来一个信号。

槽（slot）：若想捕获这个信号，然后执行相应的逻辑代码，那么就需要使用到槽 ， 槽际上是一个函数， 当信号发射出来后，会执行与之绑定的槽函数

连接信号与槽：为了让点击某个按钮时执行某个逻辑，需要把具体的信号和槽函数绑定到一起

`对象.信号.connect(槽函数)`

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 300)
        btn = QPushButton("点我点我", self)
        btn.setGeometry(200, 200, 100, 30)
        btn.clicked.connect(self.click_my_btn)

    def click_my_btn(self, arg):
        print("点击按钮啦~", arg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
```

### ==自定义信号==

```python
import sys
import time
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, \
    QLabel, QPushButton, QVBoxLayout, QScrollArea, QHBoxLayout, \
    QWidget
from PyQt5.QtCore import Qt, pyqtSignal

# 使用QMainWindow就需要添加一个QWidget窗口，将控件放上去
class MyWindow(QMainWindow):
    # 声明一个信号，必须放在函数外面
    my_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()  # 存放消息

    def init_ui(self):
        self.resize(500, 400)
        container = QVBoxLayout()

        # 显示检测到的信息
        self.msg = QLabel("")
        self.msg.resize(440, 15)
        print(self.msg.frameSize())
        self.msg.setWordWrap(True)  # 自动换行
        self.msg.setAlignment(Qt.AlignTop)  # 靠上
        self.msg.setStyleSheet("background-color: yellow; color: black;")

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)
        # 让QScrollArea自适应大小
        scroll.setWidgetResizable(True)

        # 创建一个垂直布局器，添加滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 创建一个水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测", self)
        btn.setGeometry(150, 200, 200, 50)
        btn.clicked.connect(self.check)
        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 如果使QWidget就可以之间self.setLayout(container)
        central_widget = QWidget(self)
        central_widget.setLayout(container)
        self.setCentralWidget(central_widget)

        # 绑定信号和槽函数
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)  # 设置下一条消息的位置
        self.msg.repaint()

    def check(self):
        for i, ip in enumerate(["192.168.1.%d" %x for x in range(0, 255)]):
            msg = "模拟，正在检查 %s 上的漏洞。。。" %ip
            print(msg)  # print(msg, end = "")表示不换行
            if i % 5 == 3:
                # 自定义信号发送，相当于调用了my_slot槽函数
                self.my_signal.emit(msg + "【发现漏洞】")
            time.sleep(0.01)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle("Please click!")
    w.show()
    app.exec()
```

