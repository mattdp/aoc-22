#!/usr/bin/python3

import re
from collections import deque

# return ?list of stacks? and a list of move tuples (# crates, from, to)
def input_parser():

    move_queue = deque()

    f = open("./5-input.txt","r")
    for line in f:
        if line[0].isspace():
            continue
        elif line[0] == "m": #move line
            matches = re.match("move (\d+) from (\d+) to (\d+)",line)
            a,b,c = map(lambda x: int(x),matches.group(1,2,3))
            tup = (a,b,c)
            move_queue.append(tup)
        else: # crate info line
            #push from top down onto appropriate stack, then map reverse all stacks
            continue

    return move_queue

def main():
    print(input_parser())

main()