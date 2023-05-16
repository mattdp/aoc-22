#!/usr/bin/python3

import re
from operator import itemgetter, attrgetter

#attempt 1 too small - not firing on [(30, 83), (30, 84)]. sort found them equal
def part_one():
    f = open("./4-input.txt","r")
    total_subsets = 0
    tuple_list = []

    for line in f:
        print_string = ""
        tuple_list = range_parse(line)
        tuple_list = sorted(sorted(tuple_list), key=itemgetter(1), reverse = True) #first sort by first number, then in cases where it's the same larger last number

        if(tuple_list[0][0] <= tuple_list[1][0] and tuple_list[0][1] >= tuple_list[1][1]):
            total_subsets += 1
            print_string += "SUBSET FOUND. "

        print_string += f"{tuple_list}"
        print(print_string)
    
    return(total_subsets)

def range_parse(line):
    matches = re.match("(\d+)-(\d+),(\d+)-(\d+)",line)
    a,b,c,d = map(lambda x: int(x),matches.group(1,2,3,4))
    return [(a,b),(c,d)]

def main():
    print(part_one())

main()