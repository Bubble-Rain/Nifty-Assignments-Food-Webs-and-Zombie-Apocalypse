from FoodWeb import *
from sysArgHandler import *
from outputHandler import *

outputPath = "foodwebFiles/Output/"

def part1(graph,implementation):
    return displayFoodWeb(graph,implementation)

def part2(graph,implementation):
    return identifyApexPredator(graph,implementation)

def part3(graph,implementation):
    return identifyProducers(graph,implementation)

def part4(graph,implementation):
    return identifyMostFlexibleEaters(graph,implementation)

def part5(graph,implementation):
    return identifyTastiestOrganism(graph,implementation)

def part6(graph,implementation):
    return determineHeightOrganism(graph,implementation)

def part7(graph,implementation):

    return "For an A+:" + "\n  " + identifyHerbivores(graph,implementation) + "\n  " + identifyOmnivores(graph,implementation) + "\n  " + identifyCarnivores(graph,implementation)

if __name__ == '__main__':

    filePath, implementation = handleInput()

    foodWeb = fileIngestion(filePath, implementation)

    output = part1(foodWeb, implementation) + '\n\n' + part2(foodWeb, implementation) + '\n' + part3(foodWeb, implementation) + '\n' + part4(foodWeb, implementation) + '\n' + part5(foodWeb, implementation) + '\n\n' + part6(foodWeb, implementation) + '\n\n' + part7(foodWeb, implementation)

    print(output)

    writeFile(outputPath, '_Output', filePath, output)

    print("Finished Outputting")









