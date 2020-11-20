import os, sys
import csv
from pathlib import Path

main_path = os.environ['DSE_PATH']
data_path = main_path + "/Overspeed/data"
data_file = data_path + '/Output/overspeed.csv'
refine_path = main_path + "/RefineData/data/RefineFiles"

user=os.listdir(refine_path)
user.sort()

"""초기 데이터 생성"""
result = open(data_file, 'a', encoding='utf-8', newline="")
writer = csv.writer(result)
writer.writerow(['user','trip','overspeed'])
result.close()

for i in range(0, len(user)): 
    print('User - '+user[i]+' start.')
    trip_dir=refine_path+'/'+user[i]
    trip=os.listdir(trip_dir)
    trip.sort() 
    for j in range(len(trip)):
        py_dir='python3 overspeed.py 'refine_path+'/'+user[i]+'/'+trip[j]
        print('Trip - '+trip[j]+' start.')
        os.system(py_dir)
        print('Trip - '+trip[j]+' end.')

    print('User - '+user[i]+' end.')

