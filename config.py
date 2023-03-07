#!/usr/bin/env python3

fileName = "LL_KM_RPS_gaze_12_2.csv"
videoName = "KM_rps_1_RGB.avi"
outputPath = "/Users/zckaufman/Documents/Work/RHouse/Haru_Dataset/" # INCLUDE output folder. Ex: "/Users/zckaufman/Documents/Work/RHouse/Haru_Dataset/"
labels = ["Activity", "SDK Monitor", "Robot", "Look at Leigh"] # Must match labels from CSV
numLabels = len(labels)
mode = "gaze" # Options: gaze, thermal