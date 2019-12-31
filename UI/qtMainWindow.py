# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Ross\Documents\Programming\Python\BriskBuilder\UI\qtMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName("winMain")
        winMain.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(winMain.sizePolicy().hasHeightForWidth())
        winMain.setSizePolicy(sizePolicy)
        winMain.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        winMain.setTabShape(QtWidgets.QTabWidget.Rounded)
        winMain.setDockNestingEnabled(True)
        winMain.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(winMain)
        self.centralwidget.setObjectName("centralwidget")
        self.twMain = QtWidgets.QTabWidget(self.centralwidget)
        self.twMain.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.twMain.setObjectName("twMain")
        self.tabBuilds = QtWidgets.QWidget()
        self.tabBuilds.setMaximumSize(QtCore.QSize(394, 474))
        self.tabBuilds.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabBuilds.setObjectName("tabBuilds")
        self.scrollArea = QtWidgets.QScrollArea(self.tabBuilds)
        self.scrollArea.setGeometry(QtCore.QRect(1, 1, 393, 473))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 391, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.twMain.addTab(self.tabBuilds, "")
        self.tabNewBuild = QtWidgets.QWidget()
        self.tabNewBuild.setObjectName("tabNewBuild")
        self.lblBuildName = QtWidgets.QLabel(self.tabNewBuild)
        self.lblBuildName.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBuildName.setFont(font)
        self.lblBuildName.setObjectName("lblBuildName")
        self.lblBuildLanguage = QtWidgets.QLabel(self.tabNewBuild)
        self.lblBuildLanguage.setGeometry(QtCore.QRect(10, 70, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBuildLanguage.setFont(font)
        self.lblBuildLanguage.setObjectName("lblBuildLanguage")
        self.lblCommand = QtWidgets.QLabel(self.tabNewBuild)
        self.lblCommand.setGeometry(QtCore.QRect(10, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCommand.setFont(font)
        self.lblCommand.setObjectName("lblCommand")
        self.btnAddBuild = QtWidgets.QPushButton(self.tabNewBuild)
        self.btnAddBuild.setGeometry(QtCore.QRect(140, 420, 120, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnAddBuild.setFont(font)
        self.btnAddBuild.setObjectName("btnAddBuild")
        self.tbCommandString = QtWidgets.QPlainTextEdit(self.tabNewBuild)
        self.tbCommandString.setGeometry(QtCore.QRect(10, 170, 374, 231))
        self.tbCommandString.setObjectName("tbCommandString")
        self.tbBuildName = QtWidgets.QLineEdit(self.tabNewBuild)
        self.tbBuildName.setGeometry(QtCore.QRect(10, 40, 374, 20))
        self.tbBuildName.setObjectName("tbBuildName")
        self.cbLanguage = QtWidgets.QComboBox(self.tabNewBuild)
        self.cbLanguage.setGeometry(QtCore.QRect(10, 100, 374, 22))
        self.cbLanguage.setObjectName("cbLanguage")
        self.btnNewLanguage = QtWidgets.QPushButton(self.tabNewBuild)
        self.btnNewLanguage.setGeometry(QtCore.QRect(294, 70, 91, 23))
        self.btnNewLanguage.setObjectName("btnNewLanguage")
        self.twMain.addTab(self.tabNewBuild, "")
        winMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(winMain)
        self.twMain.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        _translate = QtCore.QCoreApplication.translate
        winMain.setWindowTitle(_translate("winMain", "Brisk Builder"))
        self.twMain.setTabText(self.twMain.indexOf(self.tabBuilds), _translate("winMain", "Builds"))
        self.tabNewBuild.setAccessibleName(_translate("winMain", "Add New Build"))
        self.lblBuildName.setText(_translate("winMain", "Build Name"))
        self.lblBuildLanguage.setText(_translate("winMain", "Programming Language"))
        self.lblCommand.setText(_translate("winMain", "Command String"))
        self.btnAddBuild.setText(_translate("winMain", "Create New Build"))
        self.btnNewLanguage.setText(_translate("winMain", "New Language"))
        self.twMain.setTabText(self.twMain.indexOf(self.tabNewBuild), _translate("winMain", "Create New Build"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winMain = QtWidgets.QMainWindow()
    ui = Ui_winMain()
    ui.setupUi(winMain)
    winMain.show()
    sys.exit(app.exec_())
