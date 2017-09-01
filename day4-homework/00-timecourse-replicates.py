#!/usr/bin/env python

"""
Usage: ./00-timecourse-replicates.py <samples.csv> <ctab_dir> <replicates file>

-Plot time course of FBtr0331261 for females and males

"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

transcript = "FBtr0331261"

df_samples = pd.read_csv(sys.argv[1]) 
fsoi = df_samples["sex"] == "female"


#Add female samples
f_fpkms = []
for sample in df_samples["sample"][fsoi]: 
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep="\t")
    froi = df["t_name"] == transcript
    f_fpkms.append(df[froi]["FPKM"].values)
    
    


#Add male samples
df_samples = pd.read_csv(sys.argv[1]) 
msoi = df_samples["sex"] == "male"


m_fpkms = []
for sample in df_samples["sample"][msoi]: 
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep="\t")
    mroi = df["t_name"] == transcript
    m_fpkms.append(df[mroi]["FPKM"].values)
    



#Add Stage 14 Replicates
df_replicates = pd.read_csv(sys.argv[3]) 


msoi_replicates= df_replicates["sex"] == "male"


replicates_male = [0,0,0,0]
for sample in df_replicates["sample"][msoi_replicates]: 
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep="\t")
    msoi_replicates = df["t_name"] == transcript
    replicates_male.append(df[msoi_replicates]["FPKM"].values)
    
    

fsoi_replicates= df_replicates["sex"] == "female"


replicates_female = [0,0,0,0]
for sample in df_replicates["sample"][fsoi_replicates]: 
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep="\t")
    fsoi_replicates = df["t_name"] == transcript
    replicates_female.append(df[fsoi_replicates]["FPKM"].values)




#Create Plot

x_tick_labels = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

plt.figure()
plt.plot(replicates_male, 'o', color='b', label="male replicates", markersize=10)
plt.xticks(range(len(x_tick_labels)), ["10", "11", "12", "13", "14A", "14B", "14C", "14D"], rotation=90)
plt.tick_params(
    axis='x',          
    which='both',      
    bottom='off',      
    top='off')
plt.tick_params(
    axis='y',          
    which='both',      
    left='off',      
    right='off')
plt.ylabel('mRNA Abundance (FPKM)', fontsize=15)
plt.xlabel('developmental stage', fontsize=15)
plt.title('Transcriptional Abundance\n of FBtr0331261', fontsize=15, y=1.02)
plt.subplots_adjust(bottom=0.15, right=0.65)


plt.plot(replicates_female, 'ro', label='female replicates', markersize=10)



plt.plot(f_fpkms, 'r-', label='female', linewidth=5)


plt.plot(m_fpkms, 'b-', label='male', linewidth=5)
plt.legend(frameon=False, bbox_to_anchor=(1.65, 1.00), numpoints=1)


plt.savefig("timecourse_replicates.png")
plt.close()


