#!/usr/bin/env python

import sys

fh = sys.stdin

counter = 0

for line in fh:
    if "NH:i:1" in line:
        counter += 1

print counter