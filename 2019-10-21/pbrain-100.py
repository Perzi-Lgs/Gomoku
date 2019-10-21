import sys
import random as rd
from Interpretor import *
from min_max import *

def main():
    inter = interpretor()
    input()
    print("OK")
    while (inter.analyseInput()):
        table = inter.getMap()
        x, y = find_coordinate(table, 0, 0) 
        #inter.dump(y, x)
        inter.input_tester()

#def main():
#    wcount = True
#    while (True):
#        toto = input()
#        if (wcount):
#            print("OK")
#            wcount = False
#        else:
#            print("1,1")
        
if __name__ == '__main__':
    sys.exit(main())