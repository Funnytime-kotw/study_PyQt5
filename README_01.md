# study_PyQt5

## PyQt基本UI

https://doc.itprojects.cn/0001.zhishi/python.0008.pyqt5rumen/index.html#/README

### 第一个Qt程序

```py
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建一个对象，传参，必须
    app = QApplication(sys.argv)

    # 创建一个窗口对象，设置标题
    w = QWidget()
    w.setWindowTitle("第一个PyQt")
    w.show()

    # 展示窗口，循环等待，必须
    app.exec()
```



### 模块介绍

PyQt中有非常多的功能模块，开发中最常用的功能模块主要有三个:

- **QtCore**:包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用
- **QtGui**:包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类
- **QtWidgets**:包含了一些列创建桌面应用的UI元素

可以参考PyQt官网的所有模块，地址：https://www.riverbankcomputing.com/static/Docs/PyQt5/module_index.html#ref-module-index

C++具体实现的API文档，地址：https://doc.qt.io/qt-5/qtwidgets-module.html



### 基本控件

#### 按钮 QPushButton

```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("这是一个PyQt程序")
    
    # 在窗口里添加控件
    btn = QPushButton("这是一个按钮")
    # 设置按钮的父亲是当前窗口，即在当前窗口显示
    btn.setParent(w)
    
    w.show()
    app.exec_()
```

### 文本 QLabel

```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("这是一个PyQt程序")
    
    # 创建一个QLabel文本并指明父对象
    label = QLabel("账号：", w)
    # 设置label的位置和宽高
    label.setGeometry(20, 20, 60, 60)

    w.show()
    app.exec_()
```

### 输入框 QLineEdit

```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("这是一个PyQt程序")

    # 创建一个QLabel文本并指明父对象
    label = QLabel("账号：", w)
    # 设置label的位置和宽高
    label.setGeometry(30, 20, 60, 60)

    # 创建一个文本框并指明父对象
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(30, 70, 200, 20)

    # 添加按钮
    btn = QPushButton("注册", w)
    btn.setGeometry(100, 100, 70, 30)

    w.show()
    app.exec_()
```

### 调整窗口大小和位置 resize, move

```python
	from PyQt5.QtWidgets import QWidget, QApplication, \
    QPushButton, QLabel, QLineEdit, QDesktopWidget
    # 设置窗口的大小
    w.resize(300, 300)

    # 将窗口设置在左上角
    w.move(0, 0)

    # 使窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    w.move(x - 150, y - 150)  # todo

    # 更通用的方法
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - (int)(width / 2), y - (int)(height / 2))  # 不支持浮点数
```

### 设置窗口icon QIcon

```python
    from PyQt5.QtGui import QIcon
    from PyQt5 import Qt
    # 设置图标
    w.setWindowIcon(QIcon('C:/Users/Administrator/Desktop/1.png'))
    # 隐藏标题栏
    w.setWindowFlags(Qt.Qt.CustomizeWindowHint)
```



## 布局

在Qt里面布局分为四个大类 ：

- QBoxLayout
- QGridLayout
- QFormLayout
- QStackedLayout

### QBoxLayout

直译为：盒子布局

一般使用它的两个子类`QHBoxLayout` 和 `QVBoxLayout` 负责水平和垂直布局

```python
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, \
    QVBoxLayout, QWidget, QPushButton, QGroupBox, QMainWindow
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)
        self.setWindowTitle(("布局"))

        # 设置垂直布局，必须
        Vlayout = QVBoxLayout()

        # 设置每个按钮之间的间距比，默认平均
        Vlayout.addStretch(1)
        # 创建一个按钮并把它添加到对象
        btn1 = QPushButton("按钮1")
        Vlayout.addWidget(btn1)

        Vlayout.addStretch(1)
        btn2 = QPushButton("按钮2")
        Vlayout.addWidget(btn2)

        Vlayout.addStretch(1)
        btn3 = QPushButton("按钮3")
        Vlayout.addWidget(btn3)
        Vlayout.addStretch(2)

        # 让当前窗口使用这个排列，必须
        self.setLayout(Vlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

```

