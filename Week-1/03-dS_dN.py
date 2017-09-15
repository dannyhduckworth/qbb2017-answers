#!/usr/bin/env python

"""
./03-dS_dN.py <alignment_nuc.fa>

Find dS/dN matches according to the codon alignments. 

"""

import sys
import numpy as np


#I first attempted to write a dictionary for each amino acid before googling resources to speed this process up.


"""
Sourced from:
http://www.petercollingridge.co.uk/python-bioinformatics-tools/codon-table
"""

#Cycles through each combination of three bases (codon) to make all the combinations of the amino acids. Assigns them to a 1-letter code. Stop codons marked as *.
bases = ['T', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

#Split each line into codons
def codon_splitter(sequence, k):
    return [sequence[i:i+k] for i in range(0, len(sequence), k)]

alignmentFile = open(sys.argv[1])

#Skip first line with header
alignmentFile.readline()
#Store first sequence for comparison
firstLine = codon_splitter(alignmentFile.readline(), 3)
dS = np.zeros(len(firstLine))
dN = np.zeros(len(firstLine))

for line in alignmentFile:
    if line[:2] == "gi": #Skip header
        continue
    for index, (codon, ref) in enumerate(zip(codon_splitter(line, 3), firstLine)):
        if codon == ref: #Same codon DNA sequence --> skip
            continue
            
        if not codon in codon_table or not ref in codon_table:
            continue #There was a random Y in the DNA sequence? Did this to circumvent this issue. 
            
        if codon_table[codon] == codon_table[ref]:
            dS[index] += 1 #If codon codes for same aa but is different sequence, add 1 to dS tally
        else:
            dN[index] += 1 #If codon codes for diff aa and is different sequence, add 1 to dN tally
            
diff_list = dN - dS


#Print the codon, dN/dS, and dN-dS.
for i in range(len(firstLine)):
    if dS[i] > 0:
        print("{}\t{}\t{}".format(
            firstLine[i], 
            float(dN[i])/dS[i],
            diff_list[i]))
