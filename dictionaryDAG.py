


def createDAG():

    return {}

def addRelationship(node,predecessor, graph):

    graphCopy = graph.copy()

    if node in graphCopy:

        predecessorsCopy = graphCopy[node].copy()
        predecessorsCopy.append(predecessor)
        graphCopy[node] = sorted(predecessorsCopy)

    else:
        graphCopy[node] = [predecessor]

    return dict(sorted(graphCopy.items()))

def nodeWithEdge(graph):

    return graph

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

        


