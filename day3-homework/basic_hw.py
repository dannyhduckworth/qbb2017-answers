#!/usr/bin/env python

#Match k-mers of query sequence to target k-mers

#USAGE
#kmer_matcher.py <target.fa> <query.fa> <k>


import sys
import fasta


#Define target and query files
target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])


def kmer_map(input_file, k, get_seq=True):
    """
    Creates dictionary with kmer keys. If get_seq = True, include sequence names and locations. 
    If get_seq = False, only include the sequence location.
    
    input_file: FASTA file
    k: kmer length
    get_seq: Parameter that determines if gene name is included
    returns dictionary of kmery key + values
    """
    kmer_dict = {}
    for ident, sequence in fasta.FASTAReader(input_file): #Execute FASTAreader on query or reference
        sequence = sequence.upper()
        for i in range(0,len(sequence) - k):
            kmer = sequence[i:i+k] #Get k length slice of file
            if get_seq: #If get_seq  = True, include gene name and location
                item = (ident, i)
            else:
                item = i #If gene_seq = False, only include the location. Since only one gene in droYak.
            if kmer not in kmer_dict:
                kmer_dict[kmer] = [item] #Create list at new key
            else:
                kmer_dict[kmer].append(item)
    return kmer_dict


kmer_dict_ref = kmer_map(target, k, get_seq=True) #Set the reference/target dictionary
kmer_dict_query = kmer_map(query, k, get_seq=False) #Set the query dictionary


for kmer, query_locations in kmer_dict_query.iteritems(): #Iterate over the query dictionary
    if kmer in kmer_dict_ref: #Search ref dictionary for query kmer
        for seq_name, ref_loc in kmer_dict_ref[kmer]: #For gene name, location in reference list at particular kmer
            for q_loc in query_locations: #Also take query locations
                print("{}\t{}\t{}\t{}".format(seq_name, ref_loc, q_loc, kmer)) #Make table for all matching results
            