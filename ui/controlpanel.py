# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ControlPanel.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControlPanelMW(object):
    def setupUi(self, ControlPanelMW):
        ControlPanelMW.setObjectName("ControlPanelMW")
        ControlPanelMW.resize(603, 471)
        self.centralwidget = QtWidgets.QWidget(ControlPanelMW)
        self.centralwidget.setObjectName("centralwidget")
        self.gridlayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")
        self.saveAll = QtWidgets.QPushButton(self.centralwidget)
        self.saveAll.setObjectName("saveAll")
        self.gridlayout.addWidget(self.saveAll, 3, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.freqPinM1 = QtWidgets.QLineEdit(self.groupBox)
        self.freqPinM1.setObjectName("freqPinM1")
        self.gridLayout_2.addWidget(self.freqPinM1, 1, 0, 1, 1)
        self.lowPinM1 = QtWidgets.QLineEdit(self.groupBox)
        self.lowPinM1.setObjectName("lowPinM1")
        self.gridLayout_2.addWidget(self.lowPinM1, 0, 1, 1, 1)
        self.highPinM1 = QtWidgets.QLineEdit(self.groupBox)
        self.highPinM1.setInputMask("")
        self.highPinM1.setObjectName("highPinM1")
        self.gridLayout_2.addWidget(self.highPinM1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.saveMotor1 = QtWidgets.QPushButton(self.groupBox)
        self.saveMotor1.setObjectName("saveMotor1")
        self.verticalLayout.addWidget(self.saveMotor1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.loadAll = QtWidgets.QPushButton(self.centralwidget)
        self.loadAll.setObjectName("loadAll")
        self.gridlayout.addWidget(self.loadAll, 4, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.highPinM2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.highPinM2.setObjectName("highPinM2")
        self.gridLayout_9.addWidget(self.highPinM2, 0, 0, 1, 1)
        self.lowPinM2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lowPinM2.setObjectName("lowPinM2")
        self.gridLayout_9.addWidget(self.lowPinM2, 0, 1, 1, 1)
        self.freqPinM2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.freqPinM2.setObjectName("freqPinM2")
        self.gridLayout_9.addWidget(self.freqPinM2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_9)
        self.saveMotor2 = QtWidgets.QPushButton(self.groupBox_2)
        self.saveMotor2.setObjectName("saveMotor2")
        self.verticalLayout_2.addWidget(self.saveMotor2)
        self.gridlayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.input2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.input2.setObjectName("input2")
        self.gridLayout_14.addWidget(self.input2, 0, 1, 1, 1)
        self.input3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.input3.setObjectName("input3")
        self.gridLayout_14.addWidget(self.input3, 1, 0, 1, 1)
        self.input4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.input4.setObjectName("input4")
        self.gridLayout_14.addWidget(self.input4, 1, 1, 1, 1)
        self.input1 = QtWidgets.QLineEdit(self.groupBox_4)
        self.input1.setObjectName("input1")
        self.gridLayout_14.addWidget(self.input1, 0, 0, 1, 1)
        self.input5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.input5.setObjectName("input5")
        self.gridLayout_14.addWidget(self.input5, 2, 0, 1, 1)
        self.input6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.input6.setObjectName("input6")
        self.gridLayout_14.addWidget(self.input6, 2, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_14)
        self.saveSensor = QtWidgets.QPushButton(self.groupBox_4)
        self.saveSensor.setObjectName("saveSensor")
        self.verticalLayout_6.addWidget(self.saveSensor)
        self.gridlayout.addWidget(self.groupBox_4, 0, 1, 2, 1)
        ControlPanelMW.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlPanelMW)
        QtCore.QMetaObject.connectSlotsByName(ControlPanelMW)
        ControlPanelMW.setTabOrder(self.highPinM1, self.lowPinM1)
        ControlPanelMW.setTabOrder(self.lowPinM1, self.saveMotor1)
        ControlPanelMW.setTabOrder(self.saveMotor1, self.highPinM2)
        ControlPanelMW.setTabOrder(self.highPinM2, self.lowPinM2)
        ControlPanelMW.setTabOrder(self.lowPinM2, self.saveMotor2)
        ControlPanelMW.setTabOrder(self.saveMotor2, self.input1)
        ControlPanelMW.setTabOrder(self.input1, self.input2)
        ControlPanelMW.setTabOrder(self.input2, self.input3)
        ControlPanelMW.setTabOrder(self.input3, self.input4)
        ControlPanelMW.setTabOrder(self.input4, self.saveSensor)
        ControlPanelMW.setTabOrder(self.saveSensor, self.saveAll)
        ControlPanelMW.setTabOrder(self.saveAll, self.loadAll)

    def retranslateUi(self, ControlPanelMW):
        _translate = QtCore.QCoreApplication.translate
        ControlPanelMW.setWindowTitle(_translate("ControlPanelMW", "ControlPanel"))
        self.saveAll.setText(_translate("ControlPanelMW", "Save All Config"))
        self.groupBox.setTitle(_translate("ControlPanelMW", "Motor 1"))
        self.freqPinM1.setPlaceholderText(_translate("ControlPanelMW", "Freq"))
        self.lowPinM1.setPlaceholderText(_translate("ControlPanelMW", "Low Pin"))
        self.highPinM1.setPlaceholderText(_translate("ControlPanelMW", "High Pin"))
        self.saveMotor1.setText(_translate("ControlPanelMW", "Save"))
        self.loadAll.setText(_translate("ControlPanelMW", "Load Current Config"))
        self.groupBox_2.setTitle(_translate("ControlPanelMW", "Motor 2"))
        self.highPinM2.setPlaceholderText(_translate("ControlPanelMW", "High Pin"))
        self.lowPinM2.setPlaceholderText(_translate("ControlPanelMW", "Low Pin"))
        self.freqPinM2.setPlaceholderText(_translate("ControlPanelMW", "Freq"))
        self.saveMotor2.setText(_translate("ControlPanelMW", "Save"))
        self.groupBox_4.setTitle(_translate("ControlPanelMW", "Sensor Group"))
        self.input2.setPlaceholderText(_translate("ControlPanelMW", "Sensor 2 Pin"))
        self.input3.setPlaceholderText(_translate("ControlPanelMW", "Sensor 3 Pin"))
        self.input4.setPlaceholderText(_translate("ControlPanelMW", "Sensor 4 Pin"))
        self.input1.setPlaceholderText(_translate("ControlPanelMW", "Sensor 1 Pin"))
        self.input5.setPlaceholderText(_translate("ControlPanelMW", "Sensor 5 Pin"))
        self.input6.setPlaceholderText(_translate("ControlPanelMW", "Sensor 6 Pin"))
        self.saveSensor.setText(_translate("ControlPanelMW", "Save"))

