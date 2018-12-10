
import pydicom
import glob

# Start by loading some data.
PathDicom = "F:/MRI Brain Scan/Series 8/"
filename = "random name"
modality = "ranfom modality"
id = "22"



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

