# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Art\Desktop\ui\v1.ui',
# licensing of 'C:\Users\Art\Desktop\ui\v1.ui' applies.
#
# Created: Sun Dec  2 11:31:48 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 300, 121, 261))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(160, 40, 401, 431))
        self.widget.setObjectName("widget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 510, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_2 = QtWidgets.QAction(mainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSingle = QtWidgets.QAction(mainWindow)
        self.actionSingle.setObjectName("actionSingle")
        self.actionMulti = QtWidgets.QAction(mainWindow)
        self.actionMulti.setObjectName("actionMulti")
        self.action3D = QtWidgets.QAction(mainWindow)
        self.action3D.setObjectName("action3D")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_2)
        self.menuView.addAction(self.actionSingle)
        self.menuView.addAction(self.actionMulti)
        self.menuView.addAction(self.action3D)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("mainWindow", "Read Directory", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("mainWindow", "File", None, -1))
        self.menuView.setTitle(QtWidgets.QApplication.translate("mainWindow", "View", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("mainWindow", "Help", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("mainWindow", "SinglePreviev", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("mainWindow", "Open", None, -1))
        self.actionSave_2.setText(QtWidgets.QApplication.translate("mainWindow", "Save", None, -1))
        self.actionSingle.setText(QtWidgets.QApplication.translate("mainWindow", "Single", None, -1))
        self.actionMulti.setText(QtWidgets.QApplication.translate("mainWindow", "Multi", None, -1))
        self.action3D.setText(QtWidgets.QApplication.translate("mainWindow", "3D", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

