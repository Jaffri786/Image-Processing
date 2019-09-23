# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:14:42 2019

@author: Ali Raza
"""
#RGB Channel through subplot

import matplotlib.pyplot as plt
import cv2


img=cv2.imread('C:/Users/Ali Raza/Desktop/Python project/RGB.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

frame=plt.figure()

frame.add_subplot(2,2,1)
plt.imshow(img)
plt.axis('off')
plt.title('Original Image')

frame.add_subplot(2,2,2)
plt.imshow(img[:,:,0],'gray')
plt.axis('off')
plt.title('Red Plane')

frame.add_subplot(2,2,3)
plt.imshow(img[:,:,1],'gray')
plt.axis('off')
plt.title('Green Plane')

frame.add_subplot(2,2,4)
plt.imshow(img[:,:,2], 'gray')
plt.axis('off')
plt.title('Blue Plane')
