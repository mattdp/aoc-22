#!/usr/bin/python3

# next: this is getting a #, optimize it for what the prompt's asking

import itertools
import re

class Node:

    id_iter = itertools.count()

    def __init__(self,parent_id,name,files_size = 0):
        self.id = next(Node.id_iter)
        self.parent_id = parent_id        
        self.name = name
        self.files_size = files_size
        self.children_ids = []

class NodeHolder:
    def __init__(self):
        self.nodes = {}
        root_node = Node(-1,"root")
        self.nodes[0] = root_node
        self.root_id = root_node.id
    
    def add_node(self,parent_id,name,files_size = 0):
        added = Node(parent_id,name,files_size)
        self.nodes[added.id] = added
        self.nodes[parent_id].children_ids.append(added.id)
        return added.id
    
    def get_node(self,node_id):
        return self.nodes[node_id]

    def set_files_size(self,node_id,files_size):
        self.nodes[node_id].files_size = files_size
        return 0

    def get_children(self,node_id):
        ids = self.nodes[node_id].children_ids
        return list(map(lambda x: self.get_node(x), ids))
    
    def total_size(self,node_id):
        node = self.get_node(node_id)
        total = node.files_size
        for child_id in node.children_ids:
            total += self.total_size(child_id)
        return total
        
def part_one(nh,inputs):
    pwd_id = nh.root_id
    file_sizes_adder = 0

    for line in inputs:
        print(line)

        if line[0] == "$" and file_sizes_adder > 0:
            nh.set_files_size(pwd_id,file_sizes_adder)
            file_sizes_adder = 0

        if line[0:6] == "$ cd /":
            pwd_id = nh.root_id
        elif line[0:7] == "$ cd ..":
            pwd_id = nh.get_node(pwd_id).parent_id
            # if parent_id < 0:
            #     raise Exception("Attempt to access parent of root node")
        elif line[0:4] == "$ cd":
            target_name = line[5:].strip()
            children = nh.get_children(pwd_id)
            target_node = list(filter(lambda node: node.name == target_name,children))
            pwd_id = target_node[0].id
        elif line[0:3] == "dir":
            nh.add_node(pwd_id,line[4:].strip())
        elif line[0:4] == "$ ls":
            pass
        else:
            match = re.match("^(\d+)*",line)
            file_sizes_adder += int(match.group(1))

    return(nh.total_size(nh.root_id))

def main():
    f = open("./7-input.txt","r")

    node_holder = NodeHolder()   
    
    p1 = part_one(node_holder,f.readlines())   
    
    print(p1)

main()