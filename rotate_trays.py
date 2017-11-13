# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 10:14:53 2017

@author: theri
"""

import cv2
import os, os.path
import glob

os.chdir('C:/Users/theri/Dropbox/Trevor_timelapse/Codes')
dirname = 'C:/Users/theri/Dropbox/Trevor_timelapse/extracted_frames3/rotated'
os.mkdir(dirname)



def rotate_img(arg1,arg2):
    
 
        
    img = cv2.imread(arg1)
    
    rows,cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2),-float(arg2),1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imwrite(os.path.join(dirname, arg1), dst)
        #cv2.namedWindow('rotated', cv2.WINDOW_NORMAL)
        #cv2.imshow('rotated', dst)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
