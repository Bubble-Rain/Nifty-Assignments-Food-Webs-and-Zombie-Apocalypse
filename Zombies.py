import dictionaryDAG as dDAG
import formatOutput as fO
import ingestCSV as iCSV

"""
Zombie DAG are Implemented as an inverted graph due to dictionaryDAG assuming that the list is predecessors of a node.
Whereas the assignment assumes that the list are the successors of the node.

"""

def createZombieDAG(implementation = 'dDAG'):
    
    if implementation == 'dDAG':
        return dDAG.createDictionaryDAG()

def addTracingRelationship(implementation = 'dDAG'):

    if implementation == 'dDAG':
        return dDAG.addDictionaryRelationship
    
def fileIngestion(path, implementation = 'dDAG'):

    DAG = createZombieDAG(implementation)

    return iCSV.fileIngestion(path, DAG, addTracingRelationship(implementation))


def displayTracing(graph,implementation = 'dDAG'):

    if implementation == 'dDAG':
        relationships = dDAG.nodeWithEdge(graph)

    return fO.formatRelationships('Contact Records', 'had contact with ', relationships)

def identifyPossiblePatientZero(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        patient_zero_list = dDAG.findSinks(graph)

    return fO.oneType('Patient Zero(s)', patient_zero_list)

def identifyPotentialZombies(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        possible_zombies_list = dDAG.findSources(graph)

    return fO.oneType('Potential Zombies', possible_zombies_list)

def identifyNeitherZombieNorPatientZero(graph, implementation = 'dDAG'):
                                        
    if implementation == 'dDAG':
        intermediary_list = dDAG.findIntermediaries(graph)

    return fO.oneType('Neither Patient Zero or Potential Zombie', intermediary_list)

def identifyMostViralPeople(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        most_viral_list = dDAG.findHighestIncoming(graph)

    return fO.oneType('Most Viral People', most_viral_list)

def identifyMostContactedPerson(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        most_contacted_list = dDAG.findHighestOutgoing(graph)
    
    return fO.oneType('Most Contacted', most_contacted_list)

def determineMaximumDistanceFromPotentialZombie(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        distance_dict = dDAG.calcLongestPathsFromSource(graph)
    
    return fO.dictSingleKey('Heights', distance_dict, 'value')

def identifySpreaderZombies(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        spreader_zombie_list = dDAG.filterForIncomingNodeTypes(graph, 'Only Source')
    
    return fO.oneType("Spreader Zombies", spreader_zombie_list)

def identifyRegularZombies(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        regular_zombie_list = dDAG.filterForIncomingNodeTypes(graph, 'Both')

    return fO.oneType("Regular Zombies", regular_zombie_list)

def identifyZombiePredators(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        zombie_predator_list = dDAG.filterForIncomingNodeTypes(graph, 'Only Intermediary')
    
    return fO.oneType("Zombie Predators", zombie_predator_list)
    

        

