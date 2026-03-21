#!/bin/sh

if [ $# -eq 0 ]
  then
    echo "You must provide the minimum size of the packages, as an argument, in Megabytes."
    exit
fi

if ! [ -d "./tmp/" ]; then
    mkdir "./tmp/"
fi

chmod +x modules/snap.sh
chmod +x modules/dpkg.sh

modules/dpkg.sh
modules/snap.sh
python3 piechart.py ${1}
rm ./tmp/dpkg_names.txt
rm ./tmp/dpkg_sizes.txt
rm ./tmp/snap_names.txt
rm ./tmp/snap_sizes.txt
