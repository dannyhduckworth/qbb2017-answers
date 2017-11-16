#!/usr/bin/env python


"""
./01-cluster-heatmap.py <hema_data.txt>


"""



import numpy as np
import scipy.cluster as sp
import matplotlib.pyplot as plt
import sys
import pandas as pd
import itertools
from sklearn import datasets
from sklearn.cluster import KMeans


data = pd.read_csv(sys.argv[1], delimiter="\t")
values = data.as_matrix()[:,1:].astype(float)

#Get the values for the rows for the heatmap.
link_data = sp.hierarchy.linkage(values, method="average", metric="euclidean")

#Transpose to find the columnar information for the dendrogram.
link_data_columns = sp.hierarchy.linkage(values.T, method="average", metric="euclidean")
heatmap_index = sp.hierarchy.leaves_list(link_data)
ordered_data = values[heatmap_index,:]
dendrite_label = ["CFU", "poly", "unk", "int", "mys", "mid"]


#Plot the heatmap
plt.figure()
plt.pcolor(ordered_data, cmap="plasma")
ax = plt.gca()
plt.xticks()
plt.grid(False)
plt.title("Heatmap of Iris characteristics")
plt.savefig("heatmap.png")
plt.close()


#Plot the dendrogram
plt.figure()
sp.hierarchy.dendrogram(link_data_columns, labels=dendrite_label)
plt.savefig("dendrogram.png")
plt.close()



#Make the k-clusters and plot as heatmap 
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(values)
labels = kmeans.predict(values)
data_matrix = pd.merge(pd.DataFrame(values, columns = ['CFU', 'poly', 'unk', 'int', 'mys', 'mid']), pd.DataFrame( labels, columns=['cluster'] ), left_index=True, right_index=True )
k_clustered = data_matrix.sort_values('cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values

plt.figure()
plt.imshow(k_clustered, aspect='auto', interpolation='nearest')
plt.grid( False )
plt.title("K-cluster Heatmap")
plt.colorbar()
plt.xticks() 
plt.savefig("k_clustered.png")
plt.close()
