import vtk
import volume_tfsetup


from PySide2 import QtWidgets, QtCore
from PyQt5 import QtCore, QtGui, uic, QtWidgets

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Model(QtWidgets.QWidget):

        def __init__(self, path, toggle, parent):
            super(Model,self).__init__(parent)

            interactor = QVTKRenderWindowInteractor(self)
            self.layout = QtWidgets.QHBoxLayout()
            self.layout.addWidget(interactor)
            self.layout.setContentsMargins(0, 0, 0, 0)
            self.setLayout(self.layout)

            renderer = vtk.vtkRenderer()
            render_window = interactor.GetRenderWindow()
            render_window.AddRenderer(renderer)

            interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
            render_window.SetInteractor(interactor)

            reader = vtk.vtkDICOMImageReader()
            reader.SetDirectoryName(path + "/")

            volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
            volumeMapper.SetInputConnection(reader.GetOutputPort())
            volumeMapper.SetBlendModeToComposite()

            volumeColor = vtk.vtkColorTransferFunction()
            volumeScalarOpacity = vtk.vtkPiecewiseFunction()
            volumeGradientOpacity = vtk.vtkPiecewiseFunction()

            if toggle == 1:
                volume_tfsetup.brxtraction(volumeColor,volumeScalarOpacity,volumeGradientOpacity)
            else:
                volume_tfsetup.skinextraction(volumeColor,volumeScalarOpacity,volumeGradientOpacity)

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


            renderer.AddViewProp(volume)
            renderer.ResetCamera()


            self.interactor = interactor
            self.renderer = renderer


        def start(self):
             self.interactor.Initialize()
             self.interactor.Start()