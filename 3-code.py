#!/usr/bin/python3

def part_one():
    f = open("./3-input.txt","r")
    line_number = 1
    total_priority = 0
    for line in f:
        line = line.strip()
        pivot = int(len(line)/2) #trusts that sacks have even #

        pocket1 = line[:pivot]
        pocket2 = line[-pivot:]

        #have to pop since no indexing sets
        intersection = set(pocket1).intersection(pocket2).pop()
        priority = get_priority(intersection)
        
        print(f"({line_number}) Priority: {priority}, Intersection: {intersection}, Contents: {line}, Pocket1: {pocket1}, Pocket2: {pocket2}")

        total_priority += priority
        line_number += 1
    return total_priority

#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
def get_priority(char):
    ascii = ord(char)
    if ascii > 96: # lowercase letter; 'a' is 97
        return ascii - 96
    else: #uppercase, 'A' is 65
        return ascii - 38

def main():
    print(part_one())

main()

