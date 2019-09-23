# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:58:19 2019

@author: Ali Raza
"""
#Reading & displayig gray image 


#Small Image

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Ali Raza/Desktop/Jaff photos/download.jpg')
cv2.imshow('gray',img)

