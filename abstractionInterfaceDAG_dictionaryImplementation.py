import dictionaryDAG as dDAG

def createDAG():
    return dDAG.createDictionaryDAG()

def addRelationship(node,predecessor,graph):
    return dDAG.addDictionaryRelationship(node,predecessor,graph)

def returnNodeWithEdge(graph):
    return dDAG.nodeWithEdge(graph)

def findSinks(graph):
    return dDAG.findSinks(graph)

def findSources(graph):
    return dDAG.findSources(graph)

def findIntermediaries(graph):
    return dDAG.findIntermediaries(graph)

def findHighestIncoming(graph):
    return dDAG.findHighestIncoming(graph)

def findHighestOutgoing(graph):
    return dDAG.findHighestOutgoing(graph)

def evaluateNodeTypes(graph):
    return dDAG.evaluateIncomingNodeTypes(graph)

def calcLongestPathsFromSource(graph):
    return dDAG.calcLongestPathsFromSource(graph)
