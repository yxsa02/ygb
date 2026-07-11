from PySide6 import QtCore, QtGui, QtWidgets
import threading, time, sys
from types import SimpleNamespace
from . import windowMain

class guiApp(threading.Thread):
    def __init__(self, activity):
        super().__init__()
        self.activity = activity
        self.daemon = False  # 设置为守护线程，这样主线程退出时，子线程也会随之退出
    def run(self):
        self.app = QtWidgets.QApplication([])
        self.w = mainWindow(self.activity)
        self.w.show()
        sys.exit(self.app.exec())

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self,activity):
        super().__init__()
        self.ui = windowMain.Ui_windowMain()
        self.activity = activity
        self.ui.setupUi(self)
        self.ui.custom_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(0))
        self.ui.action_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(1))
        self.ui.active_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(2))
        self.ui.other_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(3))
        self.ui.exit.clicked.connect(lambda: self.close())
        self.buttonSignalConnect()
        self.setStatus()
        self.setMenu()
    def setStatus(self):
        self.statusUi = SimpleNamespace()
        self.statusUi.text = QtWidgets.QLabel("")
        self.statusUi.pgb = QtWidgets.QProgressBar()
        self.statusUi.pgb.setMaximum(100)
        self.statusUi.pgb.setFixedWidth(100)
        self.statusUi.pgb.setValue(0)
        self.statusUi.text.setVisible(False)
        self.statusUi.pgb.setVisible(False)
        self.ui.status.addWidget(self.statusUi.text)
        self.statusBar().addPermanentWidget(self.statusUi.pgb)
    def setMenu(self):
        self.menu = SimpleNamespace()
        self.menu.vAction = QtWidgets.QMenu(self)
        actions = QtGui.QAction("收藏", self)
        action_like = QtGui.QAction("like", self)
        action_coin = QtGui.QAction("coin", self)
        self.menu.vAction.addActions([actions, action_like, action_coin])

    def close(self):
        self.activity.addTask("exit")
        return super().close()
    def buttonSignalConnect(self):
        self.ui.action_choseAll.clicked.connect(lambda: self.activity.vi.choose())
        self.ui.action_clear.clicked.connect(lambda: self.activity.vi.clear())
        self.ui.action_remove.clicked.connect(lambda: self.activity.vi.delete())
        self.ui.action_open.clicked.connect(lambda: self.activity.vi.delete())
        self.ui.action_save.clicked.connect(lambda: self.activity.vi.delete())
        self.ui.active_video.clicked.connect(lambda: self.menu.vAction.exec(QtGui.QCursor.pos()))
        self.ui.active_DLV.clicked.connect(lambda: self.activity.addTask("test"))
        #self.ui.action_get.clicked.connect(lambda: self.activity.geter.getVideoByBvid(self.activity.vi.getChosenItem()[0]))


if __name__ == "__main__":
    gui_app = guiApp()
    gui_app.start()
    i = 0
    while True:
        i += 1
        print(i,end="\r")
        time.sleep(1)