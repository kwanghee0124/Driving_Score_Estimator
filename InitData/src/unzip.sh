#!/bin/bash

main_path=$DSE_PATH
data_path=$main_path/InitData/data/TripFiles

for dir in $data_path/*
do
	cd $dir
	unzip '*.zip'
	rm *.zip
done

