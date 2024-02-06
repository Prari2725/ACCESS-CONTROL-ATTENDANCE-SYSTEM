import json
import os	


detdict = {}
jsonContent = {}


def getContent():
	global jsonContent
	global parent_path
	
	file = open("studentDetails.json", "r")
	jsonContent = json.load(file)
	file.close()
	


def addContent(detdict):
	global parent_path
	global jsonContent
	for key,value in detdict.items():
		jsonContent[key] = value
		

def dumpContent():
	global parent_path
	global jsonContent
	file = open("studentDetails.json", "w")
	json.dump(jsonContent, file,indent = 4)	
	file.close()

