from gui import windowMain
from PySide6 import QtWidgets, QtGui, QtCore
from types import SimpleNamespace
from typing import TYPE_CHECKING
from core.t import dl_pic
if TYPE_CHECKING:
    import core.app

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self,activity:"core.app.activity"):
        super().__init__()
        self.ui = windowMain.Ui_windowMain()
        self.activity = activity
        self.ui.setupUi(self)
        self.nowUseGetActionPage = "aw"
        self.ui.list.itemChanged.connect(self.onListItemChanged)
        self.ui.list.itemClicked.connect(lambda item: self.activity.addTask("info",{"key":item.data(QtCore.Qt.ItemDataRole.UserRole)}))
        self.ui.custom_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(0))
        self.ui.action_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(1))
        self.ui.active_cPage.clicked.connect(lambda: self.toggleGetActionPage(None))
        self.ui.other_cPage.clicked.connect(lambda: self.ui.actionPage.setCurrentIndex(6))
        self.ui.exit.clicked.connect(lambda: self.close())
        self.buttonSignalConnect()
        self.setStatus()
        self.setMenu()
        #self.updateList()
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
        action_collect = QtGui.QAction("收藏", self)
        action_like = QtGui.QAction("like", self)
        action_coin = QtGui.QAction("coin", self)
        self.menu.vAction.addActions([action_collect, action_like, action_coin])
        self.menu.vGetF = QtWidgets.QMenu(self)
        action_afterWatch = QtGui.QAction("稍后再看",self)
        action_afterWatch.triggered.connect(lambda: self.toggleGetActionPage("aw"))
        action_videoGS = QtGui.QAction("推送",self)
        action_videoGS.triggered.connect(lambda: self.toggleGetActionPage("vg"))
        action_chosedBox = QtGui.QAction("选中的Box",self)
        action_chosedBox.triggered.connect(lambda: self.toggleGetActionPage("box"))
        action_history = QtGui.QAction("观看历史",self)
        action_history.triggered.connect(lambda: self.toggleGetActionPage("hs"))
        action_bvid = QtGui.QAction("bvid",self)
        action_bvid.triggered.connect(lambda: self.toggleGetActionPage("iu"))
        self.menu.vGetF.addActions([action_chosedBox,action_afterWatch,action_history,action_videoGS,action_bvid])
    def closeEvent(self,event:QtGui.QCloseEvent):
        self.activity.addTask("exit")
        event.accept()
    def buttonSignalConnect(self):
        self.ui.action_choseAll.clicked.connect(lambda: self.activity.itemGroups().choose())
        self.ui.action_clear.clicked.connect(lambda: self.activity.itemGroups().clear())
        self.ui.action_remove.clicked.connect(lambda: self.activity.itemGroups().delete())
        self.ui.action_open.clicked.connect(lambda: self.activity.itemGroups().delete())
        self.ui.action_save.clicked.connect(lambda: self.activity.itemGroups().delete())
        self.ui.btnGV_1.clicked.connect(lambda: self.menu.vGetF.exec(QtGui.QCursor.pos()))
        self.ui.btnGV_2.clicked.connect(lambda: self.menu.vGetF.exec(QtGui.QCursor.pos()))
        self.ui.btnGV_3.clicked.connect(lambda: self.menu.vGetF.exec(QtGui.QCursor.pos()))
        self.ui.btnGV_8.clicked.connect(lambda: self.menu.vGetF.exec(QtGui.QCursor.pos()))
        self.ui.action_clear.clicked.connect(lambda: (self.activity.itemGroups().clear(),self.updateList()))
        self.ui.action_remove.clicked.connect(lambda: (self.activity.itemGroups().delete(),self.updateList()))
        self.ui.btnGet_1.clicked.connect(lambda: self.bvidActionGet())
        self.ui.setting.clicked.connect(lambda: self.activity.addTask("test"))
        self.ui.btnGet_2.clicked.connect(lambda: self.activity.addTask("seav",{"keyword":self.ui.keyword.text(),"ps":self.ui.ps_2.value()}))
        #self.ui.btnGetNext_2.clicked.connect(lambda: self.activity.addTask("gvbh",{"ps":self.ui.ps_2.value()}))
        #self.ui.action_open.clicked.connect(lambda: self.activity.action.getVideoByBvid({"bvid":self.ui.action_bvid.text()}))
    def chan(self):
        pass
    def updateList(self) -> None:
        self.ui.list.clear()
        group = self.activity.itemGroups()
        keys = group.getAll(0)          # 主键列表
        titles = group.getAll("title")  # 标题列表
        chosen_keys = set(group.getChosen(0))  # 已选中主键集合
        for key, title in zip(keys, titles):
            item = QtWidgets.QListWidgetItem(title)
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            item.setData(QtCore.Qt.ItemDataRole.UserRole, key)
            if key in chosen_keys:
                item.setCheckState(QtCore.Qt.CheckState.Checked)
            else:
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.ui.list.addItem(item)
    def toggleGetActionPage(self,type:str|None):
        if type == None:
            type = self.nowUseGetActionPage
        if type == "aw":
            self.ui.actionPage.setCurrentIndex(2)
            self.nowUseGetActionPage = "aw"
        elif type == "hs":
            self.ui.actionPage.setCurrentIndex(3)
            self.nowUseGetActionPage = "hs"
        elif type == "box":
            self.ui.actionPage.setCurrentIndex(4)
            self.nowUseGetActionPage = "box"
        elif type == "iu":
            self.ui.bvid.setEnabled(True)
            self.ui.actionPage.setCurrentIndex(5)
            self.nowUseGetActionPage = "iu"
        elif type == "vg":
            self.ui.bvid.setEnabled(False)
            self.ui.actionPage.setCurrentIndex(5)
            self.nowUseGetActionPage = "vg"
    def bvidActionGet(self):
        if self.nowUseGetActionPage == "vg":
            self.activity.addTask("gvbh",{"ps":self.ui.ps_2.value()})
        elif self.nowUseGetActionPage == "iu":
            self.activity.addTask("gvbi",{"bvid":self.ui.bvid.text()})
    def onListItemChanged(self, item):
        key = item.data(QtCore.Qt.ItemDataRole.UserRole)
        checked = item.checkState() == QtCore.Qt.CheckState.Checked
        # 这里直接同步到 itemGroups()
        self.activity.itemGroups().choose(key, checked)
    def showpic(self, url):
        # 显示封面 - 使用QLabel
        image_data = QtCore.QByteArray(dl_pic(url))
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image_data)
        # 缩放图片到合适大小（可选）
        scaled_pixmap = pixmap.scaled(self.ui.pic.width(),self.ui.pic.height(),QtGui.Qt.AspectRatioMode.KeepAspectRatio,QtGui.Qt.TransformationMode.SmoothTransformation)
        self.ui.pic.setPixmap(scaled_pixmap)
        self.ui.pic.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)