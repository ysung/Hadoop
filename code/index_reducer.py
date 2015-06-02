#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

oldKey = None
numTotal = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, num = data_mapped
    thisKey = thisKey.lower()
    num = int(num)
    print (thisKey, num)
    if oldKey and oldKey != thisKey:
        print (oldKey, "\t", numTotal)
        if oldKey == "fantastic":
            print (oldKey, num)
        oldKey = thisKey
        numTotal = 0

    oldKey = thisKey
    numTotal += float(num)

# if oldKey != None:
#     print (oldKey, "\t", numTotal)