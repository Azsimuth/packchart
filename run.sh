#!/bin/sh

if [ $# -eq 0 ]
  then
    echo "You must provide the minimum size of the packages, as an argument, in Megabytes."
    exit
fi

./dkpg.sh
./snap.sh
python3 piechart.py ${1}
rm dkpg_names.txt
rm dkpg_sizes.txt
rm snap_names.txt
rm snap_sizes.txt
