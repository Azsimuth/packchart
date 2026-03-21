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

def read_dpkg():
    dpkg_names = list()
    dpkg_sizes = list()

    deleted_indices = list()

    with open("./tmp/dpkg_sizes.txt", "r") as f:
        i = 0
        for line in f:
            i+=1
            sz = float(line) / 1000
            if sz > SIZE_TRESHOLD:
                dpkg_sizes.append(float(line) / 1000)
            else:
                deleted_indices.append(i)

    with open("./tmp/dpkg_names.txt", "r") as f:
        j = 0
        for line in f:
            j+=1
            if not (j in deleted_indices):
                dpkg_names.append(line + " (" + str(dpkg_sizes[len(dpkg_names)]) + " MB)" )
    
    print(
            "Removed: " + 
            str(len(deleted_indices)) +
            " dpkg entries as per the sizing treshold."
            )

    return (dpkg_sizes, dpkg_names)

def read_snap():
    snap_names = list()
    snap_sizes = list()
    deleted_indices = list()
    with open("./tmp/snap_sizes.txt", "r") as f:
        i = 0
        for line in f:
            i+=1
            sz = normalize_snap_sizes(line)
            if sz > SIZE_TRESHOLD:
                snap_sizes.append(sz)
            else:
                deleted_indices.append(i)

    with open("./tmp/snap_names.txt", "r") as f:
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
apt_sz, apt_n = read_dpkg()

ttl_size = apt_sz + snap_sz

s = 0
for n in ttl_size:
    s += n
print("Total size of included packages: " + str(s) + " MB /~ " + str(round(s/1000, 2)) + " G")
plt.pie(ttl_size, labels = ( apt_n + snap_n ))
print("Pie chart opened in new window.")
plt.show()

