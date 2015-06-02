#!/usr/bin/python
import sys
import re

oldKey = None
numTotal = 0
oldRequest = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, num = data_mapped
    if oldKey and oldKey != thisKey:
        print (oldKey, "\t", numTotal)
        oldKey = thisKey
        numTotal = 0

    oldKey = thisKey
    numTotal += float(num)

if oldKey != None:
    print (oldKey, "\t", numTotal)