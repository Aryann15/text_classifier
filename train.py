import numpy as np
import cv2 as cv
import os

path= 'myData'
images= []
classNo=[]

myList = os.listdir(path)
print(myList)

class_numbers = len(myList)
for x in range(0,class_numbers):
    pic_list = os.listdir(path + '/' + str(x))
    for y in pic_list:
        current_image = cv.imread(path+'/'+str(x)+ '/' +y)
        current_image = cv.resize(current_image,(32,32))
        images.append(current_image)
        classNo.append(x)
    # print(x)

images = np.array(images)
classNo = np.array(classNo)