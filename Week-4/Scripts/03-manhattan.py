#!/usr/bin/env python

"""
./03-manhattan.py <plink2> <plot name>

Make Manhattan plots of the 46 conditions.
"""


import sys
import numpy as np
import matplotlib.pyplot as plt


pheno = open(sys.argv[1])

p_sig = []
p_notsig = []

for p in pheno:
    line = p.split()
    if 'CHR' in line or 'NA' in line:
        continue
    val = -np.log10(float(line[8]))
    if float(line[8]) <= 10e-5:
        p_sig.append(val)
    else:
        p_notsig.append(val)



plt.figure()
#X-axis is the entire length of the list.
#Y-axis is the actual -log10 p value. 
plt.scatter(range(len(p_sig)), p_sig, s=3, alpha = 0.5, c="purple")
plt.scatter(range(len(p_notsig)), p_notsig, s=3, alpha = 0.5, c="gray")

plt.ylabel("-log10 p value")
plt.xlabel("Gene Location")

plt.savefig(str(sys.argv[2]) + "_manhattan_plot.png")
plt.close()

pheno.close()