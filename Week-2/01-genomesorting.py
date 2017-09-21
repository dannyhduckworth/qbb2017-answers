#!/usr/bin/env python

"""
./01-genomesorting.py 

Compute the number of contigs, minimum/maximum/average contig length, and N50

"""


import sys
import fasta


contigFile = open(sys.argv[1])


#Iterate FASTAReader. Extract out the statistics from these sequences. 

contig_lens = []

for dna_id, contig in fasta.FASTAReader(contigFile):
    contig_lens.append(len(contig))
    
minimum = min(contig_lens)
maximum = max(contig_lens)
num_contigs = len(contig_lens)
avg_length = sum(contig_lens) / float(num_contigs)


#Method to find N50. Find the half length and compare to a list summed one item at a time. 
half_len = sum(contig_lens) // 2
count_size = 0
n50 = None

for l in sorted(contig_lens, reverse=True):
    count_size += l
    if count_size >= half_len:
        n50 = l
        break


print "Min {} \n Max {} \n Num Contigs {} \n Avg Length {} \n N50 {}".format(minimum, maximum, num_contigs, avg_length, n50)





