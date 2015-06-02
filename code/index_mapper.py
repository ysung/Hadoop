#!/usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    next(reader, None)  # skip the headers
    heap = [] # priority queue, min heap
    dic = {} # hashtable
    dic2 = {}
    for line in reader:
        match = re.findall("\w+", line[4])
        if match:
            for word in match:
                word = word.lower()
                if word not in dic:
                    dic[word] = 1
                    dic2[word] = [float(line[0])]
                else:
                    dic[word] += 1
                    dic2[word] += [float(line[0])]
                    # dic2[word].append(line[0])

    # for key, value in dic.items():
    #     writer.writerow((key, value))
    for key in dic:
        if key == "fantastic":
            writer.writerow((key, dic[key]))
        elif key == "fantastically":
            writer.writerow((key, dic[key]))
    for key in dic2:
        if key == "fantastically":
            writer.writerow((key, sorted(dic2[key])))

# This function allows you to test the mapper with the provided test string
def main():
    # import StringIO
    # sys.stdin = StringIO.StringIO(test_text)
    mapper()
    # sys.stdin = sys.__stdin__

main()
