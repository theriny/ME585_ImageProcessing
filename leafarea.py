# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:29:01 2017

@author: theri
"""

from matplotlib import pyplot as plt
import numpy as np
import cv2
import os, os.path
import argparse #used for image rotation
import imutils
from glob import glob
import random

#set working directory where images are located
os.chdir('c:/Python27/Trevor_timelapse/4_10/pots_frame322')
dirname = 'C:/Python27/Trevor_timelapse/frame322_bw'
os.mkdir(dirname)

#define green hsv color space
lower_green = np.array([25,100,100])
upper_green = np.array([60,255,255])


count = 0
all_dilate =[]
all_area = []
for pots in glob('*.jpg'):
    im = cv2.imread(pots)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)  
    result = cv2.bitwise_and(hsv,hsv,mask = mask)        
    kernel = np.ones((1,1),np.uint8)        
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 4)
    
            
    dilate = cv2.dilate(opening,kernel,iterations=7) 
               
    area = cv2.countNonZero(dilate)
    
    all_area.append(area)
    all_dilate.append(dilate)
    print all_area
    
    count += 1
    for pots in all_dilate:
        cv2.imwrite(os.path.join(dirname, "frame%d.jpg" % count), pots)
    
    
    
    
 
   
    

                
                    
                        
                        
                             
                            
                                
                    
        
    
    
 
    


 
