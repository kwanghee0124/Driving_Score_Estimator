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
|   |   ├─ refine_overspeed.csv
|   |   └─ RefineFiles
|   └─ src
|       ├─ refine_classified.sh
|       ├─ refine_pars.sh
|       └─ refine_overspeed.py
├─ Overspeed
|   ├─ data
|   |   ├─ db.csv
|   |   ├─ gps.csv
|   |   └─ overspeed.csv
|   └─ src
|       ├─ initial_data.py
|       └─ overspeed.py
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
    |	└─ svm_estimate.csv
    └─ src
        ├─ rf.py
        └─ svm.py
```

|Directory|Explanation|
|---------|-----------|
|InitData| TripFiles Download and unzip |
|RefineData| Classify the data using normalized values and create a refined refine_file.csv file |
|Overspeed| Counts the number of overspeed by comparing the user's driving DB with the road information DB |
|Groundtruth| Using clustering algorithms, we create groundtruth to be used in the driving score |
|Regression| Groundtruth-based Driving Score Estimate is performed using regression algorithms |


|Source code|Explanation|Data|
|----|-----------|------|
|README.md|||
|config.sh| Enables configurations and install at once ||
|Estimator.sh| All programs can be executed ||
|vlogger.py| Download TripFiles from Firebase |TripFiles|
|unzip.sh| TripFiles: trip file unzip |unzip TripFiles|
|service_account.json| Google Storage account file ||
|refine_classified.sh| Classify TripFiles according to conditions |RefineFiles|
|refine_pars.sh| Create as 1 usable file |refine_file.csv|
|refine_overspeed.py| refine_file data + overspeed_file data |refine_overspeed.csv|
|initial_data.py| Detects the overspeed of all trips inside Tripfiles and creates initial data ||
|overspeed.py|  Detects the overspeed of a one trip and adds data to overspeed.csv |overspeed.csv|
|dsi.py| DSI code for making Groundtruth |dsi_score.csv|
|hca.py| HCA code among Clustering Algorithms for making Groundtruth |hca_score.csv|
|kmeans.py| kmeans code among Clustering Algorithms for making Groundtruth |kmeans_score.csv|
|rf.py| Random Forest code among Regression Algorithms for Driving Score Estimate |rf_estimate.csv|
|svm.py| Support Vector Machine code among Regression Algorithms for Driving Score Estimate |svm_estimate.csv|


## Configuration and Install

Configuration and API Install code.

	# sudo source config.sh


## Estimator

**Usage Help**
	
	# ./Estimator.sh -h

or

	# ./Estimator.sh -?

**Program**

	# ./Estimator.sh -p [Select]

**Normalization**

	# ./Estimator.sh -n [Distance,Conunt]

**Groundtruth Model**

	# ./Estimator.sh -g [Model]

 When selecting DSI among the groundtruth models, the weight value must be entered.  
The corresponding options are:

	# ./Estimator.sh -g dsi -w [overspeed,accel,decel,stop,start]

**Regression Model**

	# ./Estimator.sh -r [Model]


## Contact
**Dankook University**

**Kwanghee Lee**  
E-main - _kwanghee0124@dankook.ac.kr_

**Sounghyoun Lee**  
E-mail - _leesh812@dankook.ac.kr_

