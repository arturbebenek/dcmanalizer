
import pydicom
import glob



def Dicominfo(pathDicom):
    filelist = glob.glob(pathDicom + "/*.dcm")
    filename = filelist[0]
    dataset = pydicom.dcmread(filename)

    # Normal mode:
    print()
    print("Filename.........:", filename)
    print("Storage type.....:", dataset.SOPClassUID)
    print()

    pat_name = dataset.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    print("Patient's name...:", display_name)
    print("Patient id.......:", dataset.PatientID)
    print("Modality.........:", dataset.Modality)
    print("Study Date.......:", dataset.StudyDate)

    if 'PixelData' in dataset:
        rows = int(dataset.Rows)
        cols = int(dataset.Columns)
        print("Image size.......: {rows:d} x {cols:d}, {size:d} bytes".format(
            rows=rows, cols=cols, size=len(dataset.PixelData)))
    if 'PixelSpacing' in dataset:
        print("Pixel spacing....:", dataset.PixelSpacing)

class DicInfo:


    def __init__(self, path):
        self.path = path
        self.filelist = glob.glob(path + "/*.dcm")
        self.filename = self.filelist[0]
        self.dataset = pydicom.dcmread(self.filename)
        self.patientname = "Patient's name...: " + str(self.dataset.PatientName)
        self.patientid = "Patient id.......: " + str(self.dataset.PatientID)
        self.modality = "Modality.........: " + str(self.dataset.Modality)
        self.studydate = "Study Date.......: "+ str(self.dataset.StudyDate)