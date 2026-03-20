import matplotlib.pyplot as plt
import sys

# IN MEGABYTES
SIZE_TRESHOLD = float(sys.argv[1])

def normalize_snap_sizes(size_str):
    # converts all sizes to MB
    if "G" in size_str:
        size_str = size_str.replace("G", "")
        return float(size_str) * 1000
    elif "M" in size_str:
        size_str = size_str.replace("M", "")
        return float(size_str)
    elif "K" in size_str:
        size_str = size_str.replace("K", "")
        return float(size_str) / 1000

def read_dkpg():
    dkpg_names = list()
    dkpg_sizes = list()

    deleted_indices = list()

    with open("dkpg_sizes.txt", "r") as f:
        i = 0
        for line in f:
            i+=1
            sz = float(line) / 1000
            if sz > SIZE_TRESHOLD:
                dkpg_sizes.append(float(line) / 1000)
            else:
                deleted_indices.append(i)

    with open("dkpg_names.txt", "r") as f:
        j = 0
        for line in f:
            j+=1
            if not (j in deleted_indices):
                dkpg_names.append(line + " (" + str(dkpg_sizes[len(dkpg_names)]) + " MB)" )
    
    print(
            "Removed: " + 
            str(len(deleted_indices)) +
            " dkpg entries as per the sizing treshold."
            )

    return (dkpg_sizes, dkpg_names)

def read_snap():
    snap_names = list()
    snap_sizes = list()
    deleted_indices = list()
    with open("snap_sizes.txt", "r") as f:
        i = 0
        for line in f:
            i+=1
            sz = normalize_snap_sizes(line)
            if sz > SIZE_TRESHOLD:
                snap_sizes.append(sz)
            else:
                deleted_indices.append(i)

    with open("snap_names.txt", "r") as f:
        j = 0
        for line in f:
            j+=1
            if not (j in deleted_indices):
                snap_names.append(line + " (" + str(snap_sizes[len(snap_names)]) + " MB)" )

    # remove "total" and it's size from the data
    snap_names.pop()
    snap_sizes.pop()
    
    print(
            "Removed: " + 
            str(len(deleted_indices)) +
            " snap entries as per the sizing treshold."
            )

    return (snap_sizes, snap_names)

snap_sz, snap_n = read_snap()
apt_sz, apt_n = read_dkpg()

plt.pie(apt_sz + snap_sz, labels = ( apt_n + snap_n ))
plt.show()
