import vtk
#from PySide2 import QtWidgets,QtCore,QtGui
from PyQt5 import QtWidgets,QtCore

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class SingleView(QtWidgets.QWidget):


    def __init__(self, parent, path, type, imnb, numofdcm):
        super(SingleView,self).__init__(parent)

        interactor = QVTKRenderWindowInteractor(self)
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(interactor)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Setup VTK environment
        renderer = vtk.vtkRenderer()
        render_window = interactor.GetRenderWindow()
        render_window.AddRenderer(renderer)

        interactor.SetInteractorStyle(vtk.vtkInteractorStyleImage())
        render_window.SetInteractor(interactor)

        #add to vtk
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(path + "/")
        #reader.SetDataExtent(0, 256, 0, 256, 1, 62)
        #reader.SetDataSpacing(3.2, 3.2, 1.5)
        reader.SetDataOrigin(0.0, 0.0, 0.0)
        reader.SetDataScalarTypeToUnsignedShort()
        reader.UpdateWholeExtent()


        # Calculate the center of the volume
        reader.Update()
        (xMin, xMax, yMin, yMax, zMin, zMax) = reader.GetExecutive().GetWholeExtent(reader.GetOutputInformation(0))
        (xSpacing, ySpacing, zSpacing) = reader.GetOutput().GetSpacing()
        (x0, y0, z0) = reader.GetOutput().GetOrigin()

        center = [x0 + xSpacing * imnb/numofdcm * (xMin + xMax),
                  y0 + ySpacing * imnb/numofdcm * (yMin + yMax),
                  z0 + zSpacing * imnb/numofdcm * (zMin + zMax)]

        # Matrices for axial, coronal, sagittal, oblique view orientations
        axial = vtk.vtkMatrix4x4()
        axial.DeepCopy((1, 0, 0, center[0],
                0, 1, 0, center[1],
                0, 0, 1, center[2],
                0, 0, 0, 1))

        coronal = vtk.vtkMatrix4x4()
        coronal.DeepCopy((1, 0, 0, center[0],
                  0, 0, 1, center[1],
                  0,-1, 0, center[2],
                  0, 0, 0, 1))

        sagittal = vtk.vtkMatrix4x4()
        sagittal.DeepCopy((0, 0, 1, center[0],
                   0, 1, 0, center[1],
                   1, 0, 0, center[2],
                   0, 0, 0, 1))

        oblique = vtk.vtkMatrix4x4()
        oblique.DeepCopy((1, 0, 0, center[0],
                  0, 0.866025, -0.5, center[1],
                  0, 0.5, 0.866025, center[2],
                  0, 0, 0, 1))

        # Extract a slice in the desired orientation
        reslice = vtk.vtkImageReslice()
        reslice.SetInputConnection(reader.GetOutputPort())
        reslice.SetOutputDimensionality(2)
        if type == 'axial':
            reslice.SetResliceAxes(axial)
        elif type == 'sagittal':
            reslice.SetResliceAxes(sagittal)
        elif type == 'coronal':
            reslice.SetResliceAxes(coronal)
        elif type == 'oblique':
            reslice.SetResliceAxes(oblique)
        reslice.SetInterpolationModeToLinear()

#        Create a greyscale lookup table
        table = vtk.vtkLookupTable()
        table.SetRange(0, 200) # image intensity range
        table.SetValueRange(0.0, 1.0) # from black to white
        table.SetSaturationRange(0.0, 0.0) # no color saturation
        table.SetRampToLinear()
        table.Build()

        # Map the image through the lookup table
        color = vtk.vtkImageMapToColors()
        color.SetLookupTable(table)
        color.SetInputConnection(reslice.GetOutputPort())

        # Display the image
        actor = vtk.vtkImageActor()
        actor.GetMapper().SetInputConnection(color.GetOutputPort())
        renderer.AddActor(actor)

        # Set up the interaction
        interactorStyle = vtk.vtkInteractorStyleImage()
        interactor.SetInteractorStyle(interactorStyle)

        self.interactor = interactor
        self.renderer = renderer
      #  self.reslice = reslice

    def start(self):
  #     self.interactor.Initialize()
       self.interactor.Start()

#    def slidercallback(self,new_value,old_value):
#        print('phot changed')
#        deltaY = new_value - old_value
#        self.reslice.Update()
#        sliceSpacing = self.reslice.GetOutput().GetSpacing()[2]
#        matrix = self.reslice.GetResliceAxes()
#        # move the center point that we are slicing through
#        center = matrix.MultiplyPoint((0, 0, sliceSpacing*deltaY, 1))
#        matrix.SetElement(0, 3, center[0])
#        matrix.SetElement(1, 3, center[1])
#        matrix.SetElement(2, 3, center[2])
#        self.interactor.Start()