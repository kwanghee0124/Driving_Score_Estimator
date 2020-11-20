import pandas as pd
import os, sys
import csv
from pathlib import Path


"""사용 변수 정리
main_dir : overspeed 메인 디렉토리
user_dir : 차량 데이터 디렉토리
gps_dir: gps 데이터
db_dir : db 데이터
data_dir : 차량 데이터csv 파일 위치
over_speed : 과속 횟수
over_flag : 과속 플래그
over_distance : 과속 거리
start_over : 과속 시작 거리
end_over : 과속 종료 거리
start_time : 과속 시작 시간
end_time : 과속 종료 시간
total = 0 : log 개수
"""
main_path = os.environ['DSE_PATH']
data_path = main_path + "/Overspeed/data"
data_file = data_path + "/Output/overspeed.csv"
gps_file = data_path + "/Input/gps.csv"
db_file = data_path + "/Input/db.csv"
refine_path = main_path + "/RefineData/data/RefineFiles"
refine_dir = sys.argv[1]

over_speed = 0
over_flag = 0
over_distance = 0
temp = 0
start_over = 0
end_over = 0
start_time = 0
end_time = 0
total = 0

"""차량데이터, GPS 파일

data : 차량 데이터
gps : GPS 파일
db : GPS 파일
"""

data=open(refine_dir)
gps=pd.read_csv(gps_file, encoding='CP949')
db=pd.read_csv(db_file, encoding='CP949')

read_data = data.readline()
read_data = data.readline()
temp_data = gps[1==gps['id']]


"""데이터 선택 및 분류
"""

while 1:
    read_data = data.readline()
    split_data=read_data.split("\"")

    """예외 처리
    """

    if not read_data:
        break
    if(len(split_data)<38):
        continue
    if(split_data[37]==','):
        continue
    if(split_data[37]=='longitude'):
        continue

    split_data[37]=split_data[37][ :8]

    if(split_data[37]==''):
        continue
    temp=float(split_data[37])
    split_data[37]=temp
    split_data[35]=split_data[35][ :7]
    temp=float(split_data[35])
    split_data[35]=temp

    """gps 탐색
    """

    sel_data = gps[(split_data[37]-0.0001<gps['long']) & (gps['long']<split_data[37]+0.0001)].copy() # 가까운 도로 탐색
    sel_temp = sel_data[(split_data[35]-0.0001<sel_data['lat']) & (sel_data['lat']<split_data[35]+0.0001)].copy()

    if sel_temp.empty:
        sel_temp = temp_data.copy()

    if len(sel_temp)>3:
        sel_temp=temp_data.copy()

    sel_data = sel_temp.copy()
    total = total+len(sel_data)

    if len(sel_data)>1:
        sel_dataframe = sel_data.iloc[0].copy()
    else:
        sel_dataframe = sel_data.copy()

    if str(type(sel_dataframe)) == "<class 'numpy.float64'>":
        sel_dataframe = temp_data.copy()
        
    sel_row = int(sel_dataframe['id'].copy()) #선택된 도로 id와 매칭하여 MAX_SPD와 도로명 추출
    sel_id = db.iloc[sel_row, :].copy()
    MAX_SPD = int(sel_id['MAX_SPD'].copy())
    ROAD_NAME = sel_id['ROAD_NAME']
    temp_data = sel_dataframe.copy()

    split_data[1] = float(split_data[1])
    split_data[3] = int(split_data[3])
    split_data[15] = float(split_data[15])
    split_data[35] = str(split_data[35])
    split_data[37] = str(split_data[37])

    if(MAX_SPD == 0):
        continue
	
    """과속 분류
    """

    if(split_data[3] > ((MAX_SPD*1.2) - 5)): #과속 비교
        if(over_flag == 0 and start_over == 0):
            start_time = split_data[1]
            over_flag = 1
            start_over = split_data[15]

    if(over_flag == 1 and split_data[3] < ((MAX_SPD * 1.2) - 5)):
        end_time = split_data[1]
        if((end_time - start_time)< 3000):
            over_speed -= 1
        end_over = split_data[15]
        over_distance = over_distance + (end_over - start_over)
        start_over = 0
        end_over = 0
        over_flag = 0
        over_speed += 2
print()

"""과속 여부를 판단한 데이터를 csv 파일에 저장
"""
user_split = PATH_data.split('/')
user_split2 = user_split[len(user_split)-1].split('.')

result = open(data_file, 'a', encoding='utf-8', newline="")

writer = csv.writer(result)
writer.writerow([user_split[len(user_split)-2], user_split2[0], over_speed])
result.close()
