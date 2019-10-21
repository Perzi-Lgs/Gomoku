import sys
from min_max import find_coordinate
from Table import *

class Interpretor(object):
    def __init__(self):
        self.counter = 0
        self.take = []
        self.table = []
        self.alive = True
        self.message = ""
        self.message_type = []
        self.bind_action = {
            "start":self.my_start,
            "turn":self.my_turn,
            "begin":self.my_begin,
            #"board":self.my_board,
            "end":self.my_end,
            "print":self.printMap
        }
    
    def readInput(self):
        self.message = input()
        self.message = self.message.lower().split(" ")
        self.message_type = self.message[0]
        try:
            self.bind_action[self.message_type]()
        except KeyError:
            pass
            #print(self.message)
        
    def my_start(self):
        try:
            self.x = 0
            self.size = int(self.message[1])
            self.table = [[0 for i in range(self.size)] for j in range(self.size)]
            print("OK")
        except:
            print("KO")
    
    def my_turn(self):
        try:
            coordinate = self.message[1].split(",")
            x = int(coordinate[0])
            y = int(coordinate[1])
            self.take.append((x, y))
            self.table[x][y] = 'B'
            my_y, my_x = find_coordinate(self.table, 0, 0)
            self.coordinatePrinter(my_x, my_y)
            #self.printMap()
            # self.coordinatePrinter(self.x, 1)
            # self.x += 1
            # self.counter += 1
        except IndexError as e:
            print(e)
        
    def my_begin(self):
        self.coordinatePrinter(10, 10)

    def my_board(self):
        pass
        
    def my_end(self):
        self.alive = False
        
    def printMap(self):
        for y in range(self.size):
            for x in range(self.size):
                print(self.table[x][y], end=" ")
            print()
    def coordinatePrinter(self, x, y):
        print(str(x)+","+str(y))
        self.table[x][y] = 'A'

inter = Interpretor()

while (inter.alive):
    inter.readInput()
