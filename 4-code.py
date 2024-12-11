#!/usr/bin/python3

brainstorm = """
make into an i,j array

possibly just transform it over and over - flip, translate
new array of diagonals

r/l
u/d
diag1
diag2

if read into those 4 things and then regex all of them for xmas it should work

for each X look in all directions
if near puzzle boundaries don't need to consider checks
"""

def main(part=1):
    f = open("./4-input.txt","r")
    xmases = 0
 
    ## "we": #left to right
    ## "ns": #up to down
    ## "swne": #lower left to upper right diagonal
    ## "nwse": #upper left to lower right diagonal
    x = {}

    j = 0
    for line in f:
        line = line.strip()
        if x == {}:
            dimension = len(line)
            x["we"] = [] #different approach since can simply append
            x["ns"] = [""] * dimension
            print(x["ns"][0])
            x["swne"] = [[]] * (dimension * 2 - 1) # "rows" triggered by all of one side, n-1 of another side
            x["nwse"] = [[]] * (dimension * 2 - 1)
        x["we"].append(line)
        for i in range(len(line)):
            x["ns"][i] += line[i]
        j += 1
    print(x["we"][0])
    print("break")
    print(x["ns"][0])

main()