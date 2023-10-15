# PARSING DATA FROM RECAP FORMAT TO A FORMAT THAT MASTRO CAN UNDERSTAND
###How to run
Run the conversion script `run_parser.py`(it's raccomanded to use the command `python3 run_parser.py`). Such script accepts various parameters, listed and described bu using the `-h` flag:

```
usage: run_parser.py [-h] -g G [-r R] [-o O] [-m M]

options:
  -h, --help  show this help message and exit
  -g G        Input file to convert
  -r R        The string used to indicate the root of the tree (GL default)
  -o O        Choose if you want to show the output in the terminal (y = yes and n = no, y is default)
  -m M        'a' onverts all the tree found and outputs to input_file_converted_all.txt, 'r' converts only one random tree for patient in input_file_converted_rand.txt, 'b' does both (b is default)  
  -s S        Maximum number of edges for the resulting expanded graph. If isn't specified there is no maximum
```

The `-g` option specify the name of the file to convert, the file is formatted as shown in the RECAP documentation at `https://github.com/elkebir-group/RECAP/tree/master#io-format`. This is the only mandatory flag

The parameter `-r` rapresents the string used to indicate the germline node, if not specified the default value is `GL` wich is the name used in the dataset presented in `RECAP` at `https://github.com/elkebir-group/RECAP/blob/master/data/TRACERx_lung/tracerx_lung.txt` and `https://github.com/elkebir-group/RECAP/blob/master/data/breast_Razavi/breast_Razavi.txt`

The flag `-o` is used to specify whether or not to recive, as output on the terminal, the converted tree as it is being processed(y for yes and n for no), if not specified yes is the default

The `-m` option specifies the mode:
    `a`: You want to take ALL the trees found in the input file and convert them to the "MASTRO format", regardless of the patients whom they belong. The output of this operation is stored in `input_file_converted_all.txt`, it is also shown in the terminal if you selected `y` in the `-o` flag
    `r`: You want to convert only one tree from each patient (the tree is choosen at random). The output of this operation is stored in `input_file_converted_rand.txt`, it is also shown in the terminal if you selected `y` in the `-o` flag
    `b` indicates that you want to do both things
If not specified `b` is the default
The `-s` flag specifies the maximum number of edges of the expanded graph. If a value is specified then all the trees that have more than the value edges in the expanded graph will not be written in the output.If nothing is specified then all the trees will be written in the output 

###Input format
Follow the directives at `https://github.com/elkebir-group/RECAP/tree/master#io-format`
[Note: The symbol that separates the clusters can be only `;` and it can not be specified to be anything else]

###Output
Running the script produces one or two (depending on the choice made in the `-m` flag) text files. Each file has a tree in each line and that complies with the format that MASTRO accepts(for more information about this format see `https://github.com/VandinLab/MASTRO#input-format`)
Those files can be individually used as an input for MASTRO

#Strip.py
(This script is not strictly necessary, the same funtionalities are implemented in `run_parser.py` using the flag `-s`)
Run `Strip.py` to discard all the expanded graph that have more than a specified value from an input file (expressed in MASTRO format)
###How to run
```
usage: strip.py [-h] -g G [-n N]

options:
  -h, --help  show this help message and exit
  -g G        Input file to strip
  -n N        Maximum number of edges of a tree (the default is 26)
```

`-g` indicates the name of the input file (this is mandatory)
`-n` indicates the maximum number of edges that a expanded graph can have (this is optional, if not specified the default value is 26). A edge is considered as any of the following: `A->-B` `A-/-B` `A-?-B`
[Note: examples of input files are provided in the folder (tracerx_lung.txt, breasts_Razavi.txt and treeforparse.txt)]
