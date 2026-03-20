#!/bin/bash
du -hcs /var/lib/snapd/snaps/* | cut -f1 > snap_sizes.txt
du -hcs /var/lib/snapd/snaps/* | cut -f2 > snap_names.txt
