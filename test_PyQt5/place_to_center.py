from PyQt5.QtWidgets import QDesktopWidget

def center_on_screen(window):
    window_geometry = window.frameGeometry()
    screen_center = QDesktopWidget().availableGeometry().center()
    window_geometry.moveCenter(screen_center)
    window.move(window_geometry.topLeft())
