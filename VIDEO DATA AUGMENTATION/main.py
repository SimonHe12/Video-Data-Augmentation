'''
Create on Sep 6 2018
Video Data Augment
Simon He
'''
import gainFrame
import operations

import cv2
import sys
import numpy as np
import os
import random

imagePath = "/Users/4321118/Desktop/Augment/data/"              #path of data
outputPath = "/Users/4321118/Desktop/Augment/Processed/"        #path for processed data

classfier = -1

for root,dirs,files in os.walk(imagePath):                      #read the path of data
    numVideo = -1
    if (1):                                              
        classfier += 1
        for file in files:
            movingDis = random.randint(30,80)                   #set the value of operations
            rotateAng = random.randint(5,15)
            scaleTim = [random.uniform(1.2,1.4),random.uniform(0.6,0.9)]
            
            numVideo += 1
            
            path = outputPath+"%d"%classfier                    #path for processed videos
            
            operations.mkdir(path)                                  
            
            processed1=[]                                       #store processed data
            processed2=[]
            processed3=[]
            processed4=[]
            processed5=[]
            processed6=[]
            processed7=[]
            processed8=[]
            if(file!='.DS_Store'):                              #if any video exists
                data, fps = gainFrame.frameSeperation(root+'/'+file)
               
                count = 0
                for img_data in data:                           #for moving operation
                    siz = img_data.shape
                    size = [siz[1],siz[0]]
                    img1,img2,img3,img4 = operations.moving(img_data,movingDis,size,outputPath,count)
                    processed1.append(img1)
                    processed2.append(img2)
                    processed3.append(img3)
                    processed4.append(img4)
                    count += 1
                path1 = path + '/' + '1'
                path2 = path + '/' + '2'
                path3 = path + '/' + '3'
                path4 = path + '/' + '4'
                operations.mkdir(path1)
                operations.mkdir(path2)
                operations.mkdir(path3)
                operations.mkdir(path4)
                operations.getVideo(processed1,path1 + '/',numVideo,fps,size) 
                operations.getVideo(processed2,path2 + '/',numVideo,fps,size)
                operations.getVideo(processed3,path3 + '/',numVideo,fps,size)
                operations.getVideo(processed4,path4 + '/',numVideo,fps,size) 


                count = 0
                for img_data in data:                           #for rotation operation
                    processed = operations.rotate(img_data, rotateAng, size, outputPath, count)
                    processed5.append(processed)
                    processed = operations.rotate(img_data, -rotateAng, size, outputPath, count)
                    processed6.append(processed)
                    count += 1
                path5 = path + '/' + '5'
                path6 = path + '/' + '6'
                operations.mkdir(path5)
                operations.mkdir(path6)
                operations.getVideo(processed5,path5 + '/',numVideo,fps,size) 
                operations.getVideo(processed6,path6 + '/',numVideo,fps,size)

                count = 0
                for img_data in data:                           #for scale operations
                    processed = operations.scale(img_data, size, scaleTim[0], outputPath, count)
                    processed7.append(processed)
                    processed = operations.scale(img_data, size, scaleTim[1], outputPath, count)
                    processed8.append(processed)
                    count += 1
                path7 = path + '/' + '7'
                path8 = path + '/' + '8'
                operations.mkdir(path7)
                operations.mkdir(path8)
                operations.getVideo(processed7,path7 + '/',numVideo,fps,size) 
                operations.getVideo(processed8,path8 + '/',numVideo,fps,size)

