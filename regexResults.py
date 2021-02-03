#!/usr/bin/python3
import re
pattern = re.compile(r'^[\d]{4,4}\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+).*$')
f = open("./results.csv","r")
for line in f:
    res = re.match(pattern, line)
    if res:
        total = int(res.group(3)) + int(res.group(4))
        if total > 20:
            print("{} [{} - {}] {}".format(res.group(1),res.group(3),res.group(4),res.group(2)))
f.close()