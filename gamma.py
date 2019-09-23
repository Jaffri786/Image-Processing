# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:41:46 2019

@author: Ali Raza
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


###READ-IMAGE
img=cv2.imread('C:/Users/Ali Raza/Desktop/Jaff photos/received_1822008948047076.jpeg')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
frame=plt.figure()
frame.add_subplot(2,2,1)
plt.imshow(img2)
plt.axis('off')


###PLOT A HISTOGRAM
hist = cv2.calcHist([img2],[0],None,[256],[0,256])
frame.add_subplot(2,2,2)
plt.title('Histogram for original picture')
plt.plot(hist)



gamma=2
###NORMALIZATION
normalization=img2/255

###GAMMA CORRECTION
img_procces= np.power(normalization,gamma)*255

img_change = np.uint8(img_procces)

frame.add_subplot(2,2,3)
plt.imshow(img_change)
plt.axis('off')


hist = cv2.calcHist([img_change],[0],None,[256],[0,256])
frame.add_subplot(2,2,4)
plt.title('Histogram for processed picture')
plt.plot(hist)
plt.show()