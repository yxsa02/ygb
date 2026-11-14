# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_windowMain(object):
    def setupUi(self, windowMain):
        if not windowMain.objectName():
            windowMain.setObjectName(u"windowMain")
        windowMain.resize(450, 450)
        windowMain.setMinimumSize(QSize(450, 450))
        self.centralwidget = QWidget(windowMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.uBar = QHBoxLayout()
        self.uBar.setObjectName(u"uBar")
        self.list = QListWidget(self.centralwidget)
        self.list.setObjectName(u"list")

        self.uBar.addWidget(self.list)

        self.action = QVBoxLayout()
        self.action.setObjectName(u"action")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.custom_cPage = QPushButton(self.centralwidget)
        self.custom_cPage.setObjectName(u"custom_cPage")

        self.horizontalLayout_3.addWidget(self.custom_cPage)

        self.action_cPage = QPushButton(self.centralwidget)
        self.action_cPage.setObjectName(u"action_cPage")

        self.horizontalLayout_3.addWidget(self.action_cPage)


        self.action.addLayout(self.horizontalLayout_3)

        self.actionPage = QStackedWidget(self.centralwidget)
        self.actionPage.setObjectName(u"actionPage")
        self.actionPage.setMaximumSize(QSize(200, 16777215))
        self.custom_page = QWidget()
        self.custom_page.setObjectName(u"custom_page")
        self.gridLayout_2 = QGridLayout(self.custom_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.custom_1 = QPushButton(self.custom_page)
        self.custom_1.setObjectName(u"custom_1")

        self.gridLayout_2.addWidget(self.custom_1, 1, 1, 1, 1)

        self.custom_2 = QPushButton(self.custom_page)
        self.custom_2.setObjectName(u"custom_2")

        self.gridLayout_2.addWidget(self.custom_2, 2, 0, 1, 1)

        self.custom_4 = QPushButton(self.custom_page)
        self.custom_4.setObjectName(u"custom_4")

        self.gridLayout_2.addWidget(self.custom_4, 3, 0, 1, 1)

        self.custom_0 = QPushButton(self.custom_page)
        self.custom_0.setObjectName(u"custom_0")

        self.gridLayout_2.addWidget(self.custom_0, 1, 0, 1, 1)

        self.custom_5 = QPushButton(self.custom_page)
        self.custom_5.setObjectName(u"custom_5")

        self.gridLayout_2.addWidget(self.custom_5, 3, 1, 1, 1)

        self.custom_6 = QPushButton(self.custom_page)
        self.custom_6.setObjectName(u"custom_6")

        self.gridLayout_2.addWidget(self.custom_6, 4, 0, 1, 1)

        self.custom_3 = QPushButton(self.custom_page)
        self.custom_3.setObjectName(u"custom_3")

        self.gridLayout_2.addWidget(self.custom_3, 2, 1, 1, 1)

        self.custom_7 = QPushButton(self.custom_page)
        self.custom_7.setObjectName(u"custom_7")

        self.gridLayout_2.addWidget(self.custom_7, 4, 1, 1, 1)

        self.custom_8 = QPushButton(self.custom_page)
        self.custom_8.setObjectName(u"custom_8")

        self.gridLayout_2.addWidget(self.custom_8, 5, 0, 1, 1)

        self.custom_9 = QPushButton(self.custom_page)
        self.custom_9.setObjectName(u"custom_9")

        self.gridLayout_2.addWidget(self.custom_9, 5, 1, 1, 1)

        self.actionPage.addWidget(self.custom_page)
        self.action_page = QWidget()
        self.action_page.setObjectName(u"action_page")
        self.gridLayout_3 = QGridLayout(self.action_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.action_remove = QPushButton(self.action_page)
        self.action_remove.setObjectName(u"action_remove")

        self.gridLayout_3.addWidget(self.action_remove, 0, 0, 1, 1)

        self.action_save = QPushButton(self.action_page)
        self.action_save.setObjectName(u"action_save")

        self.gridLayout_3.addWidget(self.action_save, 2, 0, 1, 1)

        self.action_clear = QPushButton(self.action_page)
        self.action_clear.setObjectName(u"action_clear")

        self.gridLayout_3.addWidget(self.action_clear, 0, 1, 1, 1)

        self.action_choseAll = QPushButton(self.action_page)
        self.action_choseAll.setObjectName(u"action_choseAll")

        self.gridLayout_3.addWidget(self.action_choseAll, 1, 0, 1, 1)

        self.action_2 = QPushButton(self.action_page)
        self.action_2.setObjectName(u"action_2")

        self.gridLayout_3.addWidget(self.action_2, 1, 1, 1, 1)

        self.action_open = QPushButton(self.action_page)
        self.action_open.setObjectName(u"action_open")

        self.gridLayout_3.addWidget(self.action_open, 2, 1, 1, 1)

        self.actionPage.addWidget(self.action_page)
        self.active_page_sea = QWidget()
        self.active_page_sea.setObjectName(u"active_page_sea")
        self.formLayout_2 = QFormLayout(self.active_page_sea)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.keyword = QLineEdit(self.active_page_sea)
        self.keyword.setObjectName(u"keyword")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.keyword)

        self.label = QLabel(self.active_page_sea)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.active_page_sea)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.ps_1 = QSpinBox(self.active_page_sea)
        self.ps_1.setObjectName(u"ps_1")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.ps_1)

        self.label_3 = QLabel(self.active_page_sea)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.pn_1 = QSpinBox(self.active_page_sea)
        self.pn_1.setObjectName(u"pn_1")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.pn_1)

        self.btnGV_2 = QPushButton(self.active_page_sea)
        self.btnGV_2.setObjectName(u"btnGV_2")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.btnGV_2)

        self.btnBox_2 = QPushButton(self.active_page_sea)
        self.btnBox_2.setObjectName(u"btnBox_2")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.btnBox_2)

        self.btnGet_2 = QPushButton(self.active_page_sea)
        self.btnGet_2.setObjectName(u"btnGet_2")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.btnGet_2)

        self.btnGetNext_2 = QPushButton(self.active_page_sea)
        self.btnGetNext_2.setObjectName(u"btnGetNext_2")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.btnGetNext_2)

        self.actionPage.addWidget(self.active_page_sea)
        self.active_page_hs = QWidget()
        self.active_page_hs.setObjectName(u"active_page_hs")
        self.formLayout_4 = QFormLayout(self.active_page_hs)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.btnGV_3 = QPushButton(self.active_page_hs)
        self.btnGV_3.setObjectName(u"btnGV_3")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.btnGV_3)

        self.btnBox_3 = QPushButton(self.active_page_hs)
        self.btnBox_3.setObjectName(u"btnBox_3")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.btnBox_3)

        self.btnGet_3 = QPushButton(self.active_page_hs)
        self.btnGet_3.setObjectName(u"btnGet_3")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.LabelRole, self.btnGet_3)

        self.btnGetNext_3 = QPushButton(self.active_page_hs)
        self.btnGetNext_3.setObjectName(u"btnGetNext_3")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.FieldRole, self.btnGetNext_3)

        self.label_7 = QLabel(self.active_page_hs)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.active_page_hs)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(self.active_page_hs)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.pn_3 = QSpinBox(self.active_page_hs)
        self.pn_3.setObjectName(u"pn_3")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pn_3)

        self.ps_3 = QSpinBox(self.active_page_hs)
        self.ps_3.setObjectName(u"ps_3")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.ps_3)

        self.label_10 = QLabel(self.active_page_hs)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.maxId = QLineEdit(self.active_page_hs)
        self.maxId.setObjectName(u"maxId")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.maxId)

        self.wiewAt = QLineEdit(self.active_page_hs)
        self.wiewAt.setObjectName(u"wiewAt")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.wiewAt)

        self.actionPage.addWidget(self.active_page_hs)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.formLayout_8 = QFormLayout(self.page)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.btnGV_8 = QPushButton(self.page)
        self.btnGV_8.setObjectName(u"btnGV_8")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.btnGV_8)

        self.btnBox_8 = QPushButton(self.page)
        self.btnBox_8.setObjectName(u"btnBox_8")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.btnBox_8)

        self.btnGetNext_8 = QPushButton(self.page)
        self.btnGetNext_8.setObjectName(u"btnGetNext_8")

        self.formLayout_8.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btnGetNext_8)

        self.btnGet_8 = QPushButton(self.page)
        self.btnGet_8.setObjectName(u"btnGet_8")

        self.formLayout_8.setWidget(2, QFormLayout.ItemRole.LabelRole, self.btnGet_8)

        self.actionPage.addWidget(self.page)
        self.active_page_bvid = QWidget()
        self.active_page_bvid.setObjectName(u"active_page_bvid")
        self.formLayout = QFormLayout(self.active_page_bvid)
        self.formLayout.setObjectName(u"formLayout")
        self.btnGV_1 = QPushButton(self.active_page_bvid)
        self.btnGV_1.setObjectName(u"btnGV_1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.btnGV_1)

        self.label1 = QLabel(self.active_page_bvid)
        self.label1.setObjectName(u"label1")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.bvid = QLineEdit(self.active_page_bvid)
        self.bvid.setObjectName(u"bvid")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.bvid)

        self.btnGet_1 = QPushButton(self.active_page_bvid)
        self.btnGet_1.setObjectName(u"btnGet_1")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.btnGet_1)

        self.btnBox_1 = QPushButton(self.active_page_bvid)
        self.btnBox_1.setObjectName(u"btnBox_1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.btnBox_1)

        self.btnGetNext_1 = QPushButton(self.active_page_bvid)
        self.btnGetNext_1.setObjectName(u"btnGetNext_1")
        self.btnGetNext_1.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.btnGetNext_1)

        self.label_4 = QLabel(self.active_page_bvid)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.ps_2 = QSpinBox(self.active_page_bvid)
        self.ps_2.setObjectName(u"ps_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.ps_2)

        self.actionPage.addWidget(self.active_page_bvid)
        self.other_page = QWidget()
        self.other_page.setObjectName(u"other_page")
        self.gridLayout_4 = QGridLayout(self.other_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.exit = QPushButton(self.other_page)
        self.exit.setObjectName(u"exit")

        self.gridLayout_4.addWidget(self.exit, 2, 0, 1, 1)

        self.setting = QPushButton(self.other_page)
        self.setting.setObjectName(u"setting")

        self.gridLayout_4.addWidget(self.setting, 1, 0, 1, 1)

        self.igs = QComboBox(self.other_page)
        self.igs.setObjectName(u"igs")

        self.gridLayout_4.addWidget(self.igs, 0, 0, 1, 1)

        self.actionPage.addWidget(self.other_page)

        self.action.addWidget(self.actionPage)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.active_cPage = QPushButton(self.centralwidget)
        self.active_cPage.setObjectName(u"active_cPage")

        self.horizontalLayout_4.addWidget(self.active_cPage)

        self.other_cPage = QPushButton(self.centralwidget)
        self.other_cPage.setObjectName(u"other_cPage")

        self.horizontalLayout_4.addWidget(self.other_cPage)


        self.action.addLayout(self.horizontalLayout_4)


        self.uBar.addLayout(self.action)

        self.uBar.setStretch(0, 3)

        self.verticalLayout.addLayout(self.uBar)

        self.dBar = QHBoxLayout()
        self.dBar.setObjectName(u"dBar")
        self.info = QListWidget(self.centralwidget)
        self.info.setObjectName(u"info")

        self.dBar.addWidget(self.info)

        self.pic = QLabel(self.centralwidget)
        self.pic.setObjectName(u"pic")
        self.pic.setMaximumSize(QSize(200, 200))

        self.dBar.addWidget(self.pic)

        self.dBar.setStretch(0, 1)
        self.dBar.setStretch(1, 1)

        self.verticalLayout.addLayout(self.dBar)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        windowMain.setCentralWidget(self.centralwidget)
        self.status = QStatusBar(windowMain)
        self.status.setObjectName(u"status")
        windowMain.setStatusBar(self.status)

        self.retranslateUi(windowMain)

        self.actionPage.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(windowMain)
    # setupUi

    def retranslateUi(self, windowMain):
        windowMain.setWindowTitle(QCoreApplication.translate("windowMain", u"YGB\u63a7\u5236\u53f0", None))
        self.custom_cPage.setText(QCoreApplication.translate("windowMain", u"\u81ea\u5b9a\u4e49", None))
        self.action_cPage.setText(QCoreApplication.translate("windowMain", u"\u64cd\u4f5c", None))
        self.custom_1.setText(QCoreApplication.translate("windowMain", u"1", None))
        self.custom_2.setText(QCoreApplication.translate("windowMain", u"2", None))
        self.custom_4.setText(QCoreApplication.translate("windowMain", u"4", None))
        self.custom_0.setText(QCoreApplication.translate("windowMain", u"0", None))
        self.custom_5.setText(QCoreApplication.translate("windowMain", u"5", None))
        self.custom_6.setText(QCoreApplication.translate("windowMain", u"6", None))
        self.custom_3.setText(QCoreApplication.translate("windowMain", u"3", None))
        self.custom_7.setText(QCoreApplication.translate("windowMain", u"7", None))
        self.custom_8.setText(QCoreApplication.translate("windowMain", u"8", None))
        self.custom_9.setText(QCoreApplication.translate("windowMain", u"9", None))
        self.action_remove.setText(QCoreApplication.translate("windowMain", u"\u5220\u9664", None))
        self.action_save.setText(QCoreApplication.translate("windowMain", u"\u4fdd\u5b58", None))
        self.action_clear.setText(QCoreApplication.translate("windowMain", u"\u6e05\u7a7a", None))
        self.action_choseAll.setText(QCoreApplication.translate("windowMain", u"\u5168\u9009", None))
        self.action_2.setText(QCoreApplication.translate("windowMain", u"PushButton", None))
        self.action_open.setText(QCoreApplication.translate("windowMain", u"\u6253\u5f00", None))
        self.label.setText(QCoreApplication.translate("windowMain", u"keyword", None))
        self.label_2.setText(QCoreApplication.translate("windowMain", u"ps", None))
        self.label_3.setText(QCoreApplication.translate("windowMain", u"pn", None))
        self.btnGV_2.setText(QCoreApplication.translate("windowMain", u"\u9009\u62e9\u6e20\u9053", None))
        self.btnBox_2.setText(QCoreApplication.translate("windowMain", u"Box", None))
        self.btnGet_2.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6", None))
        self.btnGetNext_2.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6\u4e0b\u4e00\u4e2a", None))
        self.btnGV_3.setText(QCoreApplication.translate("windowMain", u"\u9009\u62e9\u6e20\u9053", None))
        self.btnBox_3.setText(QCoreApplication.translate("windowMain", u"Box", None))
        self.btnGet_3.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6", None))
        self.btnGetNext_3.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6\u4e0b\u4e00\u4e2a", None))
        self.label_7.setText(QCoreApplication.translate("windowMain", u"maxId", None))
        self.label_8.setText(QCoreApplication.translate("windowMain", u"ps", None))
        self.label_9.setText(QCoreApplication.translate("windowMain", u"pn", None))
        self.label_10.setText(QCoreApplication.translate("windowMain", u"viewAt", None))
        self.btnGV_8.setText(QCoreApplication.translate("windowMain", u"\u9009\u62e9\u6e20\u9053", None))
        self.btnBox_8.setText(QCoreApplication.translate("windowMain", u"Box", None))
        self.btnGetNext_8.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6\u4e0b\u4e00\u4e2a", None))
        self.btnGet_8.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6", None))
        self.btnGV_1.setText(QCoreApplication.translate("windowMain", u"\u9009\u62e9\u6e20\u9053", None))
        self.label1.setText(QCoreApplication.translate("windowMain", u"bvid", None))
        self.btnGet_1.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6", None))
        self.btnBox_1.setText(QCoreApplication.translate("windowMain", u"Box", None))
        self.btnGetNext_1.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6\u4e0b\u4e00\u4e2a", None))
        self.label_4.setText(QCoreApplication.translate("windowMain", u"ps", None))
        self.exit.setText(QCoreApplication.translate("windowMain", u"\u9000\u51fa", None))
        self.setting.setText(QCoreApplication.translate("windowMain", u"\u8bbe\u7f6e", None))
        self.active_cPage.setText(QCoreApplication.translate("windowMain", u"\u6d3b\u52a8", None))
        self.other_cPage.setText(QCoreApplication.translate("windowMain", u"\u5176\u4ed6", None))
        self.pic.setText("")
    # retranslateUi

