import vtk
from vtk.util import numpy_support
from PySide2 import QtCore, QtGui, QtWidgets
import numpy
from matplotlib import pyplot, cm

class Singleview(QtWidgets.QWidget):

    def __init__(self, path):
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(path)
        reader.Update()

        # Load dimensions using `GetDataExtent`
        _extent = reader.GetDataExtent()
        ConstPixelDims = [_extent[1] - _extent[0] + 1, _extent[3] - _extent[2] + 1, _extent[5] - _extent[4] + 1]

        # Load spacing values
        ConstPixelSpacing = reader.GetPixelSpacing()

        x = numpy.arange(0.0, (ConstPixelDims[0] + 1) * ConstPixelSpacing[0], ConstPixelSpacing[0])
        y = numpy.arange(0.0, (ConstPixelDims[1] + 1) * ConstPixelSpacing[1], ConstPixelSpacing[1])
        z = numpy.arange(0.0, (ConstPixelDims[2] + 1) * ConstPixelSpacing[2], ConstPixelSpacing[2])

        # Get the 'vtkImageData' object from the reader
        imageData = reader.GetOutput()
        # Get the 'vtkPointData' object from the 'vtkImageData' object
        pointData = imageData.GetPointData()
        # Ensure that only one array exists within the 'vtkPointData' object
        assert (pointData.GetNumberOfArrays() == 1)
        # Get the `vtkArray` (or whatever derived type) which is needed for the `numpy_support.vtk_to_numpy` function
        arrayData = pointData.GetArray(0)

        # vtk usage

        # Convert the `vtkArray` to a NumPy array
        ArrayDicom = numpy_support.vtk_to_numpy(arrayData)
        # Reshape the NumPy array to 3D using 'ConstPixelDims' as a 'shape'
        ArrayDicom = ArrayDicom.reshape(ConstPixelDims, order='F')

        pyplot.axes().set_aspect('equal', 'datalim')
        pyplot.set_cmap(pyplot.gray())
        fig1 = pyplot.pcolormesh(x, y, numpy.flipud(numpy.rot90(ArrayDicom[:, :, 30])))
        pyplot.show(fig1)