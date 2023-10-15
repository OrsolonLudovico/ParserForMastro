# Explaining the data
Each folder contains the reasult of execution `MASTRO` on `tracerx_lung.txt` without the trees with the expanded graph that has more than 26 edges
`2 min support` means that in mastro the flag `-s` was set to 2 , `3 min support` means that it was set to 3 and so on.
The files that are called `rand` are the result of MASTRO giving the dataset with only one tree for each patient (always < 26).
The files that are called `tracerx_lung_converted_all` or `ALL` are the result of MASTRO giving it the dataset with all the trees (always < 26).

###counter.py
You can use this script with `python3 counter.py input_file`. This script will output the number of edges found in the input and show the mean at the end.
You must have the input file and `counter.py` in the same folder.
