#!/usr/bin/env python


"""

./00-KRAKEN_to_KRONA.py <kraken file>

"""

# awk '{gsub ("_","\t")}{print}' oldfile.kraken > newfile.kraken

import sys
import numpy as np


krakenFile = open(sys.argv[1])

counts = {}

#Count the number of times each ID occurs.
#Strip each line by tabs.
#Look at the first column.
#Count the number of the same IDs. 

for line in krakenFile:
	stripped = line.rstrip("\n").split("\t")

	column1 = stripped[0]
	column2 = stripped[1]

	if column2 not in counts:
			counts[column2] = 1
	else:
			counts[column2] += 1

# print counts



for t in counts:
	print str(counts[t]) + "\t" + "\t".join(t.split(";"))











