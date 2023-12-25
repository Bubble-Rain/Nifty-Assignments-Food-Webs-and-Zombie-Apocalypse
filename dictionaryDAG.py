from copy import copy

class directed_acyclic_graph:

    def __init__(self, relationships, nodeNames):
        self.relationships = relationships
        self.nodeNames = nodeNames

def createDAG():

    return directed_acyclic_graph({}, []);

def addRelationship(node,predecessor, graph):

    graphCopy = copy(graph)

    relationshipsCopy = graphCopy.relationships.copy()

    if node in relationshipsCopy:

        predecessorsCopy = relationshipsCopy[node].copy()
        predecessorsCopy.append(predecessor)

        relationshipsCopy[node] = sorted(predecessorsCopy)

    else:
        relationshipsCopy[node] = [predecessor]

    relationshipsCopy = dict(sorted(relationshipsCopy.items()))

    nodeNamesCopy = graphCopy.nodeNames.copy()

    if node not in nodeNamesCopy:
        
        nodeNamesCopy.append(node)
        nodeNamesCopy = sorted(nodeNamesCopy)

    if predecessor not in nodeNamesCopy:
       
       nodeNamesCopy.append(predecessor)
       nodeNamesCopy = sorted(nodeNamesCopy)

    return directed_acyclic_graph(relationshipsCopy, nodeNamesCopy)

def nodeWithEdge(graph):

    return graph.relationships

def flattenPredecessors(graph):

    return [predecessor for predecessors in graph.relationships.values() for predecessor in predecessors]

def calcInDegree(graph):

    return {node: len(graph.relationships[node]) if node in graph.relationships else 0 for node in graph.nodeNames}

def calcOutDegree(graph):

    unique_nodes = findUniqueNodeNames(graph)

    predecessors =  flattenPredecessors(graph)
    numOutgoingDict = {node:predecessors.count(node) for node in set(predecessors)}

    return {node: len(numOutgoingDict[node]) if node in graph else 0 for node in unique_nodes}

def findSinks(graph):

    nodesIncoming = list(graph.keys())
    predecessors =  [predecessor for predecessors in graph.values() for predecessor in predecessors]

    # Sinks are nodes who aren't predecessors for other nodes
    return sorted([node for node in nodesIncoming if node not in set(predecessors)])

def findSources(graph):

    nodesIncoming = list(graph.keys())
    predecessors =  [predecessor for predecessors in graph.values() for predecessor in predecessors]

    # Sources are nodes that have no predecessors
    return sorted([node for node in set(predecessors) if node not in nodesIncoming])

def findHigestIncoming(graph):

    numIncomingDict = {key:len(value) for key,value in graph.items()}
    maxIncoming = max(numIncomingDict.values())

    return sorted([key for key in numIncomingDict.keys() if numIncomingDict[key] == maxIncoming])

def findHighestOutgoing(graph):

    predecessors =  flattenPredecessors(graph)

    numOutgoingDict = {node:predecessors.count(node) for node in set(predecessors)}
    maxOutgoing = max(numOutgoingDict.values())

    return sorted([key for key in numOutgoingDict.keys() if numOutgoingDict[key] == maxOutgoing])




    

        


