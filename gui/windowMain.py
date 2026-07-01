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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
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
        self.active_page = QWidget()
        self.active_page.setObjectName(u"active_page")
        self.gridLayout = QGridLayout(self.active_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.active_addV = QPushButton(self.active_page)
        self.active_addV.setObjectName(u"active_addV")

        self.gridLayout.addWidget(self.active_addV, 1, 0, 1, 1)

        self.active_box = QPushButton(self.active_page)
        self.active_box.setObjectName(u"active_box")

        self.gridLayout.addWidget(self.active_box, 0, 1, 1, 1)

        self.active_video = QPushButton(self.active_page)
        self.active_video.setObjectName(u"active_video")

        self.gridLayout.addWidget(self.active_video, 2, 0, 1, 1)

        self.active_DLV = QPushButton(self.active_page)
        self.active_DLV.setObjectName(u"active_DLV")

        self.gridLayout.addWidget(self.active_DLV, 2, 1, 1, 1)

        self.active_getVideo = QPushButton(self.active_page)
        self.active_getVideo.setObjectName(u"active_getVideo")

        self.gridLayout.addWidget(self.active_getVideo, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.active_page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.active_page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.active_count = QPushButton(self.active_page)
        self.active_count.setObjectName(u"active_count")

        self.gridLayout.addWidget(self.active_count, 3, 1, 1, 1)

        self.actionPage.addWidget(self.active_page)
        self.other_page = QWidget()
        self.other_page.setObjectName(u"other_page")
        self.gridLayout_4 = QGridLayout(self.other_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.setting = QPushButton(self.other_page)
        self.setting.setObjectName(u"setting")

        self.gridLayout_4.addWidget(self.setting, 0, 0, 1, 1)

        self.exit = QPushButton(self.other_page)
        self.exit.setObjectName(u"exit")

        self.gridLayout_4.addWidget(self.exit, 1, 0, 1, 1)

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

        self.dBar.setStretch(0, 3)
        self.dBar.setStretch(1, 2)

        self.verticalLayout.addLayout(self.dBar)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        windowMain.setCentralWidget(self.centralwidget)
        self.status = QStatusBar(windowMain)
        self.status.setObjectName(u"status")
        windowMain.setStatusBar(self.status)

        self.retranslateUi(windowMain)

        self.actionPage.setCurrentIndex(0)


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
        self.active_addV.setText(QCoreApplication.translate("windowMain", u"\u6dfb\u52a0\u89c6\u9891", None))
        self.active_box.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6", None))
        self.active_video.setText(QCoreApplication.translate("windowMain", u"\u89c6\u9891\u64cd\u4f5c", None))
        self.active_DLV.setText(QCoreApplication.translate("windowMain", u"\u4e0b\u8f7d\u89c6\u9891", None))
        self.active_getVideo.setText(QCoreApplication.translate("windowMain", u"\u83b7\u53d6\u89c6\u9891", None))
        self.pushButton_2.setText(QCoreApplication.translate("windowMain", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("windowMain", u"PushButton", None))
        self.active_count.setText(QCoreApplication.translate("windowMain", u"\u7edf\u8ba1", None))
        self.setting.setText(QCoreApplication.translate("windowMain", u"\u8bbe\u7f6e", None))
        self.exit.setText(QCoreApplication.translate("windowMain", u"\u9000\u51fa", None))
        self.active_cPage.setText(QCoreApplication.translate("windowMain", u"\u6d3b\u52a8", None))
        self.other_cPage.setText(QCoreApplication.translate("windowMain", u"\u5176\u4ed6", None))
        self.pic.setText("")
    # retranslateUi

