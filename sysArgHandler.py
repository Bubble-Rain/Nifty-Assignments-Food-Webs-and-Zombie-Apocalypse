import sys
import copy
from os import path

currentImplementations = ['dDAG']
defaultImplementation = 'dDAG'

def handleInput():

    arguments = copy.deepcopy(sys.argv)

    if len(arguments) > 3:
        print("Too many arguements")
        sys.exit()

    try:

        if not path.isfile(arguments[1]):
            print("Not a file")
            sys.exit()

    except IndexError:
        print("No file input")
        sys.exit()
    
    try:
        if arguments[2] in currentImplementations:
            return arguments[1], arguments[2]
        else:
            print("Not an implementation")
            sys.exit()
    except IndexError:
        return arguments[1], defaultImplementation

if __name__ == "__main__":

    filePath, implmentation = handleInput()
    print(filePath, implmentation)
