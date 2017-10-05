#!/usr/bin/env python

"""
./01-PCA.py <plink.eigenvalue> <plot name>




"""


import matplotlib.pyplot as plt
import pandas as pd
import sys



pcaDF = pd.read_csv(sys.argv[1], sep="\t")




plt.figure()
plt.scatter(pcaDF["PC1"], pcaDF["PC2"], alpha = 0.5, s=1.75)
    
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Analysis")
    
plt.savefig(sys.argv[2] + ".png")
plt.close()






