# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ross\Documents\Programming\Python\BriskBuilder\UI\qtNewLanguageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winNL(object):
    def setupUi(self, winNL):
        winNL.setObjectName("winNL")
        winNL.resize(320, 70)
        self.centralwidget = QtWidgets.QWidget(winNL)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOkCancel = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.btnOkCancel.setGeometry(QtCore.QRect(10, 40, 300, 23))
        self.btnOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnOkCancel.setObjectName("btnOkCancel")
        self.tbNL = QtWidgets.QLineEdit(self.centralwidget)
        self.tbNL.setGeometry(QtCore.QRect(10, 10, 301, 20))
        self.tbNL.setObjectName("tbNL")
        winNL.setCentralWidget(self.centralwidget)

        self.retranslateUi(winNL)
        QtCore.QMetaObject.connectSlotsByName(winNL)

    def retranslateUi(self, winNL):
        _translate = QtCore.QCoreApplication.translate
        winNL.setWindowTitle(_translate("winNL", "Add New Language"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winNL = QtWidgets.QMainWindow()
    ui = Ui_winNL()
    ui.setupUi(winNL)
    winNL.show()
    sys.exit(app.exec_())
