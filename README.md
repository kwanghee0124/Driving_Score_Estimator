# Driving Score Estimator

## Directory and File Structure

```
.
├─ README.md
├─ config.sh
├─ Estimator.sh
├─ InitData
|   ├─ data
|   |   └─ TripFiles
|   └─ src
|       ├─ service_account.json
|       ├─ unzip.sh
|       └─ vlogger.py
├─ RefineData
|   ├─ data
|   |   ├─ refine_file.csv
|   |   ├─ refine_file+overspeed.csv
|   |   └─ RefineFiles
|   └─ src
|       ├─ refine_classified.sh
|       └─ refine_pars.sh
├─ Overspeed
|   ├─ data
|   |   ├─ db.csv
|   |   ├─ gps.csv
|   |   └─ overspeed.csv
|   └─ src
|       ├─ initial_data.py
|       └─ overspeed.csv
├─ Groundtruth
|   ├─ data
|   |   ├─ dsi_score.csv
|   |   ├─ hca_score.csv
|   |   └─ kmeans_score.csv
|   └─ src
|       ├─ dsi.py
|       ├─ hca.py
|       └─ kmeans.py
└─ Regression
    ├─ data
    |   ├─ rf_estimate.csv
    |   └─ svm_estimate.csv
    └─ src
		├─ rf.py
        └─ svm.py

```

|제목|내용|설명|
|------|---|---|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|

## Configuration and Install

Configuration and API Install code.

    sudo source config.sh


## Estimator


## Contact
**Dankook University**

**Kwanghee Lee**

E-main - _kwanghee0124@dankook.ac.kr_

**Sounghyoun Lee**

E-mail - _leesh812@dankook.ac.kr_ _wwbabaww@gmail.com_

