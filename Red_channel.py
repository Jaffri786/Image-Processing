# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:23:13 2019

@author: Ali Raza
"""

import matplotlib.pyplot as plt
import cv2

#Red chanel image

img=cv2.imread('C:/Users/Ali Raza/Desktop/Python project/RGB.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

frame=plt.figure()

frame.add_subplot(1,2,1)
plt.imshow(img)
plt.axis('off')
plt.title('Original Image')



frame.add_subplot(1,2,2)
plt.imshow(img[:,:,0],'gray')
plt.axis('off')
plt.title('Single Channel Image')