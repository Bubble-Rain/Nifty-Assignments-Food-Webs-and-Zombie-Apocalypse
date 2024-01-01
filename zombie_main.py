from Zombies import *

implementation = 'dDAG'

def part1(graph):
    return displayTracing(graph,implementation)

def part2(graph):
    return identifyPossiblePatientZero(graph,implementation)

def part3(graph):
    return identifyPotentialZombies(graph,implementation)

def part4(graph):
    return identifyNeitherZombieNorPatientZero(graph,implementation)

def part5(graph):
    return identifyMostViralPeople(graph,implementation)

def part6(graph):
    return identifyMostContactedPerson(graph,implementation)

def part7(graph):
    return determineMaximumDistanceFromPotentialZombie(graph,implementation)

def part8(graph):

    return "For an A+:" + "\n  " + identifySpreaderZombies(graph,implementation) + "\n  " + identifyRegularZombies(graph,implementation) + "\n  " + identifyZombiePredators(graph,implementation)

if __name__ == '__main__':

    contactTracing = fileIngestion('zombieFiles/Input/DataSet1.txt', implementation)

    
    output = part1(contactTracing) + '\n\n' + part2(contactTracing) + '\n' + part3(contactTracing) + '\n' + part4(contactTracing) + '\n' + part5(contactTracing) + '\n' + part6(contactTracing) + '\n\n' + part7(contactTracing) + "\n\n" + part8(contactTracing)

    print(output)
    
