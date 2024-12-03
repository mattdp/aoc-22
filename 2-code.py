#!/usr/bin/python3


p2brainstorm = """
find issue in the diff and remove both affected elements

lower bound is p1 answer upper bound is inputs

brute force by dropping each element of unsafe lists

if only one element with diff abs(4) or higher or abs(0), remove and check
if only one element with different sign than rest, remove and check

only need to see if safe, not actually make right answer - if somehow know removal possible then no need to follow through
"""

 #assumes all reports length 2 or more
def get_diffs(report):
    return [(report[i+1] - report[i]) for i in range(len(report)-1)]

def checker(diffs):
    pos = all(1 <= d <= 3 for d in diffs)
    neg = all(-1 >= d >= -3 for d in diffs)
    return (pos or neg)    

def main(part=2):
    f = open("./2-input.txt","r")
    safe_count = 0

    if(part==1):
        for line in f:
            report = list(map(lambda x: int(x),line.split()))
            #diffs example: [1, 3, 3, 2, 2, 1, 2]
            diffs = [(report[i+1] - report[i]) for i in range(len(report)-1)]
            pos = all(1 <= d <= 3 for d in diffs)
            neg = all(-1 >= d >= -3 for d in diffs)
            if pos or neg: safe_count += 1
        print(safe_count)
    else:
        for line in f:
            report = list(map(lambda x: int(x),line.split()))
            #diffs example: [1, 3, 3, 2, 2, 1, 2]
            diffs = get_diffs(report) #assumes all reports length 2 or more
            if checker(diffs): 
                safe_count += 1
            else:
                d = 0
                possible_trouble = [] #report indices to test removal
                while d < len(diffs) and possible_trouble == []:
                    element = diffs[d]
                    if element == 0 or abs(element) >= 4:
                        possible_trouble = [d, d+1]
                    elif d >= 1 and (diffs[0] * diffs[d] < 0): #one's positive, one's negative
                        if(d==1): 
                            possible_trouble = [0,1,2] #not sure which sign is in incorrect direction
                        else: 
                            possible_trouble = [d,d+1] #the new info is bad since previous signs matched at least once
                    d += 1
                if possible_trouble:
                    print(f"possible trouble at indexes {possible_trouble} in diffs {diffs}")
                    for pt in range(len(possible_trouble)):
                        remove_index = possible_trouble[pt]
                        test_report = report[:remove_index] + report[remove_index + 1:]
                        if checker(get_diffs(test_report)):
                            print(f"modified report {test_report} safe, after removing index {remove_index} from {report}") 
                            safe_count += 1
                            break
                else:
                    print(f"WARNING: no issue found for {diffs}, and all lines at this point should have at least one issue.")
        print(safe_count)

main()