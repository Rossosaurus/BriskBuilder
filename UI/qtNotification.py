# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ross\Documents\Programming\Python\BriskBuilder\UI\qtNotification.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winNotif(object):
    def setupUi(self, winNotif):
        winNotif.setObjectName("winNotif")
        winNotif.resize(230, 159)
        self.widget = QtWidgets.QWidget(winNotif)
        self.widget.setObjectName("widget")
        self.lblTitle = QtWidgets.QLabel(self.widget)
        self.lblTitle.setGeometry(QtCore.QRect(10, 10, 211, 21))
        self.lblTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.btnOk = QtWidgets.QPushButton(self.widget)
        self.btnOk.setGeometry(QtCore.QRect(78, 100, 75, 23))
        self.btnOk.setObjectName("btnOk")
        self.lblMessage = QtWidgets.QLabel(self.widget)
        self.lblMessage.setGeometry(QtCore.QRect(10, 30, 211, 61))
        self.lblMessage.setText("")
        self.lblMessage.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        winNotif.setCentralWidget(self.widget)

        self.retranslateUi(winNotif)
        QtCore.QMetaObject.connectSlotsByName(winNotif)

    def retranslateUi(self, winNotif):
        _translate = QtCore.QCoreApplication.translate
        winNotif.setWindowTitle(_translate("winNotif", "Notification"))
        self.lblTitle.setText(_translate("winNotif", "<html><head/><body><p>Message:</p></body></html>"))
        self.btnOk.setText(_translate("winNotif", "OK"))
