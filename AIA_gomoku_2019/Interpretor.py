import sys

class interpretor:
    def __init__(self):
        w = 19*19
        self.Matrix = [0 for x in range(w)]
        self.Map = [[0 for x in range(19)] for y in range(19)]
        self.cmd = []
        self.x = 0
        self.y = 0

    def readInput(self):
        self.cmd = sys.stdin.readline()

    def writeOutuput(self, x, y):
        sys.stdout.write(str(x)+','+str(y))
        sys.stdout.flush()
        self.Map[x][y] = 1
        #self.Matrix[(x*19)+y] = 1

    def analyseInput(self) -> bool:
        self.readInput()
        splitedString = self.cmd.split(' ')
        if splitedString[0] == "TURN":
            tmp = splitedString[1].split(',')
            print(tmp)
            #self.Matrix[int(tmp[0]) * 19 + int(tmp[1])] = 2
            self.Map[int(tmp[0])][int(tmp[1])] = 2
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
    def getMatrix(self):
        return self.Matrix

    def getMap(self):
        return self.Map

    def loadBoard(self):
        for i in self.Matrix:
            i = 0

    def printMatrix(self):
        for i in self.Matrix:
            print(i)