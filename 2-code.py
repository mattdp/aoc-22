#!/usr/bin/python3

translation = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",    
}

points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

a_beats_b = {
    "Paper": "Rock",
    "Rock": "Scissors",
    "Scissors": "Paper",
}

points_draw = 3
points_win = 6

def part_one():
    cumulative_points = 0

    f = open("./2-input.txt","r")
    for line in f:
        try:
            cumulative_points += score_line(line[0],line[2])
        except Error:
            print(f"Error: exited with {cumulative_points}")
    print(cumulative_points)

def score_line(them, me):
    total_points = points[translation[me]]

    if(translation[me] == translation[them]):
        total_points += points_draw
    elif(a_beats_b[translation[me]] == translation[them]):
        total_points += points_win
    
    return total_points

part_one()