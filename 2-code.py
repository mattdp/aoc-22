#!/usr/bin/python3

#next: verbose output, so can figure out what's scoring wrong
#could also make a mini input file to test

points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Lose": 0,
    "Draw": 3,
    "Win": 6,
}

a_beats_b = {
    "Paper": "Rock",
    "Rock": "Scissors",
    "Scissors": "Paper",
}

a_loses_b = {
    "Rock": "Paper",
    "Scissors": "Rock",
    "Paper": "Scissors",
}

#misread - this solves if first input is MY choice, but it's OPPONENT choice
# def part_two_misread():
#     f = open("./2-input.txt","r")
#     text = f.read()

#     scores = [ #16936, which is too high according to site
#         points["Rock"]*text.count("A"), #267 * 1 = 267
#         points["Paper"]*text.count("B"), #500 * 2 = 1000
#         points["Scissors"]*text.count("C"), #1733 * 3 = 5199
#         points["Draw"]*text.count("Y"), #834 * 3 = 2502
#         points["Win"]*text.count("Z"), #1328 * 6 = 7968
#     ]
#     print(scores)
#     return(sum(scores))

def score_line_again(them, me, verbose=False):
    translation = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",    
    }

    their_choice = translation[them]

    #Win/lose/draw points
    total_points = points[translation[me]]
    if(verbose):
        print(f"***\nWLD: {total_points} for {translation[me]}")

    if(translation[me] == "Draw"):
        pts = points[their_choice]
        if(verbose):
            print(f"Thing: {pts} for {translation[them]}")
        total_points += pts
    elif(translation[me] == "Lose"):
        selection = a_beats_b[their_choice]
        pts = points[selection] 
        if(verbose):
            print(f"Thing: {selection} gives {pts} for LOSE to {translation[them]}")
        total_points += pts
    else:
        selection = a_loses_b[their_choice]
        pts = points[selection]
        if(verbose):
            print(f"Thing: {selection} gives {pts} for WIN to {translation[them]}")
        total_points += pts
    
    if(verbose):
        print(f"{translation[them]} {translation[me]}: {total_points} points")

    return total_points

def score_line(them, me):
    translation = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",    
    }

    total_points = points[translation[me]]

    if(translation[me] == translation[them]):
        total_points += points["Draw"]
    elif(a_beats_b[translation[me]] == translation[them]):
        total_points += points["Win"]
    
    return total_points

#part_number: part 1 or part 2 of the question
def frame(part_number = 1):
    cumulative_points = 0

    f = open("./2-input.txt","r")
    for line in f:
        try:
            if part_number == 1:
                cumulative_points += score_line(line[0],line[2])
            else:
                cumulative_points += score_line_again(line[0],line[2],False)
        except:
            print(f"Error: exited with {cumulative_points}")
    return cumulative_points

def main():
    print(frame(2))

main()