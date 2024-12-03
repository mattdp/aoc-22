#!/usr/bin/python3

def main(part=1):
    f = open("./2-input.txt","r")
    safe_count = 0
    for line in f:
        report = list(map(lambda x: int(x),line.split()))
        #example: [1, 3, 3, 2, 2, 1, 2]
        diffs = [(report[i+1] - report[i]) for i in range(len(report)-1)] #assumes all reports length 2 or more
        pos = all(1 <= d <= 3 for d in diffs)
        neg = all(-1 >= d >= -3 for d in diffs)
        if pos or neg: safe_count += 1
    print(safe_count)

main()