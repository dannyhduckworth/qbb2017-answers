#!/usr/bin/env python

import sys 

fh = sys.stdin


List = []
for line in fh:
    if line[0] == "@":
        continue
    else:
        iMAPQ = line.split("\t")[4]
        fMAPQ = float(iMAPQ)
        List.append(fMAPQ)
    
AvgMAPQ = sum(List)/len(List)

print AvgMAPQ
        

