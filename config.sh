#!/bin/bash

# Absloute Path ------------------------------------------------
if [ -z $DSE_PATH ]; then
	SOURCE="${BASH_SOURCE[0]}"
	DIR="$( cd "$( dirname "$SOURCE" )" && pwd -P )"
	
	# Export environment
	echo "export DSE_PATH=$DIR" >> /etc/bash.bashrc
	
	source /etc/bash.bashrc
fi

# Library install ----------------------------------------------
# Python3 library
apt update
apt install python3 python3-dev -y

# pip3 install library
pip3 install google-cloud-storage # google-cloud

# library
pip3 install pandas 
pip3 install numpy
pip3 install matplotlib
pip3 install glob3
pip3 install scikit-learn
pip3 install scipy
pip3 install seaborn
pip3 install yellowbrick
