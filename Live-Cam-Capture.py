
#Import libraries
import urllib.request
import time
from datetime import datetime
import os
import filecmp

#Create new folder
path = "Capture "+ str(datetime.today().year) + str(datetime.today().month) +str(datetime.today().day)
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    exit()
else:
    print ("Successfully created the directory %s " % path)

URL = "https://www.skilift-donnstetten.de/webcam/pic/webpic.jpg"

#Capture first image
contador =0
filename = os.path.join(path, "Imagen" + str(contador) + ".jpg")
urllib.request.urlretrieve(URL, filename)
print("Imágenes guardadas: " + str(contador+1))
contador=contador+1
time.sleep(60)

#Capture one image every 60 seconds
while True:
    filename = os.path.join(path, "Imagen" + str(contador) + ".jpg")
    urllib.request.urlretrieve(URL, filename)
    #If previously captured image is the same, then it is deleted
    if filecmp.cmp(filename, os.path.join(path, "Imagen" + str(contador-1) + ".jpg"), shallow=False):
        print("Imagen duplicada")
        os.remove(filename)
        time.sleep(60)
    else:
        print("Imágenes guardadas: " + str(contador+1))
        contador=contador+1
        time.sleep(60)