# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sait_\Desktop\Road_Surface_Damage_Detection_System\Road-Surface-Damage-Detection-System\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.setEnabled(True)
        mainWin.resize(991, 698)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWin.sizePolicy().hasHeightForWidth())
        mainWin.setSizePolicy(sizePolicy)
        mainWin.setMinimumSize(QtCore.QSize(100, 100))
        mainWin.setBaseSize(QtCore.QSize(100, 100))
        mainWin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(mainWin)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.oriImage = QtWidgets.QLabel(self.centralwidget)
        self.oriImage.setGeometry(QtCore.QRect(60, 30, 640, 360))
        self.oriImage.setMouseTracking(True)
        self.oriImage.setStyleSheet("background : grey\n"
"")
        self.oriImage.setText("")
        self.oriImage.setObjectName("oriImage")
        self.trackImage = QtWidgets.QLabel(self.centralwidget)
        self.trackImage.setGeometry(QtCore.QRect(730, 30, 200, 360))
        self.trackImage.setStyleSheet("background : grey\n"
"")
        self.trackImage.setText("")
        self.trackImage.setObjectName("trackImage")
        self.meshOnOff = QtWidgets.QPushButton(self.centralwidget)
        self.meshOnOff.setGeometry(QtCore.QRect(770, 430, 100, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.meshOnOff.setFont(font)
        self.meshOnOff.setIconSize(QtCore.QSize(40, 40))
        self.meshOnOff.setObjectName("meshOnOff")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 450, 421, 191))
        self.listWidget.setObjectName("listWidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 430, 81, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 430, 81, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 430, 101, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 430, 81, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 20))
        self.menubar.setObjectName("menubar")
        mainWin.setMenuBar(self.menubar)

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "main"))
        self.meshOnOff.setText(_translate("mainWin", "  Mesh"))
        self.label_4.setText(_translate("mainWin", "Hasar Derecesi"))
        self.label_5.setText(_translate("mainWin", "Hasar Derinliği"))
        self.label_6.setText(_translate("mainWin", "Araca Olan Mesafe"))
        self.label_7.setText(_translate("mainWin", "No"))
