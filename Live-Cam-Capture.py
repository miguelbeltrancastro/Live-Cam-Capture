
#Import libraries
import urllib.request
import time
from datetime import datetime
import os
import filecmp

URL = input("Please enter a string: ")

#Create new folder
path = "Capture "+ str(datetime.today().year) + str(datetime.today().month) +str(datetime.today().day)
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
    exit()
else:
    print ("Successfully created the directory %s " % path)

#Capture first image
contador =0
filename = os.path.join(path, "Image" + str(contador) + ".jpg")
urllib.request.urlretrieve(URL, filename)
print("Saved Images: " + str(contador+1))
contador=contador+1
time.sleep(60)

#Capture one image every 60 seconds
while True:
    filename = os.path.join(path, "Image" + str(contador) + ".jpg")
    urllib.request.urlretrieve(URL, filename)
    #If previously captured image is the same, then it is deleted
    if filecmp.cmp(filename, os.path.join(path, "Image" + str(contador-1) + ".jpg"), shallow=False):
        print("Duplicated image")
        os.remove(filename)
        time.sleep(60)
    else:
        print("Saved Images: " + str(contador+1))
        contador=contador+1
        time.sleep(60)