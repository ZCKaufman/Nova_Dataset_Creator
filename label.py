#!/usr/bin/env python

import config as cfg
import cv2
import math

def configCheck():

    return True

def label():
    capture = cv2.VideoCapture('videos/' + cfg.videoName)
    i = 0
    timestamp = 0.0
 
    while (True):
 
        success, frame = capture.read()
 
        if success:
            #cv2.imwrite(cfg.outputPath + "{}:{:.2f}.jpg".format(math.floor(timestamp), (timestamp % 1) * 100), frame)
            cv2.imwrite(cfg.outputPath + "{:02d}_{:02d}.jpg".format(math.floor(timestamp), math.floor(timestamp % 1 * 100)), frame)
        else:
            break
        
        timestamp = timestamp + 0.0667
        if(round(timestamp, 2) % 1 == 0): 
            print("{:.1f} Seconds Converted".format(timestamp))
        i = i+1
 
    capture.release()
    return

if __name__ == '__main__':
    if configCheck():
        label()
        print("Labeling complete. Output images with labels can be found at: ", cfg.outputPath)
    else:
        print("Config file not complete. Please give all variables a value in config.py.")