#!/usr/bin/env python

"""
./04-dSdN_plot.py <dS_dN_ratio.txt> <plot_name>

Plot dS/dN values on a scatter plot. 

"""


import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np

#P value normally set at 0.05
P_VAL = 0.05


df = pd.read_csv(sys.argv[1], sep = "\t", header=None, names=["codon", "dNdS", "diff"])


x = range(len(df))
y = df["dNdS"]
# m = np.mean(df["diff"])
# std = np.std(df["diff"])


#Find Z-values and p-values
#Z-value: measure of standard deviation
#P-value: probability that value could have been caused by random chance
zvals = sp.zscore(df["diff"])
#Convert z-val to p-val using cumul. dist. function.
#2 for two-tailed curve. -1 to convert upper part of curve to lower half.
pvals = 2 * sp.norm.cdf(-1 * np.abs(zvals))

#Assign pairing of codon to dN/dS based on significance
s_x = [i for i in range(len(pvals)) if pvals[i] < P_VAL]
s_y = [y[i] for i in s_x]
ns_x = [i for i in range(len(x)) if not i in s_x]
ns_y = [y[i] for i in ns_x]



plt.figure()
plt.scatter(ns_x,ns_y, s=2)
plt.scatter(s_x,s_y, s=2, c='r')

plt.title("Sequence Alignment and Evolution Comparison")
plt.xlabel("Codon Count #")
plt.ylabel("dN/dS", rotation = 90)

plt.savefig(sys.argv[2] + ".png")
plt.close()
