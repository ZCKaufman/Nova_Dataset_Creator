#!/usr/bin/env python3

fileName = ""
videoName = "KM_rps_1_RGB.avi"
outputPath = "/Users/zckaufman/Documents/Work/RHouse/Haru_Dataset/" # INCLUDE output folder. Ex: "/Users/zckaufman/Documents/Work/RHouse/Haru_Dataset/"
labels = ["1", "2", "3"] # Must match labels from CSV
numLabels = len(labels)
mode = "gaze" # Options: gaze, thermal