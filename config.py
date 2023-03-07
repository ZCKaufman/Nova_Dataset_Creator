#!/usr/bin/env python3

fileName = "" # Include extension
videoName = "" # Include extension
delimiter = "" # Change to relevant delimiter (most likely "," or ";")
outputPath = "" # Include output folder and trailing /. Ex: "/Users/zckaufman/Documents/Work/RHouse/Haru_Dataset/"
labels = ["Activity", "SDK Monitor", "Robot", "Look at Leigh"] # Must match labels from CSV
numLabels = len(labels)
mode = "gaze" # Options: gaze, thermal