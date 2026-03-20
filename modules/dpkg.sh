#!/bin/sh

dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n | cut -f1 > ./tmp/dpkg_sizes.txt
dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n | cut -f2 > ./tmp/dpkg_names.txt
