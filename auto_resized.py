# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:18:59 2019

@author: Ali Raza
"""
#Displaying image wether it is large or small

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:/Users/Ali Raza/Desktop/Python project/large_image.jpg')
plt.imshow(img)
