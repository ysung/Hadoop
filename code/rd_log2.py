#!/usr/bin/python
import sys
import re

oldKey = None
numTotal = 0
maxNum = 0
maxKey = None
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, num = data_mapped
    if oldKey and oldKey != thisKey:
        # print (oldKey, "\t", numTotal)
        if numTotal > maxNum:
            maxKey, maxNum = oldKey, numTotal
        oldKey = thisKey
        numTotal = 0

    oldKey = thisKey
    numTotal += float(num)

print maxKey, maxNum
# if oldKey != None:
    # print (oldKey, "\t", numTotal)