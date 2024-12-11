#!/usr/bin/python3

import re

brainstorm = """

r/l
u/d
diag1
diag2

if read into those 4 things and then regex all of them for xmas and smax it should work
"""

def main(part=1):
    if(part == 1):
        f = open("./4-input.txt","r")
        xmases = 0
        j = 0
        dimension = 0

        ## "we": #left to right
        ## "ns": #up to down
        ## "nesw": #lower left to upper right diagonal
        ## "nwse": #upper left to lower right diagonal
        x = {}

        for line in f:
            line = line.strip()

            if x == {}:
                dimension = len(line)
                x["we"] = [] #different approach since can simply append
                x["ns"] = [""] * dimension
                x["nesw"] = [""] * (dimension * 2 - 1) # "rows" triggered by all of one side, n-1 of another side
                x["nwse"] = [""] * (dimension * 2 - 1)
            x["we"].append(line)
            for i in range(len(line)):
                x["ns"][i] += line[i]
                x["nesw"][j+i] += line[i]
                #aiming to make upper right most "S" its own row
                #meaning dimension = 140, i = 139, j = 0 should index to 0
                nwse_index = dimension-(i+1)+j
                x["nwse"][nwse_index] += line[i]
                #if(j <= 1):
                #    print(f"i = {i}, j = {j}, dimension = {dimension}, nwse_index = {nwse_index}")
            j += 1
        #print(x["we"][0])
        #print(x["ns"][0])
        #print(x["nesw"])
        #print(x["nwse"])

        pattern = r"XMAS|SAMX"
        for key in x.keys():
            lists = x[key]
            for l in range(len(lists)):
                matches = re.findall(pattern,x[key][l])
                if matches:
                    xmases += len(matches)
        
        print(xmases)

main()