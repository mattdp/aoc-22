#!/usr/bin/python3

def height_check(treeline):

    highest_tree = -1
    indexes = list(range(0,len(treeline)))
    for i in indexes:
        tree = treeline[i]
        if tree[1] == 1:
            pass
        elif tree[0] > highest_tree:
            highest_tree = tree[0]
            tree[1] = 1
        else:
            tree[1] = 0
    
    #sweep from opposite direction
    highest_tree = -1
    indexes.reverse()
    for i in indexes:
        tree = treeline[i]
        if tree[1] == 1:
            pass
        elif tree[0] > highest_tree:
            highest_tree = tree[0]
            tree[1] = 1
        else:
            tree[1] = 0    
    
    return treeline

def main():
    f = open("./8-input-tiny.txt","r")
    rows = []
    for line in f:
        row = list()
        line = line.strip()
        for char in line:
            row.append([int(char),False])
        rows.append(row)
    
    columns = list(zip(*rows))

    #assumes square grid
    for i in range(0,len(rows)):
        rows[i] = height_check(rows[i]) #first row looks good but if check line 55 it's all set to 1s
        #somehow when i is 0, there are changes happening in non-0 rows
        columns[i] = height_check(columns[i])
        print(f"i of {i}\nrows: {rows}\ncols: {columns}\n")

    visible_count = 0
    for x in range(0,len(rows)):
        for y in range(0,len(rows)):
            if ((rows[x][y][1] == 1) or (columns[y][x][1] == 1)):
                visible_count += 1
    print(visible_count)

main()