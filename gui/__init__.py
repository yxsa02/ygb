from PySide6 import QtCore, QtWidgets
import threading, time, sys
from .main import mainWindow
from core import app, data

class guiApp(threading.Thread):
    def __init__(self, activity:app.activity):
        super().__init__()
        self.activity = activity
        self.daemon = False  # 设置为守护线程，这样主线程退出时，子线程也会随之退出
    def run(self):
        self.app = QtWidgets.QApplication([])
        self.Wmain = mainWindow(self.activity)
        self.Wmain.show()
        sys.exit(self.app.exec())
