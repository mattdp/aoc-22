part_two_prompt = """
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

def part_two():
    f = open("./1-input.txt","r")

    leaderboard = [0,0,0]
    running_count = 0
    line_count = 1
    casted = 0

    for line in f:
        #print(f'line {line_count}: {line}')
        try:
            casted = int(line)
            running_count = running_count + casted
        except ValueError:
            leaderboard = assess(leaderboard,running_count)
            running_count = 0
        line_count += 1
    print(leaderboard)
    print(sum(leaderboard))  

def assess (leaderboard,running_count):
    if (running_count > leaderboard[len(leaderboard)-1]):
        carry = 0
        for index in range(len(leaderboard)):
            if carry > 0: 
                new_carry = leaderboard[index]
                leaderboard[index] = carry
                carry = new_carry
            elif running_count > leaderboard[index]:
                carry = leaderboard[index]
                leaderboard[index] = running_count
    return leaderboard

part_one_prompt = """
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

def part_one():
    f = open("./1-input.txt","r")

    running_count = 0
    max_calories = 0
    line_count = 1
    casted = 0

    for line in f:
        #print(f'line {line_count}: {line}')
        try:
            casted = int(line)
            running_count = running_count + casted
            if running_count > max_calories:
                max_calories = running_count
        except ValueError:
            running_count = 0
        line_count += 1

    print(max_calories)

part_one()
part_two()