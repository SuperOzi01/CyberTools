#!/bin/bash

file=$1
echo "--- [x] Working On It! ---"
result=0
Data=$(cat $file)
val=""
while [ $result -eq 0 ];
do
	echo "$Data" | base64 -d &> /dev/null
	if [ $? -eq 0 ];
	then
		Data=$(echo $Data | base64 -d 2> /dev/null)
	else
		result=1
	fi
done
echo "--- [x] Result! ---"
echo "$Data"

