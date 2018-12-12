import vtk
import glob


class Model:


    def __init__(self, path):

        filelist = glob.glob(path + "/*.dcm")

        #self.vtkWidget = QVTKRenderWindowInteractor()