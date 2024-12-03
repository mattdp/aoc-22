#!/usr/bin/python3

# can do this all in one traversal w/o sort, but didn't figure out distance was absolute until split it out for debugging

import re
from collections import deque

#part two
def main(part=2):
    f = open("./1-input.txt","r")
    total_distance = 0
    left = []
    right = []
    for line in f:
        matches = re.match(r"(\d+)\s+(\d+)",line)
        a,b = map(lambda x: int(x),matches.group(1,2))
        left.append(a)
        right.append(b)
    
    left.sort()
    right.sort()

    if(part==1):
        for i in range (0,len(left)):
            distance = abs(right[i] - left[i])
            total_distance += distance
            print(f"{left[i]} and {right[i]} input, {distance} distance, new total {total_distance}") 
        print(total_distance)
    else:
        similarity = 0

        left = deque(left)
        right = deque(right)

        while left:
            pop_counter = 0
            similarity_counter = 0
            checking = left.popleft()
            for r in range(0,len(right)):
                if right[r] < checking:
                    pop_counter += 1
                if right[r] == checking:
                    similarity_counter += 1
                if right[r] > checking:
                    break
            for _ in range(pop_counter):
                right.popleft()
            similarity += checking * similarity_counter

        print (similarity)

main()