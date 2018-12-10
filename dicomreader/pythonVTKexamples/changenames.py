import os, glob
# listing directories
print ("The dir is: %s"%os.listdir(os.getcwd()))

# renaming directory ''tutorialsdir"
#create dirs path"
pathDicom = "C:/Users/Art/Documents/python/dcmanalizer/prep_data"



filelist = glob.glob(pathDicom + "*.dcm")

val = 0

for file in filelist:
    val+1
    os.rename(file,".val")