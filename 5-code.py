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
            stack_index = 0
            char_pos = 1
            while char_pos <= len(line):
                if not line[char_pos].isspace():
                    stacks[stack_index].append(line[char_pos])
                stack_index += 1
                char_pos += 4 # "] [" is separator, then 1 more to get to char
            
    return stacks, move_queue

def main():

    stacks = list()
    for i in range (9):
        stacks.append(deque())
    move_queue = deque()

    print(input_parser(stacks,move_queue))

main()