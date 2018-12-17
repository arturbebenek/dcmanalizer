
import pydicom
import glob


class DicInfo:


    def __init__(self, path):
        filelist = glob.glob(path + "/*.dcm")
        filename = filelist[0]
        dataset = pydicom.dcmread(filename)
        self.patientname = "Patient's name: \n" + str(dataset.PatientName)
        self.patientid = "Patient id: \n" + str(dataset.PatientID)
        self.modality = "Modality: \n" + str(dataset.Modality)
        self.studydate = "Study Date: \n" + str(dataset.StudyDate)

        if 'PixelData' in dataset:
            self.pixeldata = ("Image size: \n" + str(dataset.Rows) + " x " + str(dataset.Columns) + "\nWeight: " +
                               "\n" + str(len(dataset.PixelData)) + " Bytes")
        if 'PixelSpacing' in dataset:
            self.pixelspacing = "Pixel spacing: \n" + str(dataset.PixelSpacing)
