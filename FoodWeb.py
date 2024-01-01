import dictionaryDAG as dDAG
import formatOutput as fO
import ingestCSV as iCSV

def createFoodWebDAG(implementation = 'dDAG'):
    
    if implementation == 'dDAG':
        return dDAG.createDictionaryDAG()

def addPredatorPreyRelationship(implementation = 'dDAG'):

    if implementation == 'dDAG':
        return dDAG.addDictionaryRelationship
    
def fileIngestion(path, implementation = 'dDAG'):

    DAG = createFoodWebDAG(implementation)

    return iCSV.fileIngestion(path, DAG, addPredatorPreyRelationship(implementation))


def displayFoodWeb(graph,implementation = 'dDAG'):

    if implementation == 'dDAG':
        relationships = dDAG.nodeWithEdge(graph)

    return fO.formatRelationships('Predators and Prey', 'eats ', relationships)

def identifyApexPredator(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        apex_predator_list = dDAG.findSinks(graph)

    return fO.oneType('Apex Predators', apex_predator_list)

def identifyProducers(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        producers_list = dDAG.findSources(graph)

    return fO.oneType('Producers',  producers_list)

def identifyMostFlexibleEaters(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        most_flexible_list = dDAG.findHighestIncoming(graph)

    return fO.oneType('Most Flexible Eaters', most_flexible_list)

def identifyTastiestOrganism(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        tastiest_list = dDAG.findHighestOutgoing(graph)
    
    return fO.oneType('Tastiest', tastiest_list)

def determineHeightOrganism(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        distance_dict = dDAG.calcLongestPathsFromSource(graph)
    
    return fO.dictSingleKey('Heights', distance_dict)

def identifyHerbivores(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        herbivore_list = dDAG.filterForIncomingNodeTypes(graph, 'Only Source')
    
    return fO.oneType("Herbivores", herbivore_list)

def identifyOmnivores(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        omnivores_list = dDAG.filterForIncomingNodeTypes(graph, 'Both')

    return fO.oneType("Omnivores", omnivores_list)

def identifyCarnivores(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        carnivores_list = dDAG.filterForIncomingNodeTypes(graph, 'Only Intermediary')
    
    return fO.oneType("Carnivores", carnivores_list)
    

        

