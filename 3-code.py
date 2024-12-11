#!/usr/bin/python3

import re

part2brainstorm = """

regex approach: could use location of group and locations of do/dont 
to figure out what's relevant as iterate through list of matches. 
function for position and which of do/don't apply there

could also parse the text, chopping off front until reach a do, don't, or mult
"""

def main(part=2):
    f = open("./3-input.txt","r")
    total_sum = 0
    if(part==1):
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
    else:
        mega = r""
        for line in f:
            mega += line
            #print(mega)
        pattern = r"do\(\)"
        result = re.split(pattern,mega)
        dont_pattern = r"^(.*)don\'t\(\)"
        mult_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        for r in result:
            shorter = ""
            substring = re.match(dont_pattern,r)
            if substring:
                shorter = substring[0]
            else:
                shorter = r
            #print(shorter)
            matches = re.findall(mult_pattern,shorter)
            total_sum += sum((map(lambda x: int(x[0])*int(x[1]),matches)))
        print(total_sum)

main()