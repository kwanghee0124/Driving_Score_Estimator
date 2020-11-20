import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# path setting
main_path = os.environ['DSE_PATH']
data_path = main_path + "/Groundtruth/data"
refine_path = main_path + "/RefineData/data" 
refine_file = refine_path + "/refine_file+overspeed.csv"

# def - remap function
def remap(old_value, in_min, in_max, out_min, out_max):
    return (old_value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Input argv
norm_dist = sys.argv[1].split(',')[0] # normalization
weight = sys.argv[2].split(',') # dsi weight

# Read data file
data = pd.read_csv(refine_file)
data_f = data[['overspeed','accel','decel','stop','start']].copy() * 100 # visual

# Normalization
dist = data['distance'].copy() / int(norm_dist) # 10km

data_f['overspeed'] = (data_f['overspeed'] / dist)
data_f['accel'] = (data_f['accel'] / dist)
data_f['decel'] = (data_f['decel'] / dist)
data_f['stop'] = (data_f['stop'] / dist)
data_f['start'] = (data_f['start'] / dist)

# DSI weight
data_f['overspeed'] = round(data_f['overspeed'] * float(weight[0]))
data_f['accel'] = round(data_f['accel'] * float(weight[1]))
data_f['decel'] = round(data_f['decel'] * float(weight[2]))
data_f['stop'] = round(data_f['stop'] * float(weight[3]))
data_f['start'] = round(data_f['start'] * float(weight[4]))

# Feature sum
data_f['dsi'] = data_f.sum(axis=1)

# Score mapping
new_value = []
for i in data_f['dsi']:
    new_value.append(round(remap(i, min(data_f['dsi']), max(data_f['dsi']), 100, 1), 0))
data_f['score'] = new_value

# Score csv save
data_f.to_csv(data_path + "/dsi_score.csv", header=True, index=False)
