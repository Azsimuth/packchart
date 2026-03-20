#!/bin/sh

dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n | cut -f1 > dkpg_sizes.txt
dpkg-query -Wf '${db:Status-Status} ${Installed-Size}\t${Package}\n' | sed -ne 's/^installed //p'|sort -n | cut -f2 > dkpg_names.txt
