# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:38:38 2017

@author: theri
"""

import cv2
import numpy as np
import os
from rotate_ht_genesis2 import rotate_img
from angle_ht_genesis2_practice import find_angle
from segmentpots2 import segment_pots
import glob
import csv
from itertools import groupby
# yoavram: Bug fix for Python 3 as suggested in https://github.com/nschloe/matplotlib2tikz/issues/20
try:
        from itertools import izip
except ImportError:
        izip = zip


os.chdir("C:/Users/theri/Dropbox/Trevor_timelapse/extracted_frames3/frames")
dirname = 'C:/Users/theri/Dropbox/Trevor_timelapse/extracted_frames3/frames/results'

frames = glob.glob('./*.jpg')


#create lists to keep track of images and angles
angle_list = []
frame_list = []

count = 0
while (count < len(frames)):

    for frame in frames:
    
     angle_list2 = find_angle(frame)
     rotated = rotate_img(frame, angle_list2)
     
     angle_list.append(angle_list2)
     frame_list.append(frame)
     
     with open('angles.csv', 'w') as a:
            write = csv.writer(a)
            write.writerows(izip(frame_list, angle_list))
            
    pots = segment_pots(rotated)
    
    for pot in frame_list:
        cv2.imwrite(os.path.join(dirname, "frame%s.jpg" % frame), pots)

    count = count + 1;
    
    
