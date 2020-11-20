#!/bin/bash

help() {
	echo "Driving Score Estimator Help"
	
	echo -e "\n========Option========"
	
	echo "-p | Program"
	echo -e "\t[ID] InitData"
	
	echo -e "\t[RD] RefineData"
	echo -e "\t\tOption: -n"
	
	echo -e "\t[O] Overspeed"
	echo -e "\t\tOption: -n"

	echo -e "\t[G] Groundtruth"
	echo -e "\t\tOption: -n, -g, [dsi](-w)"
	
	echo -e "\t[R] Regression"
	echo -e "\t\tOption: -g, -r"
	
	echo -e "\tex) -p ID\n"
	
	echo "-n(Option) | Normalization"
	echo -e "\tNormalization distance, Normalization count"
	echo -e "\tex) -n 10000,15\n"

	echo "-g(Option) | Groundtruth Model"
	echo -e "\tGourndtruth Model: dsi, hca, kmeans"
	echo -e "\tex) -g dsi\n"

	echo "-w(Option) | DSI weight"
	echo -e "\toverspeed,accel,decel,stop,start"
	echo -e "\tex) -w 1,1,1,1,1\n"

	echo "-r(Option) | Regression Model"
	echo -e "\tRegression Model: rf, svm"
	echo -e "\tex) -r svm\n"

	exit 0
}

while getopts "p:n:g:w:r:h?" opt
do
	case $opt in
		p) prog=$OPTARG ;;
		n) norm=$OPTARG ;;
		g) gt_model=$OPTARG ;;
		w) weight=$OPTARG ;;
		r) r_model=$OPTARG ;;
		h) help ;;
		?) help ;;
	esac
done

main_path=$DSE_PATH

if [ $prog == "ID" ]; then
	src_path=$main_path/InitData/src

	python3 $src_path/vlogger.py && source $src_path/unzip.sh

elif [ $prog == "RD" ]; then
	src_path=$main_path/RefineData/src
	
	source $src_path/refine_classified.sh $norm && source $src_path/refine_pars.sh

elif [ $prog == "O" ]; then
	src_path=$main_path/Overspeed/src

	

elif [ $prog == "G" ]; then
	src_path=$main_path/Groundtruth/src
	
	case $gt_model in
		dsi) python3 $src_path/dsi.py $norm $weight ;;
		hca) python3 $src_path/hca.py $norm ;;
		kmeans) python3 $src_path/kmeans.py $norm ;;
	esac
elif [ $prog == "R" ]; then
	src_path=$main_path/Regression/src

	case $r_model in
		svm) python3 $src_path/svm.py $gt_model ;;
		rf) python3 $src_path/rf.py $gt_model ;;
	esac
fi
