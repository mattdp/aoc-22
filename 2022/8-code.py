#!/usr/bin/python3

#maybe mixing edit in place and return of a copy, pick one or the other?
def height_check(treelines,i):

    treeline = treelines[i]

    highest_tree = -1
    indexes = list(range(0,len(treeline)))
    for i in indexes:
        tree = treeline[i]
        if tree[0] > highest_tree:
            highest_tree = tree[0]
            tree[1] = 1
        elif tree[1] == 1:
            pass
        else:
            tree[1] = 0   
    
    #sweep from opposite direction
    highest_tree = -1
    indexes.reverse()
    for i in indexes:
        tree = treeline[i]
        if tree[0] > highest_tree:
            highest_tree = tree[0]
            tree[1] = 1
        elif tree[1] == 1:
            pass
        else:
            tree[1] = 0    
    
    return treeline

def main():
    f = open("./8-input.txt","r") #returning 20, answer is 21 - troubleshoot details from here
    rows = []
    for line in f:
        row = list()
        line = line.strip()
        for char in line:
            row.append([int(char),False])
        rows.append(row)
    
    #sets correct values, but possibly entangles list with the rows?
    #columns = list(zip(*rows)) 

    #adding this didn't fix spillover issue
    columns = []
    for i in range(0,len(rows)):
        column = list(map(lambda r: r[i].copy(),rows))
        columns.append(column)

    #assumes square grid
    for i in range(0,len(rows)):
        height_check(rows,i) #first row looks good but if check line 55 it's all set to 1s
        height_check(columns,i) #after rows run, before columns, there are changes in columns
        print(f"i of {i}\nrows: {rows}\ncols: {columns}\n")

    visible_count = 0
    print("Entering visibility count")
    for x in range(0,len(rows)):
        for y in range(0,len(rows)):
            if ((rows[x][y][1] == 1) or (columns[y][x][1] == 1)):
                print(f"({x},{y}: visible)")
                visible_count += 1
    print(visible_count)

main()