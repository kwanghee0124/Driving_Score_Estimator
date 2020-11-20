import glob
import os
import sys
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering as HCA
from scipy.cluster.hierarchy import linkage, dendrogram

import matplotlib.pyplot as plt
import seaborn as sns

# Path setting
main_path = os.environ['DSE_PATH']
data_path = main_path + "/GroundtruthModel/data"
refine_path = main_path + "/RefineData/data" 
refine_file = refine_path + "/refine_file+overspeed.csv"

# Input argv
norm_dist = sys.argv[1].split(',')[0]

# Read data file
data = pd.read_csv(refine_file)
data_f = data[['overspeed','accel','decel','stop','start']].copy() * 100 # visual

# Normalization
dist = data['distance'].copy() / int(norm_dist)

data_f['overspeed'] = (data_f['overspeed'] / dist).astype(int)
data_f['accel'] = (data_f['accel'] / dist).astype(int)
data_f['decel'] = (data_f['decel'] / dist).astype(int)
data_f['stop'] = (data_f['stop'] / dist).astype(int)
data_f['start'] = (data_f['start'] / dist).astype(int)

# Score table: feature sum
score_table = pd.DataFrame({'sum':data_f.sum(axis=1)})

# figure dendrogram set
#link = linkage(data_f, method='complete')

# Model: HCA
model = HCA(n_clusters=100)
pred = model.fit_predict(data_f)
data_f['cluster'] = pred

# Score table: create
score_table['cluster'] = data_f['cluster'].copy()
score_table = score_table.sort_values(by=['sum'])
score_table = score_table.drop_duplicates(['cluster'])
score_table = score_table.drop('sum', axis=1)
score_table['score'] = range(100, 0, -1)

# cluster - score mapping
data_f = pd.merge(data_f, score_table, how='left', on='cluster')

# ---- figure ----
# figure: dendrogram
#dendrogram(link)

# figure: correlation - heatmap
#corr = data_f.corr()
#sns.heatmap(corr, annot=True, fmt='.3f', cmap='RdYlBu_r')

# figure: pairplot
#sns.pairplot(data_f, diag_kind='kde', hue='cluster', palette='bright')

# figure setting - save
#plt.axis([0,25,0,80])
#plt.xlabel("xlabel")
#plt.ylabel("ylabel")
#plt.savefig('figure_name.png')
#------------------

# Score csv save
data_f.to_csv(data_path + "/hca_score.csv", header=True, index=False)
