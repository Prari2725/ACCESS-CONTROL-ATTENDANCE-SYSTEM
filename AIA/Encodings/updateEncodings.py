import pickle
import os
savePath = ''
if os.path.isdir('Encodings/'):
    
    if os.path.isfile('Encodings/Encodings.dat'):
        print("[INFO] encodings already avaiable going for update ... ")
        savePath = "Encodings/Encodings.dat"
        flag = 1
        
    else:
        savePath = "Encodings/Encodings.dat"
        flag = 0

else:
    os.mkdir('Encodings')
    print("[INFO] making new encodings ... ")
    savePath = "Encodings/Encodings.dat"
    flag = 0

