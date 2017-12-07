#!/usr/bin/env python


"""
./00-heatmap.py abundance_table.tab


"""


import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt



data = pd.read_csv(sys.argv[1], sep="\t", index_col=0)[['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']]


bin_names = {"bin.1": "S. haemolyticus", "bin.2": "L. citreum", "bin.3": "S. lugenesis", "bin.4": "E. faecalis", "bin.5": "C. avidum", "bin.6": "S. epidermis", "bin.7": "S. aureus", "bin.8": "A. prevotii"}

genome_names = [bin_names[bin] for bin in data.index]

def heatmap_plot(abundances, ylabel, xlabel):
	plt.figure()
	plt.imshow(abundances, aspect="auto", interpolation="nearest")
	plt.colorbar()
	plt.grid(False)
	plt.title("Genome 8 Days Post Birth")
	plt.xticks([x for x in range(len(xlabel))], xlabel, rotation="vertical")
	plt.xlabel("Day")
	plt.ylabel("Bacteria")
	plt.yticks([x for x in range(len(ylabel))], ylabel)
	plt.tight_layout()
	plt.savefig("genome_heatmap.png")
	plt.close()


heatmap_plot(data, genome_names, data.columns)


