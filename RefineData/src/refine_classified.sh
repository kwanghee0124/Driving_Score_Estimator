#!/bin/bash

# path setting
main_path=$DSE_PATH
init_path=$main_path/InitData/data
refine_path=$main_path/RefineData/data

# refine value
refine_value=$1
refine_dist=${refine_value%,*}
refine_cnt=${refine_value#*,}

# cleate RefineFiles dir
if [ -d $refine_path/RefineFiles ]; then
	rm -rf $refine_path/RefineFiles
fi
mkdir $refine_path/RefineFiles

for dir in $init_path/TripFiles/*
do
	cnt=0
	echo "$dir"
	user=`echo "${dir#*TripFiles/}"`

	for file in $dir/*
	do
		line=`tail -n1 $file`
   		dist=`echo "$line" | cut -d"," -f8 | cut -d"." -f1` # distance parsing
   		dist=`echo "${dist//\"}"`							# " delete
   		if [ $dist -ge $refine_dist ]; then
			cnt=`expr $cnt + 1`
   		fi
	done

	echo "$cnt"
	if [ $cnt -ge $refine_cnt ]; then
		mkdir $refine_path/RefineFiles/$user

		for file in $dir/*
		do
			trip=`echo "${file#*$user/}"`

			line=`tail -n1 $file`
   			
			dist=`echo "$line" | cut -d"," -f8 | cut -d"." -f1` # distance parsing
   			dist=`echo "${dist//\"}"`							# " delete

   			if [ $dist -ge $refine_dist ]; then
				cp $file $refine_path/RefineFiles/$user/$trip
   			fi
		done
	fi
done
