from __future__ import print_function
import os
import sys
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import spatial
import spatial2
import single
import single2
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


        self.ui.horizontalScrollBar.setValue(50)
        self.ui.horizontalScrollBar.update()
        self.ui.horizontalScrollBar.valueChanged.connect(self.dcmchange)

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
        self.typeflag = 0
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

        self.adjustslider()

    def errorhandler(self):
        loadhandle = QtWidgets.QMessageBox.question(self, 'ERROR', "Brak prawidłowego formatu, wybierz folder zawierający jedynie pliki z rozszerzeniem .dcm "
                                                                   "Chcesz spróbować ponownie?",QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Yes)
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
        self.typeflag = 1
        self.vtk_widget.close()
        self.vtk_widget.destroy()
       # self.vtk_widget.setParent(None)
        self.ui.vtk_panel.update()
        self.vtk_widget = single2.SingleView(self.ui.vtk_panel, path, 'axial', self.dcmnumber, self.numofdcms)
        self.vtk_widget.start()
        self.ui.vtk_layout.addWidget(self.vtk_widget)
       # self.ui.vtk_layout.addWidget(self.new_widget)
      #  self.new_widget = single.SingleView(self.ui.vtk_panel,path)
       # self.ui.vtk_layout.addWidget(self.new_widget)
        self.ui.vtk_layout.update()
        #self.ui.horizontalScrollBar.setMinimum = 0;
        #self.ui.horizontalScrollBar.setMaximum = len(info.DicInfo.filelist)
        # self.vtk_widget = single.SingleView(path,self.ui)
       # self.ui.vtk_layout.addWidget(self.vtk_widget)
       # self.vtk_widget.start()

      #  self.typeofwiev = "single"

    def multiView(self):

        self.typeflag = 2
        self.vtk_widget.close()
        self.vtk_widget.destroy()
       # self.vtk_widget.setParent(None)
        self.ui.vtk_panel.update()

        self.axial = single2.SingleView(self.vtk_widget, path, 'axial', self.dcmnumber, self.numofdcms)
        self.axial.start()
        self.sagit = single2.SingleView(self.vtk_widget, path, 'sagittal', self.dcmnumber, self.numofdcms)
        self.sagit.start()
        self.coron = single2.SingleView(self.vtk_widget, path, 'coronal', self.dcmnumber, self.numofdcms)
        self.coron.start()
        self.obliq = single2.SingleView(self.vtk_widget, path, 'oblique', self.dcmnumber, self.numofdcms)
        self.obliq.start()

        self.vtk_widget = QtWidgets.QGroupBox("3 najważniejsze rzuty: ")
        layout2 = QtWidgets.QGridLayout()
        layout2.addWidget(self.axial,0,0)
        layout2.addWidget(self.sagit,0,1)
        layout2.addWidget(self.coron,1,0)
        layout2.addWidget(self.obliq,1,1)

        self.vtk_widget.setLayout(layout2)
        self.vtk_widget.setParent(self.ui.vtk_panel)
        self.ui.vtk_layout.addWidget(self.vtk_widget)
        self.ui.vtk_layout.update()
       #self.adjustslider()
       # self.typeofwiev = "multi"



    def createActions(self):
        self.aboutAct = QtWidgets.QAction("&O aplikacji", self,
                statusTip ="Pokazuje informacje o DicomViewer i jego autorze ",
                triggered =self.about)

        self.aboutQtAct = QtWidgets.QAction("Informacje dotyczące &Qt", self,
                statusTip= "Pokazuje informacje o bibliotece wykorzystanej do tworzenia interfejsu",
                triggered= QtWidgets.qApp.aboutQt)

    def about(self):
         QtWidgets.QMessageBox.about(self, "O aplikacji",
                                "<b>DicomViewer</b> jest aplikacją stworzoną do zarządzaniem zbiorami plików typu dicom"
                                "przy pomocy różnych widoków a także wizualizacji przestrzennej. Jest to projekt inżynierski,"
                                " autorstwa Artura Bębenka")

    def adjustslider(self):
        self.ui.horizontalScrollBar.setMinimum(0)
        self.ui.horizontalScrollBar.setMaximum(len(info.DicInfo(path).filelist))
        self.ui.horizontalScrollBar.setValue(len(info.DicInfo(path).filelist)/2)
        self.numofdcms = len(info.DicInfo(path).filelist)
        self.dcmnumber = self.ui.horizontalScrollBar.value()

    def dcmchange(self, new_value):
        #print(new_value)
        if (self.typeflag != 0):
    #        print(self.typeflag)
            self.dcmnumber = new_value
        if (self.typeflag == 1):
            self.singleview()
        elif (self.typeflag == 2):
            self.multiView()

           # single.SingleView.slidercallback(new_value, self.old_value)
     #   if self.typeofview == "multi":
      #      print ("zmiana obrazka")


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
