#!/usr/bin/python

import sys

curr_quant = None
key_quant = []
sum_rev = []

for line in sys.stdin:
    line = line.strip()
    ln = line.split('\t')
    quantity = int(ln[0])
    revenue = int(ln[1])

    # new entry of key-value pair
    if curr_quant != quantity and len(key_quant)==0: 
        key_quant.append(quantity)
        sum_rev.append(revenue)
        curr_quant = quantity
        
    # append values corresponding to existing key
    elif curr_quant == quantity and len(key_quant)==1: 
        sum_rev.append(revenue)

    # when new key appears
    elif curr_quant != quantity and len(key_quant)==1:
        print str.join('\t',(str(quantity), str(sum(sum_rev))))

        key_quant = []
        sum_rev = []

        key_quant.append(quantity)
        sum_rev.append(revenue)
        curr_quant = quantity




