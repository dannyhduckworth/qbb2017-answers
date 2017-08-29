#!/usr/bin/env python 

import sys

fh = sys.stdin 

counter = 0

for line in fh:
    if line[0] != "@":
        counter += 1
        
print counter