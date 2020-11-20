# %%
import os
import sys
import pandas as pd
from google.cloud import storage

# %%
import geopandas

main_path = os.environ['DSE_PATH']
src_path = main_path + '/InitData/src'
data_path = main_path + '/InitData/data'

credential_path = src_path + '/service-account.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# %%
client = storage.Client()

# %%
buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name)

# %%
blobs = client.list_blobs('vlogger-vocher.appspot.com')
for blob in blobs:
    print(blob.name)
    vehicle_user = blob.name.split('/')[0] + '/' + blob.name.split('/')[1]
    data_dir = data_path + '/' + vehicle_user
    if not(os.path.isdir(data_dir)):
        os.makedirs(os.path.join(data_dir))
    blob.download_to_filename(data_path + '/' + blob.name)

# %%
