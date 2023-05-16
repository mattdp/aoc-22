#!/usr/bin/python3

import re
from collections import deque

# transform stacks and move_queue to have all data
def input_parser(stacks,move_queue):

    f = open("./5-input.txt","r")
    for line in f:
        if line[0].isspace(): #skip crate stack key, separator
            continue
        elif line[0] == "m": #move line
            matches = re.match("move (\d+) from (\d+) to (\d+)",line)
            a,b,c = map(lambda x: int(x),matches.group(1,2,3))
            tup = (a,b,c)
            move_queue.append(tup)
        else: # crate info line
            stack_index = 1
            char_pos = 1
            while char_pos <= len(line):
                if not line[char_pos].isspace():
                    stacks[stack_index].append(line[char_pos])
                stack_index += 1
                char_pos += 4 # "] [" is separator, then 1 more to get to char
            
    return stacks, move_queue

def main(part_number = 2):

    #for ease of debugging, keep input stack #s same as list slots
    stacks = [None] 
    for i in range (9):
        stacks.append(deque())
    move_queue = deque()

    input_parser(stacks,move_queue)

    #(quantity, from, to)
    for m in move_queue:
        if (part_number == 1):
            for i in range(m[0]):
                crate = stacks[m[1]].popleft()
                stacks[m[2]].appendleft(crate)
        elif (part_number == 2):
            cratepile = list()
            for i in range(m[0]):
                crate = stacks[m[1]].popleft()
                cratepile.append(crate)
            #cratepile has top crate first here...
            for c in range(len(cratepile)):
                crate = cratepile.pop()
                stacks[m[2]].appendleft(crate)
            #...and adds to new stack bottom up

    print_string = ""
    for s in range(1,10):
        print(f"{s}: {stacks[s]}")
        print_string += stacks[s].popleft()

    print(print_string)

main()