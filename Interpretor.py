import sys

class interpretor:
    def __init__(self):
        w = 19*19;
        self.Matrix = [0 for x in range(w)]
        self.Map = [[0 for x in range(19)] for y in range(19)]
        cmd = []

    def readInput(self):
        self.cmd = sys.stdin.readline()

    def writeOutuput(self, x, y):
        self.x = x
        self.y = y
        sys.stdout.write(x+','+y)
        sys.stdout.flush()
        self.Map[x][y] = 1
        self.Matrix[(x*19)+y] = 1

    def analyseInput(self) -> bool:
        splitedString = self.cmd.split(' ')
        if splitedString[0] == "TURN":
            tmp = splitedString[1].split(',')
            self.Matrix[int(tmp[0]) * 19 + int(tmp[1])] = 2
            self.Map[x][y]
            return True
        elif splitedString[0] == "START":
            return True
        elif self.cmd == "BEGIN\n":
            return True
        elif self.cmd == "END\n":
            return False
        elif self.cmd == "BOARD\n":
            self.loadBoard()
            while self.cmd != "DONE\n":
                self.readInput()
                if self.cmd != "DONE\n":
                    splitedString = self.cmd.split(',')
                    self.Matrix[int(splitedString[0]) * 19 + int(splitedString[1])] = int(splitedString[2])
                    self.Map[splitedString[0]][splitedString[1]]
            return True
    def getMap(self):
        return self.Matrix

    def loadBoard(self):
        for i in self.Matrix:
            i = 0

    def printMatrix(self):
        for i in self.Matrix:
            print(i)