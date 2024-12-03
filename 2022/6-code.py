#!/usr/bin/python3

def part_one():
    unique_length = 14
    f = open("./6-input.txt","r")
    scan_index = unique_length-1 #first place it could work
    for line in f:
        while scan_index < len(line):
            four_set = set(line[(scan_index-(unique_length-1)):(scan_index+1)])
            if len(four_set) == unique_length:
                return(scan_index + 1) #nth char, not nth index
            scan_index += 1
        return("Error - didn't find match")

def main():
    print(part_one())

main()