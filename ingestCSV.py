import csv
import copy

def fileIngestion(path, graph, addRelationshipFunction):

    
    graphCopy = copy.copy(graph)
    csvFile = open(path)
    csvReader = csv.reader(csvFile, delimiter = ',')
    
    for row in csvReader:

        rowCopy = copy.deepcopy(row)

        node = rowCopy[0]
        predecessors = rowCopy[1:]

        for predecessor in predecessors:
            graphCopy = addRelationshipFunction(node, predecessor, graphCopy)
    csvFile.close()  
    return graphCopy
