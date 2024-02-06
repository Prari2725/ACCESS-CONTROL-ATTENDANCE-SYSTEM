import json
import csv
import pandas as pd
from pathlib import Path
import os
from datetime import datetime

PRNdict = {}
attendenceToMark = ()

def getjsonDetails():
    global PRNdict
    file = open("studentDetails.json", "r")
    PRNdict = json.load(file)
    file.close()



def checkIfCsvExist():
    global PRNdict
    my_file = Path("CSV_sheet"+"/"+'Attendence_'+str(datetime.now().date())+'.csv')
    if my_file.is_file():
       pass
    else:
        file = open("CSV_sheet"+"/"+'Attendence_'+str(datetime.now().date())+'.csv', 'w', newline ='')
        with file:
            header = PRNdict["Headers"]
            writer = csv.DictWriter(file, fieldnames = header)
            writer.writeheader()


def getCSVdata(givenPRNnumber):
    global attendenceToMark
    file = open("CSV_sheet"+"/"+'Attendence_'+str(datetime.now().date())+'.csv', 'r')
    PrnCOLdata = pd.read_csv(file)
    numbers = PrnCOLdata['PRN number'].tolist()
    
    attendenceToMark = []
    for onePRN in givenPRNnumber:
        if onePRN not in numbers:
            attendenceToMark.append(onePRN)
    



def writeValuesInCSV():
    global attendenceToMark
    global PRNdict
    file = open("CSV_sheet"+"/"+'Attendence_'+str(datetime.now().date())+'.csv', 'a+', newline ='')
    with file:
        for data in attendenceToMark:
            listData = PRNdict[data]
            header = PRNdict["Headers"]
            writer = csv.DictWriter(file,fieldnames=header)
            
            writer.writerow({
                            'PRN number' : str(data),
                            'firstName' :listData[0] ,
                            'midName': listData[1], 
                            'lastName': listData[2],
                            'class': listData[3],
                            'Year': listData[4],
                            'mobileNumber':listData[5]
                        })

