# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:16:49 2019

@author: Ali Raza
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('C:/Users/Ali Raza/Desktop/Python project/RGB.jpg')
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
frame=plt.figure()
frame.add_subplot(4,2,1)
plt.title('Original image')
plt.imshow(img2,'gray')
plt.axis('off')

#PLOT A HISTOGRAM
hist, edges = np.histogram(img2,bins=range(256))
frame.add_subplot(4,2,2)
plt.title('Histogram for original picture')
plt.bar(edges[:-1], hist, width = 0.8, color='red')

#Red plane image
frame.add_subplot(4,2,3)
plt.imshow(img2[:,:,0],'gray')
plt.axis('off')
plt.title('Red Plane')

#histogram of red plane
hist, edges = np.histogram(img2[:,:,0],bins=range(256))
frame.add_subplot(4,2,4)
plt.title('Histogram for Red plane')
plt.bar(edges[:-1], hist, width = 0.8, color='red')

#Green plane image
frame.add_subplot(4,2,5)
plt.imshow(img2[:,:,1],'gray')
plt.axis('off')
plt.title('Green Plane')

#histogram of Green plane
hist, edges = np.histogram(img2[:,:,1],bins=range(256))
frame.add_subplot(4,2,6)
plt.title('Histogram for Green plane')
plt.bar(edges[:-1], hist, width = 0.8, color='red')

#Blue plane image
frame.add_subplot(4,2,7)
plt.imshow(img2[:,:,2],'gray')
plt.axis('off')
plt.title('Blue Plane')

#histogram of Blue plane
hist, edges = np.histogram(img2[:,:,2],bins=range(256))
frame.add_subplot(4,2,8)
plt.title('Histogram for Blue plane')
plt.bar(edges[:-1], hist, width = 0.8, color='red')


