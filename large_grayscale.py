# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 04:35:33 2019

@author: Ali Raza
"""
#Reading & Displaying gray scale

#Large image



import numpy as np
import cv2

img = cv2.imread('C:/Users/Ali Raza/Desktop/Python project/large_image.jpg')
cv2.imshow('large_image',img)