#!/usr/bin/python3

import re
from operator import itemgetter

#attempt 1 too small - not firing on [(30, 83), (30, 84)]. sort found them equal
def compute(part_number=2):
    f = open("./4-input.txt","r")
    total_subsets = 0
    tuple_list = []

    for line in f:
        print_string = ""
        tuple_list = range_parse(line)

        #tuple_list = sorted(sorted(tuple_list), key=itemgetter(1), reverse = True) 
        # ^ this gets the right answer for part 1, but not for the reasons I thought, and it doesn't order the list right for part 2.
        #example: (15,76) and (21, 65). first 15 then 21, then no change since 15 76 bigger than 65. if would change, not a subset, since bigger [..][1] is linked to smaller [0][..]

        tuple_list = sorted(tuple_list, key = lambda t: (t[0], -t[1]))

        total_subsets += scoring(part_number,tuple_list)

        print_string += f"{tuple_list}"
        print(print_string)
    
    return(total_subsets)

#tuple_list is sorted by first number ascending, then second decending
def scoring(part_number,tuple_list):
    if part_number == 1:
        if(tuple_list[0][0] <= tuple_list[1][0] and tuple_list[0][1] >= tuple_list[1][1]):
            print("SUBSET FOUND")
            return 1
        return 0
    else:
        #first values match, or the top end of the bigger range is more or equal to the start of the smaller range
        if(tuple_list[0][0] == tuple_list[1][0] or tuple_list[0][1] >= tuple_list[1][0]):
            return 1
        return 0

def range_parse(line):
    matches = re.match("(\d+)-(\d+),(\d+)-(\d+)",line)
    a,b,c,d = map(lambda x: int(x),matches.group(1,2,3,4))
    return [(a,b),(c,d)]

def main():
    print(compute())

main()