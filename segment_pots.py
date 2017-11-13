# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:22:05 2017

@author: theri
"""

from matplotlib import pyplot as plt
import numpy as np
import cv2
import os
#import imutils



#set working directory where images are located
os.chdir('C:/Users/theri/Dropbox/Trevor_timelapse/extracted_frames3')





    

def segment_pots(arg):
    
    #read frame image
    img = cv2.imread(arg)
    cv2.namedWindow('frame0', cv2.WINDOW_NORMAL)
    cv2.imshow('frame0', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    #Crop out trays and write it to image file
    tray = img[159:942, 683:1484]
    cv2.imwrite('tray.jpg', tray)
    img2 = cv2.imread('tray.jpg')
    cv2.namedWindow('tray', cv2.WINDOW_NORMAL)
    cv2.imshow('tray', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #define lengths x and y
    x=133
    y=133

    #define range of green color in HSV
    lower_green = np.array([25,100,100])
    upper_green = np.array([60,255,255])



    #choose specific pots from tray 1 (pots 3,4,9,10,15)
    pot3=tray[4:129,1+(2*x):121+(2*x)]
    cv2.imwrite('pot3.jpg', pot3)
    pot4=tray[4+y:129+y,1:121]
    cv2.imwrite('pot4.jpg', pot4)
    pot9=tray[4+(2*y):129+(2*y),1+(2*x):121+(2*x)]
    cv2.imwrite('pot9.jpg', pot9)
    pot10=tray[4+(3*y):129+(3*y),1:121]
    cv2.imwrite('pot10.jpg', pot10)
    pot15=tray[4+(4*y):129+(4*y),1+(2*x):121+(2*x)]
    cv2.imwrite('pot15.jpg', pot15)

    #choose specific pots from tray 2 (pots 1,5,7,11,13)
    pot_1=tray[0:122,408:529]
    cv2.imwrite('pot_1.jpg', pot_1)
    pot_5=tray[0+y:122+y,408+x:529+x]
    cv2.imwrite('pot_5.jpg', pot_5)
    pot_7=tray[0+(2*y):122+(2*y),408:529]
    cv2.imwrite('pot_7.jpg', pot_7)
    pot_11=tray[0+(3*y):122+(3*y),408+x:529+x]
    cv2.imwrite('pot_11.jpg', pot_11)
    pot_13=tray[0+(4*y):122+(4*y),408:529]
    cv2.imwrite('pot_13.jpg', pot_13)   
    
        
     
    #plot all analyzed images to single window
    plt.subplot(2,5,1),plt.imshow(pot3,'Greens'),plt.title('pot3')
    plt.axis("off")
    plt.subplot(2,5,2),plt.imshow(pot4,'Greens'),plt.title('pot4')
    plt.axis("off")
    plt.subplot(2,5,3),plt.imshow(pot9,'Greens'),plt.title('pot9')
    plt.axis("off")
    plt.subplot(2,5,4),plt.imshow(pot10,'Greens'),plt.title('pot10')
    plt.axis("off")
    plt.subplot(2,5,5),plt.imshow(pot15,'Greens'),plt.title('pot15')
    plt.axis("off")
    plt.subplot(2,5,6),plt.imshow(pot_1,'Greens'),plt.title('pot_1')
    plt.axis("off")
    plt.subplot(2,5,7),plt.imshow(pot_5,'Greens'),plt.title('pot_5')
    plt.axis("off")
    plt.subplot(2,5,8),plt.imshow(pot_7,'Greens'),plt.title('pot_7')
    plt.axis("off")
    plt.subplot(2,5,9),plt.imshow(pot_11,'Greens'),plt.title('pot_11')
    plt.axis("off")
    plt.subplot(2,5,10),plt.imshow(pot_13,'Greens'),plt.title('pot_13')
    plt.axis("off")

       
    plt.show()
    
