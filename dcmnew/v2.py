from __future__ import print_function
import os
import sys
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import spatial
import spatial2
import single
import info

class DicomViewerApp(QtWidgets.QMainWindow):
    def __init__(self):

        #Parent constructor
        super(DicomViewerApp,self).__init__()
        self.vtk_widget = None
        self.ui = None
        self.setup()

    def setup(self):
        import v2_ui
        self.ui = v2_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.vtk_widget = axial(self.ui.vtk_panel)
        #self.vtk_widget = DicomViewer(self.ui.vtk_panel)
        #self.vtk_widget = single.SingleView(self.ui.vtk_panel, "F:/MRI Brain Scan/Series 8")

        self.ui.vtk_layout = QtWidgets.QHBoxLayout()
        self.ui.vtk_layout.addWidget(self.vtk_widget)
        self.ui.vtk_layout.setContentsMargins(0,0,0,0)
        self.ui.vtk_panel.setLayout(self.ui.vtk_layout)

        self.ui.ReadBtn.clicked.connect(self.setExistingDirectory)
        self.ui.GenerateBtn.clicked.connect(self.generate3d)
        self.ui.SingleBtn.clicked.connect(self.singleview)
        self.ui.MultiBtn.clicked.connect(self.multiView)

        self.createActions()
        self.ui.menuInfo.addAction(self.aboutAct)
        self.ui.menuHelp.addAction(self.aboutQtAct)


        self.ui.checkBox_inside.setChecked(True)
        self.buttongroup = QtWidgets.QButtonGroup()
        self.buttongroup.addButton(self.ui.checkBox_skin, 2)
        self.buttongroup.addButton(self.ui.checkBox_inside, 1)
        #self.ui.threshold_slider.setValue(50)
   #     self.ui.threshold_slider.valueChanged.connect(self.vtk_widget.set_threshold)
    #    self.vtk_widget.arrow_picked.connect(self.update_magnitude)

    def initialize(self):
        self.vtk_widget.start()

    def setExistingDirectory(self):
        global path
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if path == '':
            sys.exit()
        filelist = os.listdir(path)
        for a in range(0,len(filelist)):
            if filelist[a].endswith('.dcm') == True:
                self.ui.patient_label.setText(info.DicInfo(path).patientname + "\n" + info.DicInfo(path).patientid
                                      + "\n" + info.DicInfo(path).modality + "\n" + info.DicInfo(path).studydate
                                      + "\n" + info.DicInfo(path).pixeldata + "\n" + info.DicInfo(path).pixelspacing)
            else:
                self.errorhandler()

    def errorhandler(self):
        loadhandle = QtWidgets.QMessageBox.question(self, 'ERROR', "No valid format, select directory only with .dcm files, "
                                                                   "try again?",QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Yes)
        if loadhandle == QtWidgets.QMessageBox.Yes:
            self.setExistingDirectory()
        else:
            sys.exit()

    def generate3d(self):
        toggle = self.buttongroup.checkedId()
#        self.projection = spatial.Model(path,toggle)

        self.vtk_widget.close()
        self.vtk_widget.destroy()
        self.vtk_widget = spatial2.Model(path, toggle, self.ui.vtk_panel)
        self.vtk_widget.start()
        self.ui.vtk_layout.addWidget(self.vtk_widget)
        self.ui.vtk_layout.update()

    def singleview(self):
        print('clicked')
        self.vtk_widget.close()
        self.vtk_widget.destroy()
       # self.vtk_widget.setParent(None)

        self.ui.vtk_panel.update()
        #self.vtk_widget = DicomViewer(self.ui.vtk_panel)
        self.vtk_widget = single.SingleView(self.ui.vtk_panel, path)
        self.vtk_widget.start()
        self.ui.vtk_layout.addWidget(self.vtk_widget)
       # self.ui.vtk_layout.addWidget(self.new_widget)
      #  self.new_widget = single.SingleView(self.ui.vtk_panel,path)
       # self.ui.vtk_layout.addWidget(self.new_widget)


        self.ui.vtk_layout.update()
        # self.vtk_widget = single.SingleView(path,self.ui)
       # self.ui.vtk_layout.addWidget(self.vtk_widget)
       # self.vtk_widget.start()

    def multiView(self):
        self.vtk_widget.close()
        self.vtk_widget.destroy()
       # self.vtk_widget.setParent(None)
        self.vtk_widget = axial(self.ui.vtk_panel)
        self.ui.vtk_layout.addWidget(self.vtk_widget)
        self.ui.vtk_layout.update()

    def createActions(self):
        self.aboutAct = QtWidgets.QAction("&Info", self,
                statusTip ="Show the application's Info box",
                triggered =self.about)

        self.aboutQtAct = QtWidgets.QAction("About &Qt", self,
                statusTip= "Show the Qt library's About box",
                triggered= QtWidgets.qApp.aboutQt)

    def about(self):
         QtWidgets.QMessageBox.about(self, "About Application",
                                "The <b>Application</b> was made to manage dicom datasets "
                                "using different way of views and 3d visualisation. "
                                "This is beta version")



class DicomViewer(QtWidgets.QWidget):


    def __init__(self, parent):
        super(DicomViewer,self).__init__(parent)

        # Make tha actual QtWidget a child so that it can be re parented
        interactor = QVTKRenderWindowInteractor(self)
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(interactor)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Setup VTK environment
        renderer = vtk.vtkRenderer()
        render_window = interactor.GetRenderWindow()
        render_window.AddRenderer(renderer)

        interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        render_window.SetInteractor(interactor)
        renderer.SetBackground(0.2,0.2,0.2)

        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)

        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        renderer.AddActor(actor)

        self.interactor = interactor
        self.renderer = renderer


    def start(self):
        self.interactor.Initialize()
        self.interactor.Start()
        #self.interactor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, self.click_to_pick, 10)

class axial(QtWidgets.QLabel):
    def __init__(self, parent):
        super(axial,self).__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        self.pixmap = QtGui.QPixmap('mri.jpg')
        self.setPixmap(self.pixmap)



if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    main_window = DicomViewerApp()
    main_window.show()
    #main_window.initialize()
    app.exec_()
