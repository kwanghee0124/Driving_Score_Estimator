import os
import sys
import pandas as pd

main_path = os.environ['DSE_PATH']
refine_path = main_path + "/RefineData/data"
refine_file = refine_path + "/refine_file.csv"
overspeed_path = main_path + "/Overspeed/data"
overspeed_file = overspeed_path + "/overspeed.csv"

refine = pd.read_csv(refine_file).copy()
osf = pd.read_csv(overspeed_file)
overspeed = osf['overspeed'].copy()

refine['overspeed'] = overspeed

refine.to_csv(refine_path + "/refine_overspeed.csv", header=True, index=False)
