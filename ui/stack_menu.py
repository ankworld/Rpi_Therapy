# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/stack_menu.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_main = QtWidgets.QLabel(self.page_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_main.sizePolicy().hasHeightForWidth())
        self.title_main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_main.setFont(font)
        self.title_main.setScaledContents(False)
        self.title_main.setAlignment(QtCore.Qt.AlignCenter)
        self.title_main.setWordWrap(False)
        self.title_main.setObjectName("title_main")
        self.verticalLayout_2.addWidget(self.title_main)
        self.btn_auto = QtWidgets.QPushButton(self.page_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_auto.sizePolicy().hasHeightForWidth())
        self.btn_auto.setSizePolicy(sizePolicy)
        self.btn_auto.setObjectName("btn_auto")
        self.verticalLayout_2.addWidget(self.btn_auto)
        self.btn_man = QtWidgets.QPushButton(self.page_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_man.sizePolicy().hasHeightForWidth())
        self.btn_man.setSizePolicy(sizePolicy)
        self.btn_man.setObjectName("btn_man")
        self.verticalLayout_2.addWidget(self.btn_man)
        self.btn_shutdown = QtWidgets.QPushButton(self.page_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_shutdown.sizePolicy().hasHeightForWidth())
        self.btn_shutdown.setSizePolicy(sizePolicy)
        self.btn_shutdown.setAutoFillBackground(False)
        self.btn_shutdown.setStyleSheet("QPushButton {\n"
"color: rgb(255,255,255);\n"
"background : rgb(239, 41, 41)\n"
"}")
        self.btn_shutdown.setFlat(False)
        self.btn_shutdown.setObjectName("btn_shutdown")
        self.verticalLayout_2.addWidget(self.btn_shutdown)
        self.stackedWidget.addWidget(self.page_main)
        self.page_auto_profile = QtWidgets.QWidget()
        self.page_auto_profile.setObjectName("page_auto_profile")
        self.gridLayout = QtWidgets.QGridLayout(self.page_auto_profile)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_auto_back = QtWidgets.QPushButton(self.page_auto_profile)
        self.btn_auto_back.setObjectName("btn_auto_back")
        self.gridLayout.addWidget(self.btn_auto_back, 6, 0, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.page_auto_profile)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 3, 0, 1, 1)
        self.tbv_profile = QtWidgets.QTableView(self.page_auto_profile)
        self.tbv_profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tbv_profile.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tbv_profile.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbv_profile.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbv_profile.setGridStyle(QtCore.Qt.SolidLine)
        self.tbv_profile.setObjectName("tbv_profile")
        self.gridLayout.addWidget(self.tbv_profile, 2, 0, 1, 2)
        self.btn_del = QtWidgets.QPushButton(self.page_auto_profile)
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.btn_del, 3, 1, 1, 1)
        self.btn_sel = QtWidgets.QPushButton(self.page_auto_profile)
        self.btn_sel.setObjectName("btn_sel")
        self.gridLayout.addWidget(self.btn_sel, 6, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.page_auto_profile)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)
        self.line_1 = QtWidgets.QFrame(self.page_auto_profile)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.gridLayout.addWidget(self.line_1, 1, 0, 1, 2)
        self.title_profile = QtWidgets.QLabel(self.page_auto_profile)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_profile.setFont(font)
        self.title_profile.setAlignment(QtCore.Qt.AlignCenter)
        self.title_profile.setObjectName("title_profile")
        self.gridLayout.addWidget(self.title_profile, 0, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_auto_profile)
        self.page_auto_add = QtWidgets.QWidget()
        self.page_auto_add.setObjectName("page_auto_add")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_auto_add)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb_spd = QtWidgets.QComboBox(self.page_auto_add)
        self.cb_spd.setObjectName("cb_spd")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.cb_spd.addItem("")
        self.gridLayout_2.addWidget(self.cb_spd, 2, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.page_auto_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 3, 0, 1, 1)
        self.btn_add_con = QtWidgets.QPushButton(self.page_auto_add)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_con.sizePolicy().hasHeightForWidth())
        self.btn_add_con.setSizePolicy(sizePolicy)
        self.btn_add_con.setObjectName("btn_add_con")
        self.gridLayout_2.addWidget(self.btn_add_con, 3, 1, 1, 1)
        self.lbl_s2 = QtWidgets.QLabel(self.page_auto_add)
        self.lbl_s2.setObjectName("lbl_s2")
        self.gridLayout_2.addWidget(self.lbl_s2, 1, 0, 1, 1)
        self.cb_s1 = QtWidgets.QComboBox(self.page_auto_add)
        self.cb_s1.setObjectName("cb_s1")
        self.cb_s1.addItem("")
        self.cb_s1.addItem("")
        self.cb_s1.addItem("")
        self.cb_s1.addItem("")
        self.cb_s1.addItem("")
        self.gridLayout_2.addWidget(self.cb_s1, 0, 1, 1, 1)
        self.lbl_spd = QtWidgets.QLabel(self.page_auto_add)
        self.lbl_spd.setObjectName("lbl_spd")
        self.gridLayout_2.addWidget(self.lbl_spd, 2, 0, 1, 1)
        self.cb_s2 = QtWidgets.QComboBox(self.page_auto_add)
        self.cb_s2.setObjectName("cb_s2")
        self.cb_s2.addItem("")
        self.cb_s2.addItem("")
        self.cb_s2.addItem("")
        self.cb_s2.addItem("")
        self.cb_s2.addItem("")
        self.gridLayout_2.addWidget(self.cb_s2, 1, 1, 1, 1)
        self.lbl_s1 = QtWidgets.QLabel(self.page_auto_add)
        self.lbl_s1.setObjectName("lbl_s1")
        self.gridLayout_2.addWidget(self.lbl_s1, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_auto_add)
        self.page_man = QtWidgets.QWidget()
        self.page_man.setObjectName("page_man")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_man)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_man = QtWidgets.QLabel(self.page_man)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_man.setFont(font)
        self.title_man.setAlignment(QtCore.Qt.AlignCenter)
        self.title_man.setObjectName("title_man")
        self.verticalLayout_3.addWidget(self.title_man)
        self.btn_man_s1 = QtWidgets.QPushButton(self.page_man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_man_s1.sizePolicy().hasHeightForWidth())
        self.btn_man_s1.setSizePolicy(sizePolicy)
        self.btn_man_s1.setObjectName("btn_man_s1")
        self.verticalLayout_3.addWidget(self.btn_man_s1)
        self.btn_man_s2 = QtWidgets.QPushButton(self.page_man)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_man_s2.sizePolicy().hasHeightForWidth())
        self.btn_man_s2.setSizePolicy(sizePolicy)
        self.btn_man_s2.setObjectName("btn_man_s2")
        self.verticalLayout_3.addWidget(self.btn_man_s2)
        self.spb_speed = QtWidgets.QSpinBox(self.page_man)
        self.spb_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.spb_speed.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spb_speed.setMaximum(100)
        self.spb_speed.setSingleStep(5)
        self.spb_speed.setProperty("value", 50)
        self.spb_speed.setObjectName("spb_speed")
        self.verticalLayout_3.addWidget(self.spb_speed)
        self.btn_man_back = QtWidgets.QPushButton(self.page_man)
        self.btn_man_back.setObjectName("btn_man_back")
        self.verticalLayout_3.addWidget(self.btn_man_back)
        self.stackedWidget.addWidget(self.page_man)
        self.page_process = QtWidgets.QWidget()
        self.page_process.setObjectName("page_process")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_process)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.page_process)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 2)
        self.lbl_time = QtWidgets.QLabel(self.page_process)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.gridLayout_3.addWidget(self.lbl_time, 0, 0, 1, 2)
        self.pg_bar = QtWidgets.QProgressBar(self.page_process)
        self.pg_bar.setProperty("value", 24)
        self.pg_bar.setObjectName("pg_bar")
        self.gridLayout_3.addWidget(self.pg_bar, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_process)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_auto, self.btn_man)
        MainWindow.setTabOrder(self.btn_man, self.btn_shutdown)
        MainWindow.setTabOrder(self.btn_shutdown, self.tbv_profile)
        MainWindow.setTabOrder(self.tbv_profile, self.btn_auto_back)
        MainWindow.setTabOrder(self.btn_auto_back, self.cb_s1)
        MainWindow.setTabOrder(self.cb_s1, self.cb_s2)
        MainWindow.setTabOrder(self.cb_s2, self.cb_spd)
        MainWindow.setTabOrder(self.cb_spd, self.btn_cancel)
        MainWindow.setTabOrder(self.btn_cancel, self.btn_add_con)
        MainWindow.setTabOrder(self.btn_add_con, self.btn_man_s1)
        MainWindow.setTabOrder(self.btn_man_s1, self.btn_man_s2)
        MainWindow.setTabOrder(self.btn_man_s2, self.btn_man_back)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Therapy"))
        self.title_main.setText(_translate("MainWindow", "Main Menu"))
        self.btn_auto.setText(_translate("MainWindow", "Auto"))
        self.btn_man.setText(_translate("MainWindow", "Manual"))
        self.btn_shutdown.setText(_translate("MainWindow", "Shutdown"))
        self.btn_auto_back.setText(_translate("MainWindow", "Back"))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_del.setText(_translate("MainWindow", "Delete"))
        self.btn_sel.setText(_translate("MainWindow", "Select"))
        self.title_profile.setText(_translate("MainWindow", "Profile"))
        self.cb_spd.setItemText(0, _translate("MainWindow", "50"))
        self.cb_spd.setItemText(1, _translate("MainWindow", "55"))
        self.cb_spd.setItemText(2, _translate("MainWindow", "60"))
        self.cb_spd.setItemText(3, _translate("MainWindow", "65"))
        self.cb_spd.setItemText(4, _translate("MainWindow", "70"))
        self.cb_spd.setItemText(5, _translate("MainWindow", "75"))
        self.cb_spd.setItemText(6, _translate("MainWindow", "80"))
        self.cb_spd.setItemText(7, _translate("MainWindow", "85"))
        self.cb_spd.setItemText(8, _translate("MainWindow", "90"))
        self.cb_spd.setItemText(9, _translate("MainWindow", "95"))
        self.cb_spd.setItemText(10, _translate("MainWindow", "100"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_add_con.setText(_translate("MainWindow", "Add"))
        self.lbl_s2.setText(_translate("MainWindow", "Section 2 (times)"))
        self.cb_s1.setItemText(0, _translate("MainWindow", "0"))
        self.cb_s1.setItemText(1, _translate("MainWindow", "5"))
        self.cb_s1.setItemText(2, _translate("MainWindow", "10"))
        self.cb_s1.setItemText(3, _translate("MainWindow", "15"))
        self.cb_s1.setItemText(4, _translate("MainWindow", "20"))
        self.lbl_spd.setText(_translate("MainWindow", "Speed (%)"))
        self.cb_s2.setItemText(0, _translate("MainWindow", "0"))
        self.cb_s2.setItemText(1, _translate("MainWindow", "5"))
        self.cb_s2.setItemText(2, _translate("MainWindow", "10"))
        self.cb_s2.setItemText(3, _translate("MainWindow", "15"))
        self.cb_s2.setItemText(4, _translate("MainWindow", "20"))
        self.lbl_s1.setText(_translate("MainWindow", "Section 1 (times)"))
        self.title_man.setText(_translate("MainWindow", "Manual Control"))
        self.btn_man_s1.setText(_translate("MainWindow", "Section 1"))
        self.btn_man_s2.setText(_translate("MainWindow", "Section 2"))
        self.btn_man_back.setText(_translate("MainWindow", "Back"))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.lbl_time.setText(_translate("MainWindow", "Time"))