```python
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, \
    QVBoxLayout, QWidget, QPushButton, QGroupBox, QRadioButton
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 300)
        self.setWindowTitle(("布局"))

        # 设置外层垂直布局
        container = QVBoxLayout()

        # 创建一个组
        hobby_Vlayout = QVBoxLayout()
        hobby_box = QGroupBox("爱好")
        hobby_btn1 = QRadioButton("唱歌")
        hobby_btn2 = QRadioButton("打球")
        hobby_btn3 = QRadioButton("写字")
        hobby_Vlayout.addWidget(hobby_btn1)
        hobby_Vlayout.addWidget(hobby_btn2)
        hobby_Vlayout.addWidget(hobby_btn3)
        hobby_box.setLayout(hobby_Vlayout)

        # 创建第二个组
        gender_Hlayout = QHBoxLayout()
        gender_box = QGroupBox("性别")
        gender_btn1 = QRadioButton("男")
        gender_btn2 = QRadioButton("女")
        gender_Hlayout.addWidget(gender_btn1)
        gender_Hlayout.addWidget(gender_btn2)
        gender_box.setLayout(gender_Hlayout)

        # 将这两个组添加到容器里
        container.addStretch(1)
        container.addWidget(hobby_box)
        container.addStretch(1)
        container.addWidget(gender_box)
        container.addStretch(1)
        # 显示最外层的容器
        self.setLayout(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()

```

### QGridLayout

网格布局，有的人称之为九宫格布局

```python
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, \
    QVBoxLayout, QWidget, QGridLayout, QGroupBox, QRadioButton, \
    QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 300)
        self.setWindowTitle(("计算器"))

        # 设置外层垂直布局
        container = QVBoxLayout()
        data = {
            0 : ["7", "8", "9", "+", "("],
            1 : ["4", "5", "6", "-", ")"],
            2 : ["1", "2", "3", "*", "<-"],
            3 : ["0", ".", "=", "/", "("],
        }

        # 创建一个输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        container.addWidget(edit)

        # 创建一个网格布局
        grid = QGridLayout()
        for line_num, line_data in data.items():
            for col_num, row_num in enumerate(line_data):
                btn = QPushButton(row_num)
                grid.addWidget(btn, line_num, col_num)
        # 把网格布局追加到容器
        container.addLayout(grid)
        
        self.setLayout(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()
```

### QFormLayout

一般适用于提交数据**form表单**。比如： 登录，注册类似的场景

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout,\
    QLineEdit, QPushButton, QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置禁止更改宽高
        self.resize(300, 150)
		
        # 创建外层容器和表单
        container = QVBoxLayout()
        container.addStretch(1)
        form_layout = QFormLayout()

        # 创建输入框
        edit1 = QLineEdit()
        edit1.setPlaceholderText("请输入账号")
        form_layout.addRow("账号", edit1)
        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        form_layout.addRow("密码", edit2)
        # 创建按钮
        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100, 30)

        container.addLayout(form_layout)
        container.addWidget(login_btn, alignment = Qt.AlignRight)
        container.addStretch(1)

        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()
```

### QStackedLayout

提供了多页面切换的布局，一次只能看到一个界面。 **抽屉布局**

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout,\
    QLineEdit, QPushButton, QApplication, QWidget, QStackedLayout, \
    QLabel

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:yellow;")

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是第二个抽屉", self)
        self.setStyleSheet("background-color:red;")

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是布局")
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        # 创建一个抽屉布局
        self.stacked_layout = QStackedLayout()
        # 创建两个单独的窗口
        win1 = Window1()
        win2 = Window2()
        # 将两个窗口添加到抽屉
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        self.resize(300, 300)
        container = QVBoxLayout()

        # 创建一个显示具体内容的布局器
        widget = QWidget()  # 在container内再创建一个QWidget
        widget.setLayout(self.stacked_layout)  # 把抽屉放到QWidget
        widget.setStyleSheet("background-color:white;")

        # 创建两个按钮，用于切换布局
        btn_press1 = QPushButton("抽屉1")
        btn_press2 = QPushButton("抽屉2")
        # 给按钮添加事件，点击后调用函数
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)
        
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置当前调用抽屉时的索引值
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        self.stacked_layout.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()
```

## 窗口

在Qt中，生成窗口有三种方式： `QWidget` 、 `QMainWindow` 、 `QDialog`

- QWidget：控件和窗口的父类 ，自由度高（什么都东西都没有），没有划分菜单、工具栏、状态栏、主窗口 等区域
- QMainWindow：是` QWidget`的子类，包含菜单栏，工具栏，状态栏，标题栏等，中间部分则为主窗口区域
- QDialog：对话框窗口的基类

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(200, 200)
        label = QLabel("这是文字~~")
        label.setStyleSheet("font-size:30px;color:red")

        # 调用父类中的menuBar，从而对菜单栏进行操作
        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")

        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("复制")
        edit_menu.addAction("粘贴")
        edit_menu.addAction("剪切")

        # 设置中心内容显示
        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle("我是窗口标题")
    w.show()
    app.exec()
```

```python
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton("确定", self)
        ok_btn.setGeometry(50, 50, 100, 30)
```
