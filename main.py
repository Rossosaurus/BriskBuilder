from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from UI.qtMainWindow import Ui_winMain
from UI.qtNewLanguageWindow import Ui_winNL
from UI.qtNotification import Ui_winNotif
import sqlite3
import sys

#Initialize SQLite3
conn = sqlite3.connect('builds.db')
c = conn.cursor()

#Initialize Qt forms
class winMain(QMainWindow): #Initate class winMain as type QMainWindow
    def __init__(self):
        super(winMain, self).__init__() #Run __init__ function of QMainWindow class
        self.uiMain = Ui_winMain() #Set class variable ui equal to the UI class of winMain in qtMainWindow.py
        self.uiMain.setupUi(self) #Run setupUi to initialize mainWin GUI

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
        self.Main.uiMain.btnNewLanguage.clicked.connect(self.openWinNL)

        #winNL connections
        self.NL.uiNL.tbNL.returnPressed.connect(self.addLanguage)
        self.NL.uiNL.btnOkCancel.accepted.connect(self.addLanguage)

        #winNotif connections
        self.Notif.uiNotif.btnOk.clicked.connect(self.notifOK)
    
    #winMain methods
    def openWinNL(self):
        self.NL.show()
    
    #winNL methods
    def addLanguage(self):
        l = self.NL.uiNL.tbNL.text().upper()
        try:
            if l.isalnum:
                c.execute("INSERT OR IGNORE INTO languages (languageName) VALUES (?);", (l,))
                conn.commit()
                self.setMessage(str("The language: " + l + " has successfully been added to the list click OK to return to the previous menu."))
                self.NL.hide()
        except:
            self.setMessage("An error occurred please submit an issue at <a href=\"https://github.com/Rossosaurus/BriskBuilder\">https://github.com/Rossosaurus/BriskBuilder</a>")

            
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