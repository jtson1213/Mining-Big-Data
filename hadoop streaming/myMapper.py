#!/usr/bin/python
import sys, datetime

lst = []

for line in sys.stdin:
    line = line.strip()
    vals = line.split('|')
    quantity = int(vals[8])
    discount = int(vals[11])
    revenue = int(vals[12])

    if discount<3:
        output = [quantity, revenue]
        lst.append(output)

lst.sort()
for i in range(len(lst)):
    print str.join('\t',(str(lst[i][0]), str(lst[i][1])))
    
