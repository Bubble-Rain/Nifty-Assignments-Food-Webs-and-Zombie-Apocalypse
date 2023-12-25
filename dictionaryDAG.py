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

    predecessors =  flattenPredecessors(graph)
    numOutgoingDict = {node:predecessors.count(node) for node in set(predecessors)}

    return {node: numOutgoingDict[node] if node in numOutgoingDict else 0 for node in graph.nodeNames}

def findSinks(graph):

    outdegree = calcOutDegree(graph)

    return [node for node, num_out in outdegree.items() if num_out == 0]

def findSources(graph):

    indegree = calcInDegree(graph)

    return [node for node, num_in in indegree.items() if num_in == 0]

def findHigestIncoming(graph):

    indegree = calcInDegree(graph)
    max_indegree = max(indegree.values())

    return [node for node, num_in in indegree.items() if num_in == max_indegree]

def findHighestOutgoing(graph):

    outdegree = calcOutDegree(graph)
    max_outdegree = max(outdegree.values())

    return [node for node, num_in in outdegree.items() if num_in == max_outdegree]




    

        


