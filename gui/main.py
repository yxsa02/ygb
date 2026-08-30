from gui import windowMain
from PySide6 import QtWidgets, QtGui
from types import SimpleNamespace

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
        self.menu.vGetF = QtWidgets.QMenu(self)
        action_afterWatch = QtGui.QAction("稍后再看",self)
        action_afterWatch.checkableChanged.connect(lambda: self.activity.addTask("gvbi"))
        action_videoGS = QtGui.QAction("推送",self)
        action_chosedBox = QtGui.QAction("选中的Box",self)
        self.menu.vGetF.addActions([action_chosedBox,action_afterWatch,action_videoGS])
    def close(self):
        self.activity.addTask("exit")
        return super().close()
    def buttonSignalConnect(self):
        self.ui.action_choseAll.clicked.connect(lambda: self.activity.itemGroups().choose())
        self.ui.action_clear.clicked.connect(lambda: self.activity.itemGroups().clear())
        self.ui.action_remove.clicked.connect(lambda: self.activity.itemGroups().delete())
        self.ui.action_open.clicked.connect(lambda: self.activity.itemGroups().delete())
        self.ui.action_save.clicked.connect(lambda: self.activity.itemGroups().delete())
        self.ui.active_getVideo.clicked.connect(lambda: self.menu.vGetF.exec(QtGui.QCursor.pos()))
        
        self.ui.setting.clicked.connect(lambda: self.activity.addTask("test"))
        self.ui.action_open.clicked.connect(lambda: self.activity.action.getVideoByBvid(self.activity.itemGroups().getChosen()[0]))
    def chan(self):
        pass
    def updateList(self) -> None:
        self.ui.list.clear()
        self.ui.list.addItems(self.activity.i().getAll())
