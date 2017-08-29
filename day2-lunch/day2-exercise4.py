#!/usr/bin/env python

import sys

fh = sys.stdin

           
count = 0
for line in fh:
    if line[0] != "@":
        print line.split('\t')[2]
        count += 1
        if count >= 10:
            break
        
        