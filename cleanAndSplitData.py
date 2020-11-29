import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# split data for train and test
lines = []
with open("agedetector_group_train.v1.0.txt", "r") as f:
  line = f.readline()
  while line:
    lines.append(line)
    line = f.readline()

len(lines)

import random
def splitData(dataSet, ratio):
  trainSize = int (len(dataSet) * ratio)
  trainSet = []
  dataSetCopy = list(dataSet)
  while len(trainSet) < trainSize:
    index = random.randrange(len(dataSetCopy))
    trainSet.append(dataSetCopy.pop(index))
  return [trainSet, dataSetCopy]

trainSet = []
testSet = []
trainSet, testSet = splitData(lines, 0.7)

len(trainSet)

len(testSet)

with open("trainSet.txt", "w") as f:
  for line in trainSet:
    f.writelines(line)

# convert txt to csv
# https://stackoverflow.com/questions/39642082/convert-txt-to-csv-python-script
import csv
with open("trainSet.txt", "r") as f:
    stripped = (line.strip() for line in f)
    lines = (line.split(" ", 1) for line in stripped)
    with open("trainSet.csv", "w") as out_file:
      writer = csv.writer(out_file)
      writer.writerow(('title', 'data'))
      writer.writerows(lines)

with open("testSet.txt", "w") as f:
  for line in testSet:
    f.writelines(line)
with open("testSet.txt", "r") as f:
    stripped = (line.strip() for line in f)
    lines = (line.split(" ", 1) for line in stripped)
    with open("testSet.csv", "w") as out_file:
      writer = csv.writer(out_file)
      writer.writerow(('title', 'data'))
      writer.writerows(lines)
