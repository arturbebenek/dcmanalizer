

class brxtraction:

    def __init__(self, volumeColor, volumeScalarOpacity, volumeGradientOpacity):
        volumeColor.AddRGBPoint(0, 0.0, 0.0, 0.0)
        volumeColor.AddRGBPoint(10, 0.0, 0.5, 0.7)
        volumeColor.AddRGBPoint(20, 1.0, 1.0, 1.0)
        volumeColor.AddRGBPoint(30, 0.0, 0.3, 0.0)
        volumeColor.AddRGBPoint(150,  1.0, 0.5, 0.3)

# The opacity transfer function is used to control the opacity
# of different tissue types.
        volumeScalarOpacity.AddPoint(0, 0.00)
        volumeScalarOpacity.AddPoint(10, 0.00)
        volumeScalarOpacity.AddPoint(20, 0.80)
        volumeScalarOpacity.AddPoint(30, 0.00)
        volumeScalarOpacity.AddPoint(150, 0.00)

# The gradient opacity function is used to decrease the opacity
# in the "flat" regions of the volume while maintaining the opacity
# at the boundaries between tissue types.  The gradient is measured
# as the amount by which the intensity changes over unit distance.
# For most medical data, the unit distance is 1mm.
        volumeGradientOpacity.AddPoint(0,   0.0)
        volumeGradientOpacity.AddPoint(60, 0.2)
        volumeGradientOpacity.AddPoint(90,  0.4)
        volumeGradientOpacity.AddPoint(100, 1.0)

        self.volumeColor = volumeColor
        self.volumeScalarOpacity = volumeScalarOpacity
        self.volumeGradientOpacity = volumeGradientOpacity

class skinextraction:

    def __init__(self,volumeColor,volumeScalarOpacity,volumeGradientOpacity):
        volumeColor.AddRGBPoint(0,    0.0, 0.0, 0.0)
        volumeColor.AddRGBPoint(100,  1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(500, 1.0, 0.5, 0.3)
        volumeColor.AddRGBPoint(1150, 1.0, 1.0, 0.9)

        volumeScalarOpacity.AddPoint(0, 0.00)
        volumeScalarOpacity.AddPoint(100, 0.15)
        volumeScalarOpacity.AddPoint(500,  0.65)
        volumeScalarOpacity.AddPoint(1150, 0.15)

        volumeGradientOpacity.AddPoint(0,   0.0)
        volumeGradientOpacity.AddPoint(90,  0.5)
        volumeGradientOpacity.AddPoint(100, 1.0)

        self.volumeColor = volumeColor
        self.volumeScalarOpacity = volumeScalarOpacity
        self.volumeGradientOpacity = volumeGradientOpacity
