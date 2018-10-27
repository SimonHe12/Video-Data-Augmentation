'''
This is the file for getting frames

'''

import cv2
import sys
import numpy as np
import os


def frameSeperation(img_root):              #img_root--the root file of videos
    X_data = []
    vidcap = cv2.VideoCapture(img_root)     #load video
    fps = vidcap.get(cv2.CAP_PROP_FPS)      #get fps
    success, image = vidcap.read()          #read video into frame
    success = True
    count = 0

    while success:                          #put frames of a video into a array
        if(success==0):
            break
        X_data.append(image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return X_data, fps
    
