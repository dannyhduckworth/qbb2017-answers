#!/usr/bin/env python


"""
./03-k_means_clustering.py <hema_data.txt>


"""

#Again, Max helped me out a ton in writing these functions. 


import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

#This code is to take the k means clusters and produce a heatmap.

def cluster (data, labels):
	transposed = np.transpose(data.values)
	#Find linkage values
	linkx, linky = linkage(data.values, method-"average"), linkage(transposed, method="average")
	#Used leaves_list on the linkage sets
	leavesx, leavesy = leaves_list(linkx), leaves_list(linky)
	transformed = data.values[leavesx,:][:, leavesy]
	labels_xy = np.array(labels)[leavesy]
	return transformed, labels_xy, linkx, linky


def k_cluster(X):
	kmeans = KMeans(n_clusters=6, random_state=0)
	kmeans.fit(X)
	labels = kmeans.predict(X)
	X = pd.merge(pd.DataFrame(X), pd.DataFrame(labels, columns=["Cluster"] ), left_index=True, right_index=True )
	return X.sort_values('Cluster')[['CFU', 'poly', 'unk', 'int', 'mys', 'mid']].values, labels


#Learned how to add the title and labels as inputs, yay! 
def pl_heatmap(title, labels, intensities, save_name):
	plt.figure()
	plt.imshow(intensities, aspect="auto", interpolation="nearest", cmap="plasma")
	plt.colorbar()
	plt.grid(False)
	plt.title(title)
	plt.yticks([])
	plt.xticks(range(6), labels)
	plt.savefig(save_name)
	plt.close()



if __name__ == "__main__":
	data_df = pd.read_csv(sys.argv[1], sep="\t")
	labels = ["CFU", "poly", "unk", "int", "mys", "mid"]
	data = data_df[labels]
	hier_trans, labels_xy, linky, leavesy = cluster(data, labels)
	pl_heatmap("KMeans Heatmap, k=6", labels_xy, hier_trans, "KMeans_Cluster_better.png")
