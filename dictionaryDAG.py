


def createDAG():

    return {}

def addRelationship(node,predecessor, graph):

    graphCopy = graph.copy()

    if node in graphCopy:

        predecessorsCopy = graphCopy[node].copy()
        predecessorsCopy.append(predecessor)
        graphCopy[node] = predecessorsCopy

    else:
        graphCopy[node] = [predecessor]

    return graphCopy

        


