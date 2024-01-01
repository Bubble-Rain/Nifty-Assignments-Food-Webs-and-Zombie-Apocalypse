from Zombies import *
from sysArgHandler import *
from outputHandler import *

outputPath = "zombieFiles/Output/"

def part1(graph,implementation):
    return displayTracing(graph,implementation)

def part2(graph,implementation):
    return identifyPossiblePatientZero(graph,implementation)

def part3(graph,implementation):
    return identifyPotentialZombies(graph,implementation)

def part4(graph,implementation):
    return identifyNeitherZombieNorPatientZero(graph,implementation)

def part5(graph,implementation):
    return identifyMostViralPeople(graph,implementation)

def part6(graph,implementation):
    return identifyMostContactedPerson(graph,implementation)

def part7(graph,implementation):
    return determineMaximumDistanceFromPotentialZombie(graph,implementation)

def part8(graph,implementation):

    return "For an A+:" + "\n  " + identifySpreaderZombies(graph,implementation) + "\n  " + identifyRegularZombies(graph,implementation) + "\n  " + identifyZombiePredators(graph,implementation)

if __name__ == '__main__':

    filePath, implementation = handleInput()

    contactTracing = fileIngestion(filePath, implementation)

    output = part1(contactTracing, implementation) + '\n\n' + part2(contactTracing, implementation) + '\n' + part3(contactTracing, implementation) + '\n' + part4(contactTracing, implementation) + '\n' + part5(contactTracing, implementation) + '\n' + part6(contactTracing, implementation) + '\n\n' + part7(contactTracing, implementation) + "\n\n" + part8(contactTracing, implementation)

    print(output)

    writeFile(outputPath, '-out', filePath, output)

    print("Finished Outputting")









