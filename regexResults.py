#!/usr/bin/python3
import re
pattern = re.compile(r'^[\d]{4,4}\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+).*$') #Regex
f = open("./results.csv","r") #Open file
#Compare all lines of file
for line in f:
    res = re.match(pattern, line) #each line is compare with the pattern
    if res:
        total = int(res.group(3)) + int(res.group(4))
        if total > 20:
            print("{} [{} - {}] {}".format(res.group(1),res.group(3),res.group(4),res.group(2)))
f.close()
