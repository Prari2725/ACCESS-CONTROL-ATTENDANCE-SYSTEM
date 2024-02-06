import face_recognition
import pickle
import cv2
import time
import markAttendence
import os	

print("[INFO] loading encodings...")
data = pickle.loads(open("Encodings/Encodings.dat", "rb").read())


image = cv2.imread("Test_Encodings/4.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

time.sleep(2)

print("[INFO] finding faces...")
boxes = face_recognition.face_locations(rgb,number_of_times_to_upsample=1,model='hog')
encodings = face_recognition.face_encodings(rgb, boxes)

names = []

print("[INFO] recognizing faces...")
time.sleep(2)
for encoding in encodings:
	matches = face_recognition.compare_faces(data['encodings'],encoding)
	name = "Unknown"
	
	if True in matches:
		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}
		
		for i in matchedIdxs:
			name = data["names"][i]
			counts[name] = counts.get(name, 0) + 1
		name = max(counts, key=counts.get)
		
	names.append(name)



print("[INFO] marking faces with red box...")
time.sleep(2)
for ((top, right, bottom, left), name) in zip(boxes, names):
	
	cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 3)

	cv2.rectangle(image,(left,bottom+35),(right,bottom),(0,0,255),cv2.FILLED)
	font = cv2.FONT_HERSHEY_DUPLEX
	cv2.putText(image,name,(left+6,bottom+24),font,0.7,(255,255,255),1)	

print("[INFO] showing image...")
cv2.imshow("Image", image)
if cv2.waitKey(100) & 0xFF == ord('q'):
	cv2.destroyAllWindows()
os.system("python3 start.py")