#!/usr/bin/env python

"""
./01-plot.py <filtered.vcf> <plot name>

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
   af_value = row[7].split(";") #Keep information in 8th column
   af_number = af_value[3][3:] #Keep the actual AF value. 
   af_split = af_number.split(",") #Split the doubvle values with commas
   for af in af_split: #Append these AF values to the list
       alleles.append(float(af))
       


plt.figure()
plt.hist(alleles, bins=25, color="maroon", linewidth=1.2, edgecolor='black')
plt.xlabel('Allele')
plt.ylabel('Frequency')
plt.title('Allele Spectrum of Variants')
plt.savefig(sys.argv[2] + ".png")
plt.close()
    
