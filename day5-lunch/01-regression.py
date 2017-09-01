#!/usr/bin/env python

"""
Usage: ./01-regression.py <histone.tab> <histone.tab> <histone.tab> <histone.tab> <c_tab>


"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import statsmodels.formula.api as sm



#Import the histone tab files for means
h3k36 = pd.read_csv(sys.argv[1], sep="\t", index_col=0, header=None)
h3k9 = pd.read_csv(sys.argv[2], sep="\t", index_col=0, header=None)
h3k4 = pd.read_csv(sys.argv[3], sep="\t", index_col=0, header=None)
h3k27 = pd.read_csv(sys.argv[4], sep="\t", index_col=0, header=None)


#Import c_tab file for FPKMs
c_tab = pd.read_csv(sys.argv[5], sep="\t", index_col="t_name")



#Concat the histone means and the FPKMs. 
concat = pd.concat ( ((h3k36[5]), (h3k9[5]), (h3k27[5]), (h3k4[5]), c_tab["FPKM"]), 1, join = "inner")


#Create model from Y's = FPKMs, X's = histone means
model = sm.OLS(concat["FPKM"], concat.iloc[:,:4])
results = model.fit()
print(results.summary())


