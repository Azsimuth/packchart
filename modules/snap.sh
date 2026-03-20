#!/bin/bash
du -hcs /var/lib/snapd/snaps/* | cut -f1 > ./tmp/snap_sizes.txt
du -hcs /var/lib/snapd/snaps/* | cut -f2 > ./tmp/snap_names.txt
