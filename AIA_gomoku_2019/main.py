#!/bin/python3

import sys
import random as rd
from Interpretor import interpretor

inter = interpretor()
while (inter.analyseInput()):
    table = inter.getMap()
    for line in table:
        print(line)
    table = inter.getMap()
    try:
        for x in range(19):
            for y in range(19):
                if (table[x][y] == 0):
                    inter.writeOutuput(x, y)
                    raise NotImplementedError
    except:
        pass