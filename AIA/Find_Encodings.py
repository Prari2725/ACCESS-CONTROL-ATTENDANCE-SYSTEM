from imutils import paths
import face_recognition
import os
import pickle
from Encodings import updateEncodings

imagePaths = list(paths.list_images("Dataset/"))

knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i + 1, len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2]
    img = face_recognition.load_image_file(imagePath)
    boxes = face_recognition.face_locations(img, number_of_times_to_upsample=1, model="hog")
    
    # Check if any faces are detected before accessing encodings
    if len(boxes) > 0:
        encodings = face_recognition.face_encodings(img, boxes)[0]
        knownEncodings.append(encodings)
        knownNames.append(name)

print("[INFO] serializing encodings...")

data = {"encodings": knownEncodings, "names": knownNames}

pathfile = updateEncodings.savePath

if updateEncodings.flag == 1:
    with open(pathfile, "rb+") as fileObjectMainRead:
        Data = pickle.load(fileObjectMainRead)
        
        for index in range(len(knownEncodings)):
            Data["encodings"].append(knownEncodings[index])
            Data["names"].append(knownNames[index])
        
        fileObjectMainRead.seek(0)  # Move the file pointer to the beginning
        fileObjectMainRead.truncate()  # Clear the file content
        fileObjectMainRead.write(pickle.dumps(Data))
else:
    with open(pathfile, "wb") as fileDefaultSave:
        fileDefaultSave.write(pickle.dumps(data))

print("[INFO] encodings saved successfully...")
os.system("python3 start.py")