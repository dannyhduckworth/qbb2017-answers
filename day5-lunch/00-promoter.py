#!/usr/bin/env python

"""
Usage: ./00-promoter.py <stringtie_ctab>

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA

#Import stringtie files
df= pd.read_csv(sys.argv[1], sep="\t")


#Create conditionals that determine +/- 
coi = ["chr", "start", "end", "t_name"]
coi_plus = df["strand"] == "+"
coi_minus = df["strand"] == "-"

#Create dataframe for the + strands. +/- 500 bp from start
df_f = pd.DataFrame()
for strand in df[coi][coi_plus]:
    df_f["chr"] = df["chr"][coi_plus]
    df_f["start"] = df["start"][coi_plus] - 500
    df_f["end"] = df["start"][coi_plus] + 500
    df_f["t_name"] = df["t_name"][coi_plus]
   
#Create dataframe for the - strands. +/- 500 bp from end.  
df_b = pd.DataFrame()
for strand in df[coi][coi_minus]:
    df_b["chr"] = df["chr"][coi_minus]
    df_b["start"] = df["end"][coi_minus] - 500
    df_b["end"] = df["end"][coi_minus] + 500
    df_b["t_name"] = df["t_name"][coi_minus]
    
    
#Append the two dataframes   
df_final = df_f.append(df_b)

#print df_final
    
#Exclude negative values  
positive_hit = df_final["start"]  >= 0 
df_ult = df_final[positive_hit]


#Report final dataframe of promoter regions
df_ult.to_csv("promoter.bed", "\t", header=False, index=False)


#














  
  

    

 