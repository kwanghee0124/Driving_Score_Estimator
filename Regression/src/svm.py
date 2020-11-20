import os
import sys
import numpy as np
import pandas as pd

import sklearn.svm as svm
from sklearn.preprocessing import StandardScaler as SScaler
from sklearn.model_selection import train_test_split as split
from sklearn.metrics import mean_squared_error
from math import sqrt

# path setting
main_path = os.environ['DSE_PATH']
data_path = main_path + "/Regression/data"
GtM_path = main_path + "/Groundtruth/data"
dsi_file = GtM_path + "/dsi_score.csv"
hca_file = GtM_path + "/hca_score.csv"
kmeans_file = GtM_path + "/kmeans_score.csv"

# Input argv
GtM = sys.argv[1] # Groundtruth Model

# Read data file
if GtM == "dsi":
    data = pd.read_csv(dsi_file)
elif GtM == "hca":
    data = pd.read_csv(hca_file)
elif GtM == "kmeans":
    data = pd.read_csv(kmeans_file)

X = data[['overspeed','accel','decel','stop','start']]
Y = data['score']

# Standard Scaler
scaler = SScaler()
scaler.fit(X)
X_scaler = scaler.transform(X)

# Data split
train_f, test_f, train_s, test_s = split(X_scaler, Y, test_size=0.3, random_state=0)

# Model: SVM
model = svm.SVC(kernel='linear', C=9, random_state=0)
model.fit(train_f, train_s)
pred = model.predict(test_f)

# RMSE(Root Mean Squared Error)
RMSE = sqrt(mean_squared_error(test_s, pred))

estimate = pd.DataFrame({"predict":pred, "target":test_s})
estimate.to_csv(data_path + "/svm_estimate.csv")

# print RMSE
print("RMSE: {:.2f}".format(RMSE))
