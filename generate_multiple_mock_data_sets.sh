#!/usr/bin/env bash

# This script will generate mock datasets for CanDIG V1 ingestion
#
# Usage:
#  $ ./generate_multiple_mock_data_sets <#sets> <#records> 
# * #sets: number of sets of mockdata to create, each set contains a clin file and a pipeline file 
#   #records: number of records per set

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Colour
CYAN_BG='\e[0;46m'
NO_BG='\e[0m'


if [ $# -eq 2 ]; then
	max=$1
	records=$2

	if ! [[ "$max" =~ ^[1-9]+$ ]] || ! [[ "$records" =~ ^[1-9]+$ ]];then
		echo "Please specify a positive integer for both # of datasets and # of records"
		exit 1
	fi

	if [ ! -d output ]; then
		echo "Initializing output directory..."
		mkdir output
	# else
	# 	echo "Output directory already exists"
	fi

	for (( i=1; i <= $max; ++i))
	do
		sh ./mock_data.sh $records

		# if [ -f output/mock_clinphen_${i}.json ]; then
		# 	echo -e "${RED}WARNING: output/mock_clinphen_${i}.json has been overwritten.${NC}"
		# fi

		# if [ -f output/mock_pipeline_${i}.json ]; then
		# 	echo -e "${RED}WARNING: output/mock_pipeline_${i}.json has been overwritten.${NC}"
		# fi

		mv "mock_clinphen_1.json" "output/mock_clinphen_${i}.json"
		mv "mock_pipeline_1.json" "output/mock_pipeline_${i}.json"

		echo -e "${GREEN}SUCCESS: mock clinphen/pipeline datasets #${i} have been printed to the output folder ${NC}\n"
	done
else
	echo "Usage: <# of datasets to generate> <#records per dataset>"
fi 