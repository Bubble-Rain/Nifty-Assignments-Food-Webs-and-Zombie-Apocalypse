


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


def flattenPredecessors(graph):

    return [predecessor for predecessors in graph.values() for predecessor in predecessors]

def findUniqueNodeNames(graph):

    nodeList = flattenPredecessors(graph)
    nodeList.extend(graph.keys())

    return sorted(list(set(nodeList)))

def calcInDegree(graph):

    unique_nodes = findUniqueNodeNames(graph)

    return {node: len(graph[node]) if node in graph else 0 for node in unique_nodes}

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




    

        


