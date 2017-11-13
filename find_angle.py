# load the required libraries
import os
import cv2
import numpy as np
import math
import csv
from itertools import groupby
# yoavram: Bug fix for Python 3 as suggested in https://github.com/nschloe/matplotlib2tikz/issues/20
try:
        from itertools import izip
except ImportError:
        izip = zip



#set the working directory to where the raw image is located
os.chdir('C:/Users/theri/Dropbox/Trevor_timelapse/extracted_frames3')

angle_list = []
frame_list = []

def find_angle(arg):
    


    img = cv2.imread(arg)
    #cv2.imshow('img', img)
    #cv2.waitKey()
    
    
    
   
    
    #create NumPy arrays from the color gray boundaries in RGB
    low = np.array([75-20, 82-20, 89-20])
    high = np.array([212, 206, 207])
    

    #find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(img, low, high)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #output = cv2.bitwise_and(img, img, mask = mask)

    #filter out the noise
    kernel = np.ones((2,2),np.uint8)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 1)
    #cv2.imshow('opening', opening)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #use erosion to skeletonize the image
    erode = cv2.erode(opening, kernel, iterations = 6)
    cv2.namedWindow('eroded', cv2.WINDOW_NORMAL)
    cv2.imshow('eroded', erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




    # detect edges of the eroded (skeletonized) image
    edges = cv2.Canny(erode, 150, 450, apertureSize = 3)
    cv2.imshow('edges', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    #create a variable for the lines that will be created using the HoughLines function
    lines = cv2.HoughLines(edges, 1, np.pi/180, 2)

    #for x in range(0, len(lines)):
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        
        line_img = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 5)
        
        cv2.namedWindow('%s' % arg, cv2.WINDOW_NORMAL)
        cv2.imshow('%s' % arg, line_img)
        cv2.waitKey()
        cv2.destroyAllWindows()

            
        if (x1 == x2):
            slope = 90
        
        else:
            slope = ((y2 - y1) / (x2 - x1))
    

                
    # find the angle of the found line
    theta = math.degrees(math.atan(slope))
    print (theta, arg)
    if (theta < 0):
        angle = ((theta)*(-1))
    elif ((theta >= 0)&(theta <= 45)):
        angle = theta
    else:
        angle = 90 - theta
    angle_list.append(angle)
    frame_list.append(arg)
    return angle
    
    
    with open('angles.csv', 'w') as a:
        write = csv.writer(a)
        write.writerows(izip(frame_list, angle_list))

