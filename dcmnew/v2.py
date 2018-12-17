from __future__ import print_function
import os
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import spatial
import volume_tfsetup
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

        self.vtk_widget = DicomViewer(self.ui.vtk_panel)
        self.ui.vtk_layout = QtWidgets.QHBoxLayout()
        self.ui.vtk_layout.addWidget(self.vtk_widget)
        self.ui.vtk_layout.setContentsMargins(0,0,0,0)
        self.ui.vtk_panel.setLayout(self.ui.vtk_layout)
        self.ui.ReadBtn.clicked.connect(self.setExistingDirectory)

        #self.ui.threshold_slider.setValue(50)
   #     self.ui.threshold_slider.valueChanged.connect(self.vtk_widget.set_threshold)
    #    self.vtk_widget.arrow_picked.connect(self.update_magnitude)

    def initialize(self):
        self.vtk_widget.start()

    def setExistingDirectory(self):
        global path
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.patient_label.setText(info.DicInfo(path).patientname + "\n" + info.DicInfo(path).patientid
                                      + "\n" + info.DicInfo(path).modality + "\n" + info.DicInfo(path).studydate
                                      + "\n" + info.DicInfo(path).pixeldata + "\n" + info.DicInfo(path).pixelspacing)




class DicomViewer(QtWidgets.QWidget):
    #arrow_picked = QtCore.pyqtSignal(float)


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
        self.interactor = interactor

    def start(self):
        self.interactor.Initialize()
        self.interactor.Start()


    def set_threshold(self, new_value):
        float_value = new_value/100.0
        print(float_value)
        self.threshold.ThresholdByUpper(float_value)
        self.render_window.Render()

    def process_pick(self, object, event):
        point_id = object.GetPointId()
        if point_id >= 0:
            vector_magnitude = self.glyphs.GetOutput().GetPointData().GetScalars().GetTuple(point_id)
            self.arrow_picked.emit(vector_magnitude[0])

    def click_to_pick(self, object, event):
        x, y = object.GetEventPosition()
        self.picker.Pick(x,y,0, self.renderer)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    main_window = DicomViewerApp()
    main_window.show()
    main_window.initialize()
    app.exec_()
