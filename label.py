#!/usr/bin/env python

import config as cfg
import cv2
import math
import os
import sys

def configCheck():
    print("--- Checking and running configuration from config.py ---")

    # Check output path
    #if(cfg.outputPath and cfg.outputPath != ""):
    #    print("CONFIG: Output path exists and is not empty")
    #else:
    #    return False

    if os.path.exists(cfg.outputPath) and not os.path.isfile(cfg.outputPath):
        print("CONFIG: Output path exists")
        if os.listdir(cfg.outputPath):
            print("CONFIG: Output path found but is not empty. Output path must be empty. Terminating program.")
            sys.exit()
        else:
            print("CONFIG: Output path is empty")
    else:
        print("CONFIG: Output path either does not exist or is a file. Output path must exist and be a directory.\nTerminating program.")
        sys.exit()

    # Check and create labels
    if(cfg.numLabels <= 0):
        return False
    else:
        print("CONFIG: Labels found")
    for i in cfg.labels:
        path = os.path.join(cfg.outputPath, i)
        os.mkdir(path)
        print("CONFIG: Created label -", i)
    print("CONFIG: All found labels created")

    return True

def label():
    capture = cv2.VideoCapture('videos/' + cfg.videoName)
    i = 0
    timestamp = 0.0
 
    while (True):
 
        success, frame = capture.read()
 
        if success:
            cv2.imwrite(cfg.outputPath + "{:02d}_{:02d}.jpg".format(math.floor(timestamp), math.floor(timestamp % 1 * 100)), frame)
        else:
            break
        
        timestamp = timestamp + 0.0667
        if(math.floor(timestamp) == i): 
            i = i+1
            print("{:.1f} Seconds Converted".format(timestamp))
 
    capture.release()
    return

if __name__ == '__main__':
    #if configCheck():
    label()
     #   print("Labeling complete. Output images with labels can be found at: ", cfg.outputPath)
   # else:
    #    print("Config file not complete. Please give all variables a value in config.py.")