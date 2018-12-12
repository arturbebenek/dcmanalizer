#
# This example reads a volume dataset and displays it via volume rendering.
#

import vtk
import volume_tfsetup

# Create the renderer, the render window, and the interactor. The renderer
# draws into the render window, the interactor enables mouse- and
# keyboard-based interaction with the scene.
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


PathDicom = "C:/Users/Art/Documents/python/dcmanalizer/prep_data/"

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(PathDicom)
#reader.SetDataExtent(0, 255, 0, 255, 2, 61) #0,63
#reader.SetDataSpacing(3.2, 3.2, 1.5)
#reader.SetDataOrigin(0.0, 0.0, 0.0)
#reader.SetDataScalarTypeToUnsignedShort()
#reader.UpdateWholeExtent()

# The volume will be displayed by ray-cast alpha compositing.
# A ray-cast mapper is needed to do the ray-casting, and a
# compositing function is needed to do the compositing along the ray.
#volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
volumeMapper = vtk.vtkOpenGLGPUVolumeRayCastMapper()
volumeMapper.SetInputConnection(reader.GetOutputPort())
volumeMapper.SetBlendModeToComposite()

# The color transfer function maps voxel intensities to colors.
# It is modality-specific, and often anatomy-specific as well.
# The goal is to one color for flesh (between 500 and 1000)
# and another color for bone (1150 and over).
volumeColor = vtk.vtkColorTransferFunction()
volumeScalarOpacity = vtk.vtkPiecewiseFunction()
volumeGradientOpacity = vtk.vtkPiecewiseFunction()

#volume_tfsetup.brxtraction(volumeColor,volumeScalarOpacity,volumeGradientOpacity)
volume_tfsetup.skinextraction(volumeColor,volumeScalarOpacity,volumeGradientOpacity)


# The VolumeProperty attaches the color and opacity functions to the
# volume, and sets other volume properties.  The interpolation should
# be set to linear to do a high-quality rendering.  The ShadeOn option
# turns on directional lighting, which will usually enhance the
# appearance of the volume and make it look more "3D".  However,
# the quality of the shading depends on how accurately the gradient
# of the volume can be calculated, and for noisy data the gradient
# estimation will be very poor.  The impact of the shading can be
# decreased by increasing the Ambient coefficient while decreasing
# the Diffuse and Specular coefficient.  To increase the impact
# of shading, decrease the Ambient and increase the Diffuse and Specular.
volumeProperty = vtk.vtkVolumeProperty()
volumeProperty.SetColor(volumeColor)
volumeProperty.SetScalarOpacity(volumeScalarOpacity)
volumeProperty.SetGradientOpacity(volumeGradientOpacity)
volumeProperty.SetInterpolationTypeToLinear()
volumeProperty.ShadeOn()
volumeProperty.SetAmbient(0.5)
volumeProperty.SetDiffuse(0.3)
volumeProperty.SetSpecular(0.6)


# The vtkVolume is a vtkProp3D (like a vtkActor) and controls the position
# and orientation of the volume in world coordinates.
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(volumeProperty)

# Finally, add the volume to the renderer
ren.AddViewProp(volume)

# Set up an initial view of the volume.  The focal point will be the
# center of the volume, and the camera position will be 400mm to the
# patient's left (which is our right).
camera =  ren.GetActiveCamera()
c = volume.GetCenter()
camera.SetFocalPoint(c[0], c[1], c[2])
camera.SetPosition(c[0] + 400, c[1], c[2])
camera.SetViewUp(0, 0, -1)

# Increase the size of the render window
renWin.SetSize(640, 480)

# Interact with the data.
iren.Initialize()
renWin.Render()
iren.Start()
