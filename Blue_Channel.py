# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:10:35 2019

@author: Ali Raza
"""

import matplotlib.pyplot as plt #library for plotting
import cv2

#Blue chanel image

img=cv2.imread('C:/Users/Ali Raza/Desktop/Python project/RGB.jpg') #image reading fucntion give the path of image

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #function for change image clr from BGR to RGB because default image read as BGR

frame=plt.figure() #initialize frames

frame.add_subplot(1,2,1) #(Rows,coloumn,image no.)
plt.imshow(img)
plt.axis('off')
plt.title('Original Image')



frame.add_subplot(1,2,2)
plt.imshow(img[:,:,2],'gray')
plt.axis('off')
plt.title('Single Channel Image')
