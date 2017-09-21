#!/usr/bin/env python





"""
./test.py <dotplot.tsv>
"""

#Line up the sequences for plotting (the counter trick)
#Remove duplicates


import sys
import fasta
import itertools
import matplotlib.pyplot as plt

data = open(sys.argv[1])




plt.figure()

count = 0


#Skip the header
#Use x1 = start, x2 = end
#Use y1 = start at 0, y2 = each successive contig length

#Counter adds each successive contig length so that they stack correctly    
for value in data:
    if "start1" in value:
        continue
    else:
        fields = value.split("\t")
        plt.plot([int(fields[0]), int(fields[2])], [count, count + int(fields[1])])
        
        count += int(fields[1])
        
        
    


plt.xlabel("Position")
plt.ylabel("Contig")
plt.title("Nano Spades")
plt.xlim(0,100000)
plt.ylim(0, 200000)
plt.savefig( "spades_better_plot" + ".png")
plt.close()