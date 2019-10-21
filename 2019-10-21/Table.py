import sys
import copy
from static_evaluation import *

class Table():
    def __init__(self):
        self.table = []
        self.log = {}
        self.undo_time =[]
    
    def getTable(self):
        pass

    def setTable(self, table):
        self.table = copy.deepcopy(table)
    
    def undo(self):
        try:
            time = self.undo_time[-1]
            del(self.undo_time[-1])
            for i in range(time):
                self.adj_undo()
            return (True)
        except IndexError:
            return (False)

    def adj_undo(self):
        try:
            coordinate = list(self.log.keys())[-1]
        except IndexError:
            return (False)
        value = self.log[coordinate]
        del(self.log[coordinate])
        x, y = coordinate
        self.table[y][x] = value
        return (True)
    
    def change_value(self, x, y, type):
        try:
            if (not (self.table[y][x] == 'A') and not(self.table[y][x] == 'B')):
                if (x >= 0 and y >= 0) and (x <= 19 and y <= 19):
                    self.log[(x, y)] = self.table[y][x]
                    self.table[y][x] += type
                    return (True)
        except IndexError:
            pass
        return (False)
    
    def play(self, x, y, target):
        try:
            self.log[(x, y)] = self.table[y][x]
            self.table[y][x] = target
            return (True)
        except IndexError:
            return (False)
        
    def printTable(self):
        size = len(self.table)
        for x in range(size):
            for y in range(size):
                print(self.table[x][y], end=" ")
            print()
    
    def init_scoreboard(self):
        self.table = init_scoreboard(self.table)
        
    def getScore(self, coordinate):
        #self.printTable()
        y, x = coordinate
        score = self.table[x][y]
        if (score == "A" or score == "B"):
            score = 0
        return (abs(score))
    
    def update_scoreboard(self, coordinate, type):
        if (type == 1):
            target = 'A'
        else:
            target = 'B'
        x, y = coordinate
        if (self.table[coordinate[1]][coordinate[0]] != 'A' and self.table[coordinate[1]][coordinate[0]] != 'B'):
            self.log[(coordinate[0], coordinate[1])] = self.table[coordinate[1]][coordinate[0]]
            self.table[coordinate[1]][coordinate[0]] = target
            count = 1
            count += self.change_value(x + 1, y, type)
            count += self.change_value(x - 1, y, type)
            count += self.change_value(x, y + 1, type)
            count += self.change_value(x, y - 1, type)
            count += self.change_value(x + 1, y - 1, type)
            count += self.change_value(x - 1, y + 1, type)
            count += self.change_value(x - 1, y - 1, type)
            count += self.change_value(x + 1, y + 1, type)
            self.undo_time.append(count)

# table = Table()
# test = [[0 for i in range(19)] for j in range(19)]
# table.setTable(test)
# table.play(3, 5, "A")
# table.init_scoreboard()
# table.printTable()
# print("#" * 20)
# table.update_scoreboard((4, 5), -1)
# table.printTable()
# table.undo()
# print("#" * 20)
# table.printTable()