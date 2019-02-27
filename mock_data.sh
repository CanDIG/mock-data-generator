#!/usr/bin/env bash

# This script will generate n records of pipeline & clinical metadata and output a CanDIGv1 ingestible json file
#
# Usage:
#  $ ./mock_data <#records> 
# * #records: number of records to create 
#
if [ ${#@} == 1 ]; then
	if [ ! -d md_venv/ ]; then
		echo "No environment detected, initialising..."
		virtualenv md_venv
		source md_venv/bin/activate
		pip install --upgrade pip
		pip install -U setuptools
		pip install -r requirements.txt
	fi
	source md_venv/bin/activate
	if [ ! -f project_tiers.xlsx ]; then
		wget https://github.com/CanDIG/redcap-cloud/raw/master/input/project_tiers.xlsx
	fi
	if [ ! -f load_tiers.py ]; then
		wget https://raw.githubusercontent.com/CanDIG/redcap-cloud/master/load_tiers.py
	fi
	python mock_clinphen.py $1 && \
	python load_tiers.py clinical mock_clinphen_data.json project_tiers.xlsx mock_clinphen_1.json && \
	python mock_pipeline.py && \
	python load_tiers.py pipeline mock_pipeline_data.json project_tiers.xlsx mock_pipeline_1.json && \
	# clear intermediate output
	rm mock_clinphen_data.json
	rm mock_pipeline_data.json
	deactivate
else
	echo "Usage: $0 <#records>"
fi
