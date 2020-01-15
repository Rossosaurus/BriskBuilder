from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QPushButton, QScrollArea
from UI.qtMainWindow import Ui_winMain
from UI.qtNewLanguageWindow import Ui_winNL
from UI.qtNotification import Ui_winNotif
import sqlite3, subprocess, sys

#Initialize SQLite3
conn = sqlite3.connect('builds.db')
c = conn.cursor()

#Initialize Qt forms
class winMain(QMainWindow): #Initate class winMain as type QMainWindow
    def __init__(self):
        super(winMain, self).__init__() #Run __init__ function of QMainWindow class
        self.uiMain = Ui_winMain() #Set class variable ui equal to the UI class of winMain in qtMainWindow.py
        self.uiMain.setupUi(self) #Run setupUi to initialize mainWin GUI
        self.uiMain.twMain.setCurrentIndex(0)

class winNL(QMainWindow):
    def __init__(self):
        super(winNL, self).__init__() #Run __init__ function of QMainWindow class
        tbLMask = QtGui.QRegExpValidator(QtCore.QRegExp('^[\w]*\+*\#*$'))
        self.uiNL = Ui_winNL() #Set class variable ui equal to the UI class of winMain in qtMainWindow.py
        self.uiNL.setupUi(self) #Run setupUi to initialize mainWin GUI
        self.uiNL.tbNL.setValidator(tbLMask)

class winNotif(QMainWindow):
    def __init__(self):
        super(winNotif, self).__init__()
        self.uiNotif = Ui_winNotif()
        self.uiNotif.setupUi(self)

class GUI: #Instantiate both classes in single class
    def __init__(self):
        self.Main = winMain()
        self.NL = winNL()
        self.Notif = winNotif()

        #winMain connections
        self.genBuilds()
        self.Main.uiMain.btnNewLanguage.clicked.connect(self.openWinNL)
        self.Main.uiMain.btnAddBuild.clicked.connect(self.addBuild)
        self.Main.uiMain.twMain.currentChanged.connect(self.generateLanguages)
        self.Main.uiMain.twMain.currentChanged.connect(self.genBuilds)
        

        #winNL connections
        self.NL.uiNL.tbNL.returnPressed.connect(self.addLanguage)
        self.NL.uiNL.btnOkCancel.accepted.connect(self.addLanguage)

        #winNotif connections
        self.Notif.uiNotif.btnOk.clicked.connect(self.notifOK)
    
    #winMain methods
    def openWinNL(self):
        self.NL.show()

    def generateLanguages(self):
        self.Main.uiMain.cbLanguage.clear()
        for language in c.execute("SELECT languageName FROM languages ORDER BY languageName ASC"):
            self.Main.uiMain.cbLanguage.addItem(language[0])

    def addBuild(self):
        bName = self.Main.uiMain.tbBuildName.text()
        bLanguage = self.Main.uiMain.cbLanguage.currentText()
        bCommand = self.Main.uiMain.tbCommandString.toPlainText()
        c.execute("INSERT INTO builds VALUES (NULL, ?, ?, ?);", (bName, bLanguage, bCommand))
        conn.commit()
        self.Main.uiMain.twMain.setCurrentIndex(0)
    
    def genBuilds(self):
        scBuilds = QScrollArea()
        scBuilds.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scBuilds.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scBuildsVLB = QVBoxLayout()
        for i in reversed(range(scBuildsVLB.count())):
            scBuildsVLB.itemAt(i).widget().setParent(None)
        for language in c.execute("SELECT languageName FROM languages ORDER BY languageName ASC"):
            gb = QGroupBox(language[0])
            gb.setMinimumSize(360, 50)
            gb.setMaximumWidth(360)
            vlb = QVBoxLayout()
            vlb.setContentsMargins(3,3,3,3)
            vlb.setSpacing(3)
            c1 = conn.cursor()
            for build in c1.execute("SELECT * FROM builds WHERE buildLanguage = ?", (language[0],)):
                print(build)
                frame = QFrame()
                hlb = QHBoxLayout()
                frame.setMaximumSize(360, 20)
                hlb.setContentsMargins(5,0,0,0)
                hlb.setSpacing(6)
                btnBuild = QPushButton("Build")
                btnBuild.setMaximumSize(50, 20)
                btnBuild.clicked.connect(lambda checked, buildID=build[0]: self.runBuild(buildID))
                lblBuildName = QLabel(build[1])
                lblBuildName.setMaximumSize(233,20)
                lblBuildLanguage = QLabel(build[2])
                lblBuildLanguage.setMaximumSize(60, 20)
                hlb.addWidget(lblBuildName)
                hlb.addWidget(lblBuildLanguage)
                hlb.addWidget(btnBuild)
                frame.setLayout(hlb)
                vlb.addWidget(frame)
            gb.setLayout(vlb)
            scBuildsVLB.addWidget(gb)
        scBuildsVLB.addStretch()
        scBuilds.setLayout(scBuildsVLB)
        self.Main.uiMain.gridLayout_2.addChildWidget(scBuilds)

    def runBuild(self, buildID):
        buildName = ""
        buildCommand = ""
        for build in c.execute("SELECT * FROM builds WHERE buildID = ? LIMIT 1", (buildID,)):
            buildName = build[1]
            buildCommand = build[3]
        try:
            subprocess.run("buildCommand")
        except FileNotFoundError:
            self.setMessage("The program you were trying to run could not be found in the specified location. You have probably not included the path to the program however, if you have and you still get this error try adding the program to PATH in your environment variables so you don't need to include the full path or open a an issue on github.")

    #winNL methods
    def addLanguage(self):
        l = self.NL.uiNL.tbNL.text().upper()
        try:
            if l.isalnum:
                c.execute("INSERT OR IGNORE INTO languages (languageName) VALUES (?);", (l,))
                conn.commit()
                self.setMessage(str("The language: " + l + " has successfully been added to the list click OK to return to the previous menu."))
                self.generateLanguages()
                self.NL.hide()
        except:
            self.setMessage("An error occurred please submit an issue at <a href=\"https://github.com/Rossosaurus/BriskBuilder\">https://github.com/Rossosaurus/BriskBuilder</a>")
            self.NL.hide()

            
    #winNotif methods
    def setMessage(self, message):
        self.Notif.uiNotif.lblMessage.setText(message)
        self.Notif.show()
    def notifOK(self):
        self.Notif.hide()

def  main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.Main.show() #Show winMain
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()