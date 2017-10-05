#!/usr/bin/env python

"""
./01-plot.py <vcf> <plot name>

Plot allele frequency spectrum of identified variants
"""


import sys
import itertools
import matplotlib.pyplot as plt


alleleFile = open(sys.argv[1])


alleles = []


#Find the AF value and plot the frequency
for line in alleleFile:
   if line.startswith("#"): #Skip header information
       continue
   row = line.rstrip("\t\n").split() #Strip the row
   
   
   
   af_value = row[7][3:] #Keep information in 8th column
   af_split = af_value.split(",")
   for af in af_split:
       alleles.append(float(af)) #Append these AF values to the list
       


plt.figure()
plt.hist(alleles, bins=100, color="yellow", linewidth=1.2, edgecolor='black')
plt.xlabel('Allele')
plt.ylabel('Frequency')
plt.title('Allele Spectrum of Variants')
plt.savefig(sys.argv[2] + ".png")
plt.close()