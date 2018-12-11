# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Art\Desktop\ui\v1.ui',
# licensing of 'C:\Users\Art\Desktop\ui\v1.ui' applies.
#
# Created: Sun Dec  9 17:52:06 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import info


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ReadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ReadBtn.setGeometry(QtCore.QRect(70, 30, 81, 31))
        self.ReadBtn.setObjectName("ReadBtn")
        self.ReadBtn.clicked.connect(self.setExistingDirectory)


        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 50, 521, 421))
        self.widget.setObjectName("widget")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(220, 520, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.SingleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SingleBtn.setGeometry(QtCore.QRect(30, 110, 81, 41))
        self.SingleBtn.setObjectName("SingleBtn")

        self.GenerateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateBtn.setGeometry(QtCore.QRect(30, 210, 81, 41))
        self.GenerateBtn.setObjectName("GenerateBtn")

        self.MultiBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MultiBtn.setGeometry(QtCore.QRect(30, 160, 81, 41))
        self.MultiBtn.setObjectName("MultiBtn")

        frameStyle = QtWidgets.QFrame.Sunken | QtWidgets.QFrame.Panel
        self.directoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.directoryLabel.setFrameStyle(frameStyle)
        self.directoryLabel.setGeometry(QtCore.QRect(30, 320, 131, 201))
        self.directoryLabel.setObjectName("DicomLabel")

        mainWindow.setCentralWidget(self.centralwidget)

        self.actionSingle = QtWidgets.QAction(mainWindow)
        self.actionSingle.setObjectName("actionSingle")

        self.actionMulti = QtWidgets.QAction(mainWindow)
        self.actionMulti.setObjectName("actionMulti")

        self.action3D = QtWidgets.QAction(mainWindow)
        self.action3D.setObjectName("action3D")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "Dicom Viewer", None, -1))
        self.ReadBtn.setText(QtWidgets.QApplication.translate("mainWindow", "Read Directory", None, -1))
        self.SingleBtn.setText(QtWidgets.QApplication.translate("mainWindow", "Single View", None, -1))
        self.GenerateBtn.setText(QtWidgets.QApplication.translate("mainWindow", "Generate 3D", None, -1))
        self.MultiBtn.setText(QtWidgets.QApplication.translate("mainWindow", "Multi View", None, -1))
        self.actionSingle.setText(QtWidgets.QApplication.translate("mainWindow", "Single", None, -1))
        self.actionMulti.setText(QtWidgets.QApplication.translate("mainWindow", "Multi", None, -1))
        self.action3D.setText(QtWidgets.QApplication.translate("mainWindow", "3D", None, -1))
        self.directoryLabel.setText(QtWidgets.QApplication.translate("mainWindow", "Dicom Label", None, -1))

    def setExistingDirectory(self):
       # options = QtWidgets.QFileDialog.DontResolveSymlinks | QtWidgets.QFileDialog.ShowDirsOnly
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Select Directory"))
        #info.Dicominfo(path)
        self.directoryLabel.setText(info.DicInfo(path).patientname + "\n" + info.DicInfo(path).modality)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

