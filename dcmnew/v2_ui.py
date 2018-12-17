# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Art\Documents\python\dcmnew\v2_ui.ui',
# licensing of 'C:\Users\Art\Documents\python\dcmnew\v2_ui.ui' applies.
#
# Created: Sun Dec 16 23:57:59 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
#from PySide2 import QtCore, QtGui, QtWidgets
import info

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.central_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ReadBtn = QtWidgets.QPushButton(self.frame)
        self.ReadBtn.setObjectName("ReadBtn")
        self.verticalLayout.addWidget(self.ReadBtn)
        self.SingleBtn = QtWidgets.QPushButton(self.frame)
        self.SingleBtn.setObjectName("SingleBtn")
        self.verticalLayout.addWidget(self.SingleBtn)
        self.MultiBtn = QtWidgets.QPushButton(self.frame)
        self.MultiBtn.setObjectName("MultiBtn")
        self.verticalLayout.addWidget(self.MultiBtn)
        self.GenerateBtn = QtWidgets.QPushButton(self.frame)
        self.GenerateBtn.setObjectName("GenerateBtn")
        self.verticalLayout.addWidget(self.GenerateBtn)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.patient_label = QtWidgets.QLabel(self.frame)
        self.patient_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patient_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.patient_label.setObjectName("patient_label")
        self.verticalLayout.addWidget(self.patient_label)
        self.vtk_panel = QtWidgets.QFrame(self.splitter)
        self.vtk_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vtk_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vtk_panel.setObjectName("vtk_panel")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.vtk_panel)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(30, 510, 211, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DicomViewer", None, -1))
        self.ReadBtn.setText(QtWidgets.QApplication.translate("MainWindow", "ReadDirectory", None, -1))
        self.SingleBtn.setText(QtWidgets.QApplication.translate("MainWindow", "SingleView", None, -1))
        self.MultiBtn.setText(QtWidgets.QApplication.translate("MainWindow", "MultiView", None, -1))
        self.GenerateBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Generate", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "Skin and Bones", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("MainWindow", "Inside", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.patient_label.setText(QtWidgets.QApplication.translate("MainWindow", "<No Directory Added>", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.menuInfo.setTitle(QtWidgets.QApplication.translate("MainWindow", "Info", None, -1))

