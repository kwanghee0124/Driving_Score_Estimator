#!/bin/bash

# path setting
main_path=$DSE_PATH
data_path=$main_path/RefineData/data
refine_file=$data_path/refine_file.csv

if [ -e $refine_file ]; then
	rm $refine_file
fi
touch $refine_file
echo "user,trip,accel,decel,stop,start,distance" >> $refine_file

for dir in $data_path/RefineFiles/*
do
	user=`echo "${dir#*RefineFiles/}"`
	echo $user

	for file in $dir/*
	do
		trip=`echo "${file#*$user/}" | cut -d'.' -f1`
		
		line=`tail -n1 $file`
		
		acc=`echo "$line" | cut -d"," -f4`
		acc=`echo "${acc//\"}"`
		
		dec=`echo "$line" | cut -d"," -f5`
		dec=`echo "${dec//\"}"`
		
		sstop=`echo "$line" | cut -d"," -f6`
		sstop=`echo "${sstop//\"}"`
		
		sstart=`echo "$line" | cut -d"," -f7`
		sstart=`echo "${sstart//\"}"`

		dist=`echo "$line" | cut -d"," -f8`
		dist=`echo "${dist//\"}"`


		echo "$user,$trip,$acc,$dec,$sstop,$sstart,$dist" >> $refine_file
		
	done
done
