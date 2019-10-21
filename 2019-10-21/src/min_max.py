#!/usr/bin/python3

from static_evaluation import *
import math

def ajd_min_max(position, depth, alpha, beta, player, coordinate):
    if (depth == 0):
        return (get_score(position, coordinate)) # scores the result that can be done by taking a pos
    
    if (player):
        print("here")
        maxEval = -math.inf
        for x in range(19):
            for y in range(19):
                new_position = update_scoreboard(position, (x, y), 1)
                eval = ajd_min_max(position, depth - 1,
                               alpha, beta, (not player), (x, y))
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if (beta <= alpha):
                    break
        return (maxEval)
    
    else:
        print("there")
        minEval = math.inf
        for x in range(19):
            for y in range(19):
                new_position = update_scoreboard(position, (x, y), 0)
                eval = ajd_min_max(position, depth - 1,
                               alpha, beta, player, (x, y))
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if (beta <= alpha):
                    break
        return (minEval)

# calcs the score of an action

def min_max(position, player, coordinate, depth):
    table = init_scoreboard(position)
    score = ajd_min_max(table, depth, -math.inf, math.inf, player, coordinate)
    return (abs(score))

def find_coordinate(table, player, depth):
    score_2_coor = {}
    for x in range(19):
        for y in range(19):
            score_2_coor[(x, y)] = min_max(table, player, (x, y), depth)
    for key, value in score_2_coor.items():
        print(key, value)
    return (max(score_2_coor, key=score_2_coor.get))

go_table = [[0] * 19 for i in range(19)]
go_table[4][5] = 'A'
go_table[5][6] = 'A'
go_table[6][7] = 'A'

toto = find_coordinate(go_table, 0, 0)
go_table[toto[1]][toto[0]] = 'B'

for line in go_table:
    print(line)