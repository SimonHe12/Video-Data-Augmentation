'''
This is the file including different operations
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
from PIL import Image
import os


def moving(img, a, size, path, num):                            #moving image to left, right, up, down
        img1 = img                                              #variable for L,R,U,D
        img2 = img
        img3 = img
        img4 = img

        img5 = np.zeros((size[1],size[0],3), np.uint8)          #back canvas for L,R,U,D
        img6 = np.zeros((size[1],size[0],3), np.uint8)     
        img7 = np.zeros((size[1],size[0],3), np.uint8)     
        img8 = np.zeros((size[1],size[0],3), np.uint8)
        
        img5.fill(255)
        img6.fill(255)
        img7.fill(255)
        img8.fill(255)
                                                                #manipulation of numpy of image
        img1 = img1[:, a*4:]
        img5[ : ,  : size[0]-a*4 ]=img1
        #cv2.imwrite(path + 'mov_zuo%d.png'%num, img1)
        img2 = img2[:, :size[0] - a*4]
        img6[ : , a*4 : ]=img2
        #cv2.imwrite(path + 'mov_you%d.png'%num, img2)
        img3 = img3[a:, :]
        img7[ : size[1]-a , : ]=img3
        #cv2.imwrite(path + 'mov_shang%d.png'%num, img3)
        img4 = img4[:size[1] -a, :]
        img8[ a : , : ]=img4
        #cv2.imwrite(path + 'mov_xia%d.png'%num, img4)
        return img5, img6, img7, img8



def rotate(image, angle, size, path, num):                      #rotate images by angle
        scale=1.0
        (size[1], size[0]) = image.shape[:2]
        center = (size[0] / 2, size[1] / 2)
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(image, M, (size[0], size[1]))
        #cv2.imwrite(path + 'mov%d.png'%num, rotated)
        return rotated
        

def scale(image,size,scale,path,num):                           #scale images
        res = cv2.resize(image,(int(size[0]*scale),int(size[1]*scale)),interpolation=cv2.INTER_CUBIC)
        sp = res.shape
        w = abs(int((size[0]-sp[1])/2))
        h = abs(int((size[1]-sp[0])/2))
        if (scale>1):                                           #if scale up, crop it into origional size
                img = res[:, w : w+size[0]]
                img = img[h : h+size[1], :]
        elif (scale<1):                                         #if scale down, fill void area
                img = np.zeros((size[1],size[0],3), np.uint8)     
                img.fill(255)
                img[h : h+sp[0], w : w+sp[1]]=res
        #final = np.array(im, dtype=numpy.uint8)
        return img



def getVideo(imgs, outpath, num, fps, size):                    #turn frames into a new video
        #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        #videoWriter = cv2.VideoWriter(outpath+'saveVideo%d.avi'%num,fourcc)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        videoWriter = cv2.VideoWriter(outpath+'saveVideo%d.avi'%num,fourcc, fps, (size[0],size[1]))
        for img in imgs:
                videoWriter.write(img)
        videoWriter.release()


def mkdir(path):                                                #make file path
        folder = os.path.exists(path)
        if not folder:
                os.makedirs(path) 







                
