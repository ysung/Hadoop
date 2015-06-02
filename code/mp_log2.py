#!/usr/bin/python

import sys
import re

num = 0

for line in sys.stdin:
    match = re.match("^(.*)\s(.*)\s(.*)\s(\[.*\])\s\".*\s(.*)\s.*\"\s(\d+)\s(\.*)", line.strip())
    if match:
        data = match.groups()
        if len(data) == 7:
            # ip, identity, username, time, request, status, size = data
            ip, identity, username, time, path, status, size = data
            m = re.match("^(http://www.the-associates.co.uk)(.*)", path)
            if m:
                print "{0}\t{1}".format(m.group(2), 1)
            else:
                print "{0}\t{1}".format(path, 1)

