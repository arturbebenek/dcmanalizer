
from PySide2 import QtGui, QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):
    '''Main window lets user know when window was clicked on non-widget space'''
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.initUI()
    def initUI(self):
        self.myLabel=TalkingQLabel("Don't mess with Breakfast!", self)
        self.myLabel.setGeometry(50, 50, 200, 120)
        self.setGeometry(300,200,300,250)
        self.show()
    def mousePressEvent(self, event):
        print ("Well, you pressed in main window!")

class TalkingQLabel(QtWidgets.QLabel):
    '''QLab el that indicates when it was pressed'''
    def __init__(self, txt, parent):
        QtWidgets.QLabel.__init__(self, txt, parent)
        self.initUI()
    def initUI(self):
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("QLabel { color: rgb(255, 255, 0); font-size: 15px; background-color: rgb(0,0,0)}")
    def mousePressEvent(self, event):
        print ("This time you pressed in a label")

def main():
    import sys
    qtApp=QtWidgets.QApplication(sys.argv)
    myTalker=MainWindow()
    sys.exit(qtApp.exec_())

if __name__=="__main__":
    main()