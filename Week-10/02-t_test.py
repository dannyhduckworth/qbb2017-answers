#!/usr/bin/env python


"""
./02-t_test.py <hema_data.txt>


"""



import sys
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from sklearn.cluster import KMeans


#Make functions tro find early/late averages and t-test
#This will look similar to Max's because he helped me a lot on this section, especially in understanding how to use functions to do this.

def avg_early_late(early_genes, late_genes):
	data = pd.read_csv(sys.argv[1], sep="\t")
	data["avg_early"] = data[early_genes].mean(axis=1)
	data["avg_late"] = data[late_genes].mean(axis=1)
	return data

def t_test(averages, early_genes, late_genes):
	averages["ratio_early_late"] = averages["avg_early"]/averages["avg_late"]
	stats, averages["p-values"] = ttest_ind(averages[early_genes], averages[late_genes], axis=1)
	# print averages[early_genes]
	# print p_val
	# return p_val
	return averages.mask(averages["p-values"]>0.05).dropna(how="any")
	# averages = averages.mask(averages["ratio_early_late"]>0.5.dropna(how="any")


#Find the most significant gene based on the avg ratio.
def get_upreg_max(data):
	
	return data.loc[data["ratio_early_late"].idxmax()]




if __name__ == "__main__":
	#Genes chosen based on dendrogram. CFU was the earliest. Poly and unk were the latest.
	early_genes = ["CFU"]
	late_genes = ["poly", "unk"]
	average_values = avg_early_late(early_genes, late_genes)
	t_test_stats = t_test(average_values, early_genes, late_genes)
	print t_test_stats["gene"]
	max_gene = get_upreg_max(average_values)
	print max_gene

	







