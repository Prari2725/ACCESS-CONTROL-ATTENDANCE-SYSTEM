import cv2
import os 
import time
import savedetails
import json

PRNdict = {}
file = open("studentDetails.json", "r")
PRNdict = json.load(file)
file.close()
PRNdict = list(PRNdict.keys())


loop = True
count = 0
PRN_details = {}
time.sleep(1)

print("[INFO] loading face detector... ")
face_detector = cv2.CascadeClassifier('haarcascade_frontalface.xml')
time.sleep(1)


while loop:
	time.sleep(1)
	print("[INFO] fill your personl details ... \n")
	PRNnumber = str(input("Enter your PRN number   -: "))
	if PRNnumber in PRNdict:
		print("[INFO] prn number already in data base ... exiting ")
		break
	firstName = str(input("Enter your name ('first name') -: "))
	midName = str(input("Enter your name ('middle name') -: "))
	lastName = str(input("Enter your name ('last name') -: "))
	cllas = str(input("Enter your division -: "))
	stream = str(input("Enter your Year('eg : second year') -: "))
	
	mobileNumber = int(input("Enter your Mobile number -: "))

	
	key = PRNnumber
	values = list((firstName,midName,lastName,cllas,stream,mobileNumber))
	PRN_details[key] = values

	
	savedetails.getContent()
	savedetails.addContent(PRN_details)
	savedetails.dumpContent()
	

	time.sleep(1)
	print("\n[INFO] creating dataset file to store images ... ")
	folderName = 'Dataset'+'/'+PRNnumber+'/' 
	savePath = folderName
	dire = os.path.dirname(savePath)
	
	if not os.path.exists(dire):
		os.makedirs(dire)

	time.sleep(1)
	print("[INFO] getting images  ... ")
	cameraCapture = cv2.VideoCapture(0)
	faceCount = 0

	while True:
		_, imageFrame = cameraCapture.read()
		grayFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2GRAY)
		faces = face_detector.detectMultiScale(grayFrame,1.3, 5)

		for (x,y,w,h) in faces:
			cv2.rectangle(imageFrame, (x,y), (x+w,y+h), (255,0,0), 2)
			faceCount+=1
			cv2.imwrite(dire+'/'+PRNnumber+'_'+str(faceCount)+".jpg", grayFrame)
			print("Image saved with name : ",dire+'/'+PRNnumber+'_'+str(faceCount)+".jpg")


		if cv2.waitKey(100) & 0xFF == ord('q'):
			break

		elif faceCount>=30:
			time.sleep(2)
			print("[INFO] dataset created ... ")
			break

		cv2.imshow('frame', imageFrame)
	cameraCapture.release()

	cv2.destroyAllWindows()

	count+=1
	if count == 1:
		break
	else:
		continue
time.sleep(1)
print("[INFO] saving your personal detials ... ")

os.system("python3 start.py")
