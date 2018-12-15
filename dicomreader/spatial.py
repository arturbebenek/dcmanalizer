import vtk
import volume_tfsetup


#from PySide2 import QtWidgets, QtCore
from PyQt5 import Qt

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Model(Qt.QMainWindow):

        def __init__(self, path, parent = None):
            Qt.QMainWindow.__init__(self, parent)

            self.frame = Qt.QFrame()
            self.vl = Qt.QVBoxLayout()

            self.vtkWidget = QVTKRenderWindowInteractor()
            self.vl.addWidget(self.vtkWidget)
            self.ren = vtk.vtkRenderer()
            self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
            self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

            reader = vtk.vtkDICOMImageReader()
            reader.SetDirectoryName(path + "/")

            volumeMapper = vtk.vtkOpenGLGPUVolumeRayCastMapper()
            volumeMapper.SetInputConnection(reader.GetOutputPort())
            volumeMapper.SetBlendModeToComposite()

            volumeColor = vtk.vtkColorTransferFunction()
            volumeScalarOpacity = vtk.vtkPiecewiseFunction()
            volumeGradientOpacity = vtk.vtkPiecewiseFunction()

            volume_tfsetup.brxtraction(volumeColor,volumeScalarOpacity,volumeGradientOpacity)
            #volume_tfsetup.skinextraction(volumeColor,volumeScalarOpacity,volumeGradientOpacity)

            volumeProperty = vtk.vtkVolumeProperty()
            volumeProperty.SetColor(volumeColor)
            volumeProperty.SetScalarOpacity(volumeScalarOpacity)
            volumeProperty.SetGradientOpacity(volumeGradientOpacity)
            volumeProperty.SetInterpolationTypeToLinear()
            volumeProperty.ShadeOn()
            volumeProperty.SetAmbient(0.5)
            volumeProperty.SetDiffuse(0.3)
            volumeProperty.SetSpecular(0.6)

            volume = vtk.vtkVolume()
            volume.SetMapper(volumeMapper)
            volume.SetProperty(volumeProperty)

            self.ren.AddViewProp(volume)
            self.ren.ResetCamera()

            self.frame.setLayout(self.vl)
            self.setCentralWidget(self.frame)

            self.show()
            self.iren.Initialize()
            self.iren.Start()


