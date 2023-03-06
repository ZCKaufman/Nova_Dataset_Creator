#!/usr/bin/env python

import config as cfg
import cv2

def configCheck():

    return True

def label():
    capture = cv2.VideoCapture('videos/' + cfg.videoName)
    i = 0
    timestamp = 0.0
 
    while (True):
 
        success, frame = capture.read()
 
        if success:
            cv2.imwrite(cfg.outputPath + "{:.2f}.jpg".format(timestamp), frame)
            print(i)
        else:
            break
        
        timestamp = timestamp + 0.04
        i = i+1
 
    capture.release()
    return

if __name__ == '__main__':
    if configCheck():
        label()
        print("Labeling complete. Output images with labels can be found at: ", cfg.outputPath)
    else:
        print("Config file not complete. Please give all variables a value in config.py.")