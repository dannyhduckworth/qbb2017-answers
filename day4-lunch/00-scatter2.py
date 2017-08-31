#!/usr/bin/env python

"""
Usage: ./00-scatter2.py <ctab1> <ctab2> <chart file>

-Plot the FPKM data of one ctab file vs another FPKM ctab file. 
-Edit axes, titles, etc. 
-Add a line of best fit. 


# ./00-scatter2.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/
results/stringtie/SRR072915/t_data.ctab scatter

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df1 = pd.read_csv(sys.argv[1], sep="\t")
df2 = pd.read_csv(sys.argv[2], sep="\t")
     


plt.figure()

plt.scatter(numpy.log1p(df1["FPKM"]), numpy.log1p(df2["FPKM"]), alpha=0.5, c="green")

plt.plot(numpy.unique(numpy.log1p(df1["FPKM"])), numpy.poly1d(numpy.polyfit((numpy.log1p(df1["FPKM"])), (numpy.log1p(df2["FPKM"])), 1))(numpy.unique(numpy.log1p(df1["FPKM"]))))

plt.xlabel("SRR072893")
plt.xlim(min(numpy.log1p(df1["FPKM"]))+0.1, max(numpy.log1p(df1["FPKM"]))+0.1)
plt.ylim(min(numpy.log1p(df2["FPKM"]))+0.1, max(numpy.log1p(df2["FPKM"]))+0.1)
plt.ylabel("SRR072915")
plt.title("FPKM Scatter Plot")




plt.savefig(sys.argv[3] + ".png")
plt.close()



