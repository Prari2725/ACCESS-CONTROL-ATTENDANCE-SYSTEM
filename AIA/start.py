
from tkinter import *
import os
from datetime import datetime
from PIL import Image,ImageTk

parent_dir = os.getcwd()
os_list = parent_dir.split('/')
os_list.pop()
parent_path = os.path.join(*os_list)

root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    root.destroy()
    os.system("python3 dataset_creator.py")
    
    
def function2():
    root.destroy()
    os.system("python3 Find_Encodings.py")
    

def function3():
    root.destroy()
    os.system("python3 Detection_and_Recognition_LIVE.py")
    
   
def function6():

    root.destroy()

def attend():
    os.system("libreoffice ./CSV_sheet/"+'Attendence_'+str(datetime.now().date())+'.csv')


root.title("AIA")


Label(root, text="ACCESS CONTROL SYSTEM",font=("System-ui Regular",20),fg="black",bg="white",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


image1 = Image.open('/home/pi/Desktop/AIA/icons/1.png')
image2 = Image.open('/home/pi/Desktop/AIA/icons/6.png')
image3 = Image.open('/home/pi/Desktop/AIA/icons/3.png')
image4 = Image.open('/home/pi/Desktop/AIA/icons/4.png')

image1 = image1.resize((50,50), Image.Resampling.LANCZOS)
image2 = image2.resize((50,50), Image.Resampling.LANCZOS)
image3 = image3.resize((50,50), Image.Resampling.LANCZOS)
image4 = image4.resize((60,50), Image.Resampling.LANCZOS)

img1 = ImageTk.PhotoImage(image1)
img2 = ImageTk.PhotoImage(image2)
img3 = ImageTk.PhotoImage(image3)
img4 = ImageTk.PhotoImage(image4)



Button(root,text="Create Dataset" ,font=("times new roman",20),image=img2, compound= LEFT,bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Train Dataset",font=("times new roman",20),image=img4, compound= LEFT,bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Recognize + Access Control",font=('times new roman',20),image=img1, compound= LEFT,bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Access Sheet",font=('times new roman',20),image=img3, compound= LEFT,bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()