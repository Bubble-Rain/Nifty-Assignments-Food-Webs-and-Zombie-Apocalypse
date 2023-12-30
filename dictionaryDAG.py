from copy import copy

class directed_acyclic_graph:

    def __init__(self, relationships, nodeNames):
        self.relationships = relationships
        self.nodeNames = nodeNames

def createDictionaryDAG():

    return directed_acyclic_graph({}, []);

def addDictionaryRelationship(node,predecessor, graph):

    graphCopy = copy(graph)

    relationshipsCopy = graphCopy.relationships.copy()

    if node in relationshipsCopy:

        predecessorsCopy = relationshipsCopy[node].copy()
        
        if predecessor in predecessorsCopy:
            return graph

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

def findSuccesors(node,graph):

    return [succesor for succesor, predecessors in graph.relationships.items() if node in predecessors]

def calcInDegree(graph):

    return {node: len(graph.relationships[node]) if node in graph.relationships else 0 for node in graph.nodeNames}

def calcOutDegree(graph):

    predecessors =  flattenPredecessors(graph)
    numOutgoingDict = {node:predecessors.count(node) for node in set(predecessors)}

    return {node: numOutgoingDict[node] if node in numOutgoingDict else 0 for node in graph.nodeNames}

def filterForDegreeByN(degree_dict, num_desired):

    return [node for node, num_degree in degree_dict.items() if num_degree == num_desired]

def findSinks(graph):

    return filterForDegreeByN(calcOutDegree(graph),0)

def findSources(graph):

    indegree = calcInDegree(graph)

    return filterForDegreeByN(calcInDegree(graph),0)

def findIntermediaries(graph):

    indgree = calcInDegree(graph)
    outdegree = calcOutDegree(graph)

    return [node for node in graph.nodeNames if indgree[node] > 0 and outdegree[node] > 0]

def findHighestIncoming(graph):

    indegree = calcInDegree(graph)
    max_indegree = max(indegree.values())

    return filterForDegreeByN(indegree,max_indegree)

def findHighestOutgoing(graph):

    outdegree = calcOutDegree(graph)
    max_outdegree = max(outdegree.values())

    return filterForDegreeByN(outdegree,max_outdegree)

def evaluateNodeType(indegree, outdegree):

    if indegree == 0:
        return "Source"
    elif outdegree == 0:
        return "Sink"
    else:
        return "Intermediary"

def evaluateNodeTypes(graph):

    indgree = calcInDegree(graph)
    outdegree = calcOutDegree(graph)

    return {node: evaluateNodeType(indgree[node], outdegree[node]) for node in graph.nodeNames}

def evaluateIncomingNodeType(relatedNodes, nodeTypesDict):

    nodeTypes = [nodeTypesDict[node] for node in relatedNodes]

    # By definition a Sink should not be an incoming connection
    types = ["Source","Intermediary"]

    type_count = {type:nodeTypes.count(type) for type in types}

    if type_count["Source"] > 0 and type_count["Intermediary"] > 0:
        return "Both"
    elif type_count["Source"] > 0:
        return "Only Source"
    else:
        return "Only Intermediary"
    
def evaluateIncomingNodeTypes(graph):

    nodeTypes = evaluateNodeTypes(graph)

    return {node: evaluateIncomingNodeType(graph.relationships[node], nodeTypes) for node in graph.relationships.keys()}

def filterForIncomingNodeTypes(graph, desiredType):

    nodeTypes = evaluateIncomingNodeTypes(graph)

    return [node for node, nodeType in nodeTypes.items() if nodeType == desiredType]

def evaluateOutgoingNodeType(relatedNodes, nodeTypesDict):

    nodeTypes = [nodeTypesDict[node] for node in relatedNodes]

    # By definition a Source should not be an outgoing direction
    types = ["Sink","Intermediary"]

    type_count = {type:nodeTypes.count(type) for type in types}

    if type_count["Sink"] > 0 and type_count["Intermediary"] > 0:
        return "Both"
    elif type_count["Sink"] > 0:
        return "Only Sink"
    else:
        return "Only Intermediary"
    
def evaluateOutgoingNodeTypes(graph):

    nodeTypes = evaluateNodeTypes(graph)

    return {node: evaluateOutgoingNodeType(findSuccesors(node, graph), nodeTypes) for node in graph.nodeNames if findSuccesors(node, graph)}

def filterForOutgoingNodeTypes(graph, desiredType):

    nodeTypes = evaluateOutgoingNodeTypes(graph)

    return [node for node, nodeType in nodeTypes.items() if nodeType == desiredType]

def calcLongestPath(node, relationships):

    if node not in relationships:
        return 0
    else:

        predecessors = relationships[node]
        predecessorsDistance = [ calcLongestPath(predecessor, relationships) for predecessor in predecessors]

        return 1 + max(predecessorsDistance)

def calcLongestPathsFromSource(graph):
    
    data = {node:calcLongestPath(node, graph.relationships) for node in graph.nodeNames}

    return dict(sorted(data.items(), key = lambda x: (x[1],x[0]), reverse = True))

    




    

        


