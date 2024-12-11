#!/usr/bin/python3

import re

part2brainstorm = """

regex approach: could use location of group and locations of do/dont 
to figure out what's relevant as iterate through list of matches. 
function for position and which of do/don't apply there

could also parse the text, chopping off front until reach a do, don't, or mult
"""

def main(part=1):
    f = open("./3-input.txt","r")
    total_sum = 0
    for line in f:
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern,line) #many mul's
        #print(matches)
        total_sum += sum((map(lambda x: int(x[0])*int(x[1]),matches)))
        #for m in matches:
        #    factors = re.match(r"\D*(\d+),(\d+)",m) #tested
        #    sum += int(factors.group(1)) * int(factors.group(2))
        #    #print(f"{factors.group(1)} * {factors.group(2)}")
    print(total_sum)

main()