import numpy as np
import cv2 as cv
import os
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical


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
    print(x)

images = np.array(images)
classNo = np.array(classNo)

print(images.shape)
print(classNo.shape)

# splitting the data
X_train,X_test,Y_train,Y_test = train_test_split(images, classNo, test_size=0.2)
X_train,X_validation,Y_train,Y_validation = train_test_split(X_train,Y_train, test_size=0.2)

for x in range(0,class_numbers):
    print(len(np.where(Y_train==x)[0]))

def preprocessing(img):
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)
    img = img/255
    return img

X_train = np.array(list(map(preprocessing,X_train)))
X_test = np.array(list(map(preprocessing,X_test)))
X_validation = np.array(list(map(preprocessing,X_validation)))

X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],X_train.shape[2],1 )
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],X_test.shape[2],1 )
X_validation = X_validation.reshape(X_validation.shape[0],X_validation.shape[1],X_validation.shape[2],1 )

print(X_train.shape)

dataGen = ImageDataGenerator(width_shift_range=0.1,height_shift_range=0.1,zoom_range=0.2,shear_range=0.1,rotation_range=10)
dataGen.fit(X_train)

Y_train = to_categorical(Y_train,class_numbers)
Y_test = to_categorical(Y_test,class_numbers)
Y_validation = to_categorical (Y_validation,class_numbers)

