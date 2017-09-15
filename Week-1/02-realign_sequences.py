#!/usr/bin/env python

"""
./02-realign_sequences.py <1000_homologuemms.fa> <alignment_prot.fa>

Realigns the protein sequence files (which has gaps) to the DNA sequence to introduce gaps in appropriate places.

Utilizes the previously written fasta file.

"""
import itertools
import fasta
import sys


dna_wholefile = open(sys.argv[1])
aa_wholefile = open(sys.argv[2])
alignmentFile = open("alignment_nuc.fa", "w")


#Zip the two (aa and DNA) files together, adding gaps
for (dna_id, dna_seq), (amino_id, amino_seq) in itertools.izip(fasta.FASTAReader(dna_wholefile),
fasta.FASTAReader(aa_wholefile)):
   alignmentFile.write(dna_id + "\n") #Write the DNA indentifier
   for aa in amino_seq: #If there is a gap in the aa seq, introduce a "---"
       if aa == "-":
           alignmentFile.write("---")
       else:
           alignmentFile.write(dna_seq[:3]) #If there is an aa that matches,
           dna_seq = dna_seq[3:] #write the corresponding codon

   alignmentFile.write("\n")