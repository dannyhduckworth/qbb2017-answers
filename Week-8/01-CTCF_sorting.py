#!/usr/bin/env python

"""
./01-CTCF_sorting.py <ctcf_peaks.tsv> <Nora_Primers.bed>

Find CTCF overlaps from the given CTCF peaks and the heatmap Nora file. 

"""


import sys
import itertools
import matplotlib.pyplot as plt
import numpy as np


#Define a bunch of functions to extract out the relevant data.

def load_hifive_file(file_path):
    data = np.load(file_path)
    return data['0.forward'], data['0.reverse'], data['0.enrichment']



#Find CTCF binding sites on the X Chrom only. Append position [0].
def parse_ctcf_positions(file_path):
    bind_sites = []
    fd = open(file_path, 'r')
    for line in fd:
        fields = line.rstrip('\r\n').split('\t')
        if fields[0] == 'chrX':
            ctcf_bind_sites.append(fields[1])
    fd.close()
    return bind_sites


#Find index of sites in each primer.
def ctcf_index(primer_list, sites_list):
    index_list = []
    for i, primer in enumerate(primer_list):
        start, stop = int(primer[0]), int(primer[1])
        for site in sites_list:
            if int(site) >= start and int(site) <= stop:
                index_list.append(i)
                break
    return index_list    

#Get the primers.
def parse_primers(file_path):
    primer_dict = {}
    fd = open(file_path, 'r')
    for line in fd:
        fields = line.rstrip('\r\n').split('\t')
        if fields[0] != '#chr':
            primer_dict[fields[1] + '_' + fields[2]] = fields[3]
    fd.close()
    return primer_dict



#Find the strongest match if the reverse to the forward.
def ctcf_pairs(fwd_list, rev_list, enr):
    pair_list = []
    for fwd in fwd_list:
        top_rev = None
        top = 0.
        for rev in rev_list:
            if float(enr[fwd][rev]) > top:
                top_rev = rev
                top = float(enr[fwd][rev])
        pair_list.append((fwd, top_rev))
    return pair_list



#Match names
def find_name_matches(fwd, rev, pair_list, primer_dict):
    for match in pair_list:
        fwd_key = str(fwd[match[0]][0]) + '_' + str(fwd[match[0]][1])
        rev_key = str(rev[match[1]][0]) + '_' + str(rev[match[1]][1])
        print '%s\t%s' % (primer_dict[fw_key], primer_dict[rev_key])



#Do all the functions
if __name__ == "__main__":
    #All the relevant data
    ctcf_bind_sites = parse_ctcf_positions(sys.argv[1])
    fwd, rev, enr = hifive_data('Out_enrich.heat.npz')
    primer_dict = parse_primers(sys.argv[2])
    #Match the indices 
    fwd_list = ctcf_index(fwd, ctcf_bind_sites)
    rev_list = ctcf_index(rev, ctcf_bind_sites)
    #Top interacting CTCF pairs
    pairs = ctcf_pairs(fwd_list, rev_list, enr)
    #Matches to their names
    find_name_matches(fwd, rev, pairs, primer_dict)

