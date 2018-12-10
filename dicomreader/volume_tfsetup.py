import vtk
import vtkvolume


def skinextraction():
    vtkvolume.volumeColor.AddRGBPoint(0,    0.0, 0.0, 0.0)
    vtkvolume.volumeColor.AddRGBPoint(100,  1.0, 0.5, 0.3)
    vtkvolume.volumeColor.AddRGBPoint(500, 1.0, 0.5, 0.3)
    vtkvolume.volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

# The opacity transfer function is used to control the opacity
# of different tissue types.
    vtkvolume.volumeScalarOpacity.AddPoint(0, 0.00)
    vtkvolume.volumeScalarOpacity.AddPoint(100, 0.15)
    vtkvolume.volumeScalarOpacity.AddPoint(500,  0.65)
    vtkvolume.volumeScalarOpacity.AddPoint(1150, 0.15)


# The gradient opacity function is used to decrease the opacity
# in the "flat" regions of the volume while maintaining the opacity
# at the boundaries between tissue types.  The gradient is measured
# as the amount by which the intensity changes over unit distance.
# For most medical data, the unit distance is 1mm.
    vtkvolume.volumeGradientOpacity.AddPoint(0,   0.0)
    vtkvolume.volumeGradientOpacity.AddPoint(90,  0.5)
    vtkvolume.volumeGradientOpacity.AddPoint(100, 1.0)

def brainextraction():
    vtkvolume.volumeColor.AddRGBPoint(0,    0.0, 0.0, 0.0)
    vtkvolume.volumeColor.AddRGBPoint(100,  1.0, 0.5, 0.9)
    vtkvolume.volumeColor.AddRGBPoint(500, 1.0, 0.5, 0.3)
    vtkvolume.volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

# The opacity transfer function is used to control the opacity
# of different tissue types.
    vtkvolume.volumeScalarOpacity.AddPoint(0, 0.00)
    vtkvolume.volumeScalarOpacity.AddPoint(100, 0.85)
    vtkvolume.volumeScalarOpacity.AddPoint(500,  0.15)
    vtkvolume.volumeScalarOpacity.AddPoint(1150, 0.15)


# The gradient opacity function is used to decrease the opacity
# in the "flat" regions of the volume while maintaining the opacity
# at the boundaries between tissue types.  The gradient is measured
# as the amount by which the intensity changes over unit distance.
# For most medical data, the unit distance is 1mm.
    vtkvolume.volumeGradientOpacity.AddPoint(0,   0.0)
    vtkvolume.volumeGradientOpacity.AddPoint(90,  0.5)
    vtkvolume.volumeGradientOpacity.AddPoint(100, 1.0)

def brxtraction():
    vtkvolume.volumeColor.AddRGBPoint(0, 0.0, 0.0, 0.0)
    vtkvolume.volumeColor.AddRGBPoint(10, 0.0, 0.5, 0.7)
    vtkvolume.volumeColor.AddRGBPoint(20, 1.0, 1.0, 1.0)
    vtkvolume.volumeColor.AddRGBPoint(30, 0.0, 0.3, 0.0)
    vtkvolume.volumeColor.AddRGBPoint(150,  1.0, 0.5, 0.3)
   # vtkvolume.volumeColor.AddRGBPoint(500, 1.0, 0.5, 0.3)
   # vtkvolume.volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

# The opacity transfer function is used to control the opacity
# of different tissue types.
    vtkvolume.volumeScalarOpacity.AddPoint(0, 0.00)
    vtkvolume.volumeScalarOpacity.AddPoint(10, 0.00)
    vtkvolume.volumeScalarOpacity.AddPoint(20, 0.80)
    vtkvolume.volumeScalarOpacity.AddPoint(30, 0.00)
    vtkvolume.volumeScalarOpacity.AddPoint(150, 0.00)
    #vtkvolume.volumeScalarOpacity.AddPoint(500,  0.00)
    #vtkvolume.volumeScalarOpacity.AddPoint(1150, 0.00)


# The gradient opacity function is used to decrease the opacity
# in the "flat" regions of the volume while maintaining the opacity
# at the boundaries between tissue types.  The gradient is measured
# as the amount by which the intensity changes over unit distance.
# For most medical data, the unit distance is 1mm.
    vtkvolume.volumeGradientOpacity.AddPoint(0,   0.0)
    vtkvolume.volumeGradientOpacity.AddPoint(60, 0.2)
    vtkvolume.volumeGradientOpacity.AddPoint(90,  0.4)
    vtkvolume.volumeGradientOpacity.AddPoint(100, 1.0)




