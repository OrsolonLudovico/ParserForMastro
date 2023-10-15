import networkx as nx
import matplotlib.pyplot as plt

def get_all_descendants(graph):                     #outputs a dictionary: the key is a node and the value is a list of all the descendants of that node
    all_descendants = {}
    for node in graph.nodes():
        descendants = nx.descendants(graph, node)
        all_descendants[node] = descendants

    return all_descendants
    
def descendants_to_string(disc_list):                #takes in input the output of get_all_descendants, outputs a string (apply the ->-)
    out = ""
    for node,descendants in disc_list.items():
        for descendant in descendants:
            out += f"{node}->-{descendant} "
    return out
    
def all_distant(graph,node):                         #returns all the nodes that are not discendants nor ancestors of a given node in the given tree
    descendants = nx.descendants(graph,node)
    ancestors = nx.ancestors(graph,node)
    others = []
    for n in graph.nodes():
        if n != node and n not in descendants and n not in ancestors:
            others.append(n)
    return others
    
def convert(input_str,r_name):                      #the main function of this file, converts a tree in the MASTRO format
    root_name = r_name
    G = nx.DiGraph()
    output = ""
    unkn_list = []
    
    file = input_str.splitlines()
    
    for line in file:
        parts = line.split()
        if len(parts) != 2:
            print("Format error, each line representing an edge must have two and only two nodes in it")
            exit(1)
        part1 = parts[0].split(";")
        part2 = parts[1].split(";")
        
        if len(part1) > 1:                                              #inserting the ones with "-?-"
            for i in range(len(part1)):
                for j in range(i + 1,len(part1)):
                    ordered = sorted([part1[i],part1[j]])
                    unkn_list.append(f"{ordered[0]}-?-{ordered[1]} ")
        if len(part2) > 1:
            for i in range(len(part2)):
                for j in range(i + 1,len(part2)):
                    ordered = sorted([part2[i],part2[j]])
                    unkn_list.append(f"{ordered[0]}-?-{ordered[1]} ")
        
        for bit in part1:
            if not G.has_node(str(bit)):
                G.add_node(str(bit))
        for bit in part2:
            if not G.has_node(str(bit)):
                G.add_node(str(bit))
        
        if G.has_node(root_name):                                         #we don't need the root note for MASTRO
            G.remove_node(root_name)
            
        for bit1 in part1:
            for bit2 in part2:
                if not G.has_edge(str(bit1),str(bit2)):
                    G.add_edge(str(bit1),str(bit2))
                    
    uniq_list = list(set(unkn_list))

    all_descendants = get_all_descendants(G)
    for node in G.nodes():
        temp = all_distant(G,node)
        for nod in temp:
            ordered = sorted([node,nod])
            buff = f"{ordered[0]}-?-{ordered[1]} "                      #the last space is important
            insert_bit = f"{ordered[0]}-/-{ordered[1]} "
            if buff not in uniq_list and insert_bit not in uniq_list:   #check if it's a "-?-" and not a "-/-"
                uniq_list.append(insert_bit)
                
                
    output += "".join(uniq_list)
    output += descendants_to_string(all_descendants)
    #print(output)
    
    #show the graph
    #pos = nx.spring_layout(G, seed=42)
    #labels = {node: node for node in G.nodes()}
    #nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, node_color="lightblue")
    #plt.show()
    return output