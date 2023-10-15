import argparse
import subprocess
import os
import parserDataMASTRO
import random

def check_num(parts):                                               #checks if the list has, as the first item, a valid number. If not returns -1
    num = parts[0].strip()
    try:
        num = int(num)
    except ValueError:
        num = -1
    return num;
    
    
    
parser = argparse.ArgumentParser()
parser.add_argument('-g',required = True, help= "Input file to convert")
parser.add_argument('-r',default = "GL",help= "The string used to indicate the root of the tree (GL default)")
parser.add_argument('-o',default = "y",help= "Choose if you want to show the output in the terminal(y = yes and n = no, y is default)")
parser.add_argument('-m',default = "b",help= "a converts all the tree found and outputs to input_file_converted_all.txt    r converts only one random tree for patient in input_file_converted_rand.txt    b does both (b is default)")
parser.add_argument('-s',default = 100000 ,help= "Maximum number of edges for the resulting expanded graph. If isn't specified there is no maximum")
args = parser.parse_args()

root_name = args.r
file_name = args.g
mode = args.m
max_edges_number = int(args.s)

def pass_the_trees(is_randomized):                                        #passes the trees to the parser, if 'is_randomized' is False it passes all the trees, otherwise it passes all the trees
    if is_randomized == True and args.o == "y":
        print("Randomized choice of trees below:")
    if is_randomized == False and args.o == "y":
        print("All trees below:")
    tot_output = ""
    with open(file_name, 'r') as inp:    
        first_line = inp.readline()
        parts =first_line.split('#')
        
        num_patients = check_num(parts)                                 #checking how many patients
        if num_patients == -1:
            print("Format error: the first line must contain the number of patients as the first argument")
            exit(1)
        
        for i in range(num_patients):                                   #cycle the patients
            first_line = inp.readline()
            parts = first_line.split('#')
            num_trees = check_num(parts)
            if num_trees == -1:
                print(f"Format error: number of trees for the patient number {i + 1} was not found")
                exit(1)
            valid_trees = []
            for j in range(num_trees):                                   #cycle the trees
                first_line = inp.readline()
                parts = first_line.split('#')
                num_edges = check_num(parts)
                if num_edges == -1:
                    print(f"Format error: number of edges for the tree number {j + 1} of the patient number {i + 1} was not found")
                    exit(1)
                buffer = ""
                for k in range(num_edges):                                #cycle the edges
                    edge = inp.readline()
                    buffer += edge
                output = parserDataMASTRO.convert(buffer,root_name)         #obtains the trees
                num_of_pieces = int(output.count(" "))
                if num_of_pieces <= max_edges_number:                       #check if a tree is valid
                    valid_trees.append(output)
            
            if is_randomized == False:                                      #outputs the trees
                for element in valid_trees:
                    tot_output += element + "\n"
            if is_randomized == True and len(valid_trees) > 0:
                tot_output += random.choice(valid_trees) + "\n"
                
    if args.o == "y":
        print(tot_output)
        print("")
    return tot_output

content_all = ""
content_rnd = ""
if mode == "a":                                                                 #call the function in different wasy depending on the output
    content_all = pass_the_trees(False)
elif mode == "r":
    content_rnd = pass_the_trees(True)
else:
    if mode != "b":
        print("The inserted mode isn't valid, applying default mode 'b'")
    content_all = pass_the_trees(False)
    content_rnd = pass_the_trees(True)

output_all_file_name = file_name                                                 #write the results into the respective files
output_all_file_name = output_all_file_name.replace(".txt","")
output_all_file_name += "_converted_all.txt"
with open(output_all_file_name,'w') as out_total_all:
    out_total_all.write(content_all)

output_rnd_file_name = file_name
output_rnd_file_name = output_rnd_file_name.replace(".txt","")
output_rnd_file_name += "_converted_rand.txt"
with open(output_rnd_file_name,'w') as out_total_rnd:
    out_total_rnd.write(content_rnd)
    