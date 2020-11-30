# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1269, 706)
        MainWindow.setStyleSheet(u"background-color:rgb(250,250,250)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(0,100,200);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toogle = QFrame(self.Top_Bar)
        self.frame_toogle.setObjectName(u"frame_toogle")
        self.frame_toogle.setMaximumSize(QSize(70, 40))
        self.frame_toogle.setStyleSheet(u"\n"
"	background-color: rgb(85, 170, 255);")
        self.frame_toogle.setFrameShape(QFrame.StyledPanel)
        self.frame_toogle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_toogle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toogle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.horizontalLayout_3.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toogle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(233,237,242);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.Btn_Menu_1 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setObjectName(u"Btn_Menu_1")
        self.Btn_Menu_1.setEnabled(True)
        self.Btn_Menu_1.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_1.setStyleSheet(u"QPushButton {\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75,76,78);\n"
"	border-radius: 10px ;\n"
"} \n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"} ")

        self.verticalLayout_3.addWidget(self.Btn_Menu_1)

        self.Btn_Menu_2 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setObjectName(u"Btn_Menu_2")
        self.Btn_Menu_2.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_2.setStyleSheet(u"QPushButton {\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75,76,78);\n"
"	border-radius: 10px ;\n"
"} \n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"} ")

        self.verticalLayout_3.addWidget(self.Btn_Menu_2)

        self.Btn_Menu_3 = QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setObjectName(u"Btn_Menu_3")
        self.Btn_Menu_3.setMinimumSize(QSize(0, 40))
        self.Btn_Menu_3.setStyleSheet(u"QPushButton {\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(75,76,78);\n"
"	border-radius: 10px ;\n"
"} \n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(85, 170, 255);\n"
"} ")

        self.verticalLayout_3.addWidget(self.Btn_Menu_3)


        self.verticalLayout_2.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.Pages_Widget.setStyleSheet(u"background-color: rgb(250,250,250);\n"
"")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMaximumSize(QSize(1111111, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ToolTable = QTableWidget(self.frame_2)
        if (self.ToolTable.columnCount() < 10):
            self.ToolTable.setColumnCount(10)
        if (self.ToolTable.rowCount() < 10):
            self.ToolTable.setRowCount(10)
        self.ToolTable.setObjectName(u"ToolTable")
        self.ToolTable.setMaximumSize(QSize(1111111, 16777215))
        self.ToolTable.setStyleSheet(u"background-color: rgb(233,237,242);")
        self.ToolTable.setRowCount(10)
        self.ToolTable.setColumnCount(10)

        self.horizontalLayout_5.addWidget(self.ToolTable)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 0))
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ListToolType = QListWidget(self.frame_3)
        self.ListToolType.setObjectName(u"ListToolType")

        self.verticalLayout_6.addWidget(self.ListToolType)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 300))
        self.label_2.setPixmap(QPixmap(u"drill.jpg"))

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.DelBtn = QPushButton(self.frame)
        self.DelBtn.setObjectName(u"DelBtn")

        self.horizontalLayout_4.addWidget(self.DelBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.ResetBtn = QPushButton(self.frame)
        self.ResetBtn.setObjectName(u"ResetBtn")

        self.horizontalLayout_4.addWidget(self.ResetBtn)

        self.SaveBtn = QPushButton(self.frame)
        self.SaveBtn.setObjectName(u"SaveBtn")

        self.horizontalLayout_4.addWidget(self.SaveBtn)

        self.horizontalSpacer_2 = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 90, 181, 41))
        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.Pages_Widget.addWidget(self.page_3)

        self.verticalLayout_4.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"TOOGLE", None))
        self.Btn_Menu_1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a", None))
        self.Btn_Menu_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.Btn_Menu_3.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText("")
        self.DelBtn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u0443\u044e \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.ResetBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043d\u0435\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.SaveBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

