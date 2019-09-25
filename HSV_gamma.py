# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 02:54:46 2019

@author: Ali Raza
"""

#HSV file
import cv2
import numpy as np
from matplotlib import pyplot as plt


###READ-IMAGE
img=cv2.imread('C:/Users/Ali Raza/Desktop/Jaff photos/pic/_MG_0633.JPG')
img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
frame=plt.figure()
frame.add_subplot(1,2,1)
plt.title('original image')
plt.imshow(img_RGB)
plt.axis('off')

img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
frame=plt.figure()
frame.add_subplot(1,2,1)
plt.title('hsv image')
plt.imshow(img2[:,:,2])
plt.axis('off')

###PLOT A HISTOGRAM
hist, edges = np.histogram(img2[:,:,2],bins=range(256))
frame.add_subplot(1,2,2)
plt.title('Histogram for HSV picture')
plt.bar(edges[:-1], hist, width = 0.8, color='red')



gamma_value=1.6
###NORMALIZATION

normalization=img2[:,:,2]/255
###GAMMA CORRECTION
gamma_vp= np.power(normalization,gamma_value)*255
#Changing image type to uint
vprocessed = np.uint8(gamma_vp)

im_process=img2
im_process[:,:,2]=vprocessed
#Display images of different gamma power
frame=plt.figure()
frame.add_subplot(1,2,1)
plt.imshow(vprocessed)
plt.title('processed image')
plt.axis('off')
   
    
#Histogram of images     
hist, edges = np.histogram(vprocessed,bins=range(256))
frame.add_subplot(1,2,2)
plt.title('Histrogram of proccesed image with Gamma ='+ str(gamma_value))
plt.bar(edges[:-1], hist, width = 0.8, color='red')

img3=cv2.cvtColor(im_process,cv2.COLOR_HSV2RGB)
frame=plt.figure()
frame.add_subplot(1,2,1)
plt.title('final image')
plt.imshow(img3)
plt.axis('off')
plt.show()

    