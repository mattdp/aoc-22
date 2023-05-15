"""
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

f = open("./1-input.txt","r")

running_count = 0
max_calories = 0
line_count = 1
casted = 0

for line in f:
    print(f'line {line_count}: {line}')
    try:
        casted = int(line)
        running_count = running_count + casted
        if running_count > max_calories:
            max_calories = running_count
    except ValueError:
        running_count = 0
    line_count += 1

print(max_calories)