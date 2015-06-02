#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    oldKey = None
    resultA = None
    resultB = None
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        thisKey = data_mapped[0]
        
        if oldKey and oldKey != thisKey:
            if resultA and resultB:
                print("test")
                result = resultB[2:5] + [resultB[0]] + resultB[5:]+ resultA[2:]
                print (result)
            oldKey = thisKey
            resultA = None
            resultB = None
            
        if len(data_mapped) == 6:
            resultA = data_mapped
            print (resultA)
        
        elif len(data_mapped) == 10:
            resultB = data_mapped
            print (resultB)

        
        oldKey = thisKey

    if oldKey != None:
        if resultA and resultB:
            result = resultB[2:5] + [resultB[0]] + resultB[5:]+ resultA[2:]
            print (result)

def main():
    reducer()

main()