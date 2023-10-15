import argparse                                                                 #use this script to eliminate all the expanded graph that have more than n edges

parser = argparse.ArgumentParser()
parser.add_argument('-g',required = True, help= "Input file to strip")
parser.add_argument('-n',default = 26 ,help= "Maximum number of edges of a tree (the default is 26)")
args = parser.parse_args()

inputf = args.g
max_number = args.n

with open(inputf, 'r') as inp:
    lines = inp.readlines()
result = ""
for line in lines:
    if line.count(" ") < max_number:
        result += line

outputf = inputf
outputf = outputf.replace(".txt","")
outputf += f"_only_less_than_{max_number}.txt"
with open(outputf,'w') as outf:
    outf.write(result)
