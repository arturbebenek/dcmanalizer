
import pydicom
import glob


class DicInfo:


    def __init__(self, path):
        self.path = path
        self.filelist = glob.glob(path + "/*.dcm")
        self.filename = self.filelist[0]
        self.dataset = pydicom.dcmread(self.filename)
        self.patientname = "Patient's name: \n" + str(self.dataset.PatientName)
        self.patientid = "Patient id: \n" + str(self.dataset.PatientID)
        self.modality = "Modality: \n" + str(self.dataset.Modality)
        self.studydate = "Study Date: \n" + str(self.dataset.StudyDate)

        if 'PixelData' in self.dataset:
            self.pixeldata = ("Image size: \n" + str(self.dataset.Rows) + " x " + str(self.dataset.Columns) + "\n weight: " +
                                str(len(self.dataset.PixelData)))
        if 'PixelSpacing' in self.dataset:
            self.pixelspacing = "Pixel spacing: \n" + str(self.dataset.PixelSpacing)
