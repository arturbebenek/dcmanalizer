import vtk
import glob

class Singleview:

    def __init__(self, path):
        self.path = path
        self.filelist = glob.glob(path + "/*.dcm")