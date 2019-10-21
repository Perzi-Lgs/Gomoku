#!/usr/bin/python3

from static_evaluation import *
import math
from Table import *

def find_coordinate(tab, player, depth):
    size = len(tab)
    if (player):
            type = -1
    else:
        type = 1
    score_2_coor = {}
    table = Table()
    table.setTable(init_scoreboard(tab))
    for x in range(19):
        for y in range(19):
            score_2_coor[(x, y)] = table.getScore((x, y))
            table.undo()
    #print(score_2_coor)
    return (max(score_2_coor, key=score_2_coor.get)

#go_table = [[0] * 19 for i in range(19)]
#go_table[4][5] = 'A'
#go_table[5][6] = 'A'
#go_table[6][7] = 'A'
#
#toto = find_coordinate(go_table, 0, 0) 
#go_table[toto[1]][toto[0]] = 'B'
#
#for line in go_table:
#    print(line)