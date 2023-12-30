import dictionaryDAG as dDAG
import formatOutput as fO

def createZombieDAG(implementation = 'dDAG'):
    
    if implementation == 'dDAG':
        return dDAG.createDictionaryDAG()

def addTracingRelationship(graph, sickPerson, contactee, implementation = 'dDAG',):

    if implementation == 'dDAG':
        return dDAG.addDictionaryRelationship(sickPerson, contactee, graph)

def displayTracing(graph,implementation = 'dDAG'):

    if implementation == 'dDAG':
        relationships = dDAG.nodeWithEdge(graph)

    return fO.formatRelationships('Contact Records', 'had contact with', relationships)

def identifyPossiblePatientZero(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        patient_zero_list = dDAG.findSinks(graph)

    return fO.oneType('Patient Zero(s)', patient_zero_list)

def identifyPotentialZombies(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        possible_zombies_list = dDAG.findSources(graph)

    return fO.formatRelationships('Potential Zombies', possible_zombies_list)

def identifyNeitherZombieNorPatientZero(graph, implementation = 'dDAG'):
                                        
    if implementation == 'dDAG':
        intermediary_list = dDAG.findIntermediaries(graph)

    return fO.oneType('Neither Patient Zero or Potential Zombie', intermediary_list)

def identifyMostViralPeople(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        most_viral_list = dDAG.findHighestOutgoing(graph)

    return fO.oneType('Most Viral People', most_viral_list)

def identifyMostContactedPerson(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        most_contacted_list = dDAG.findHighestIncoming(graph)
    
    return fO.oneType('Most Contacted', most_contacted_list)

def determineMaximumDistanceFromPotentialZombie(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        distance_dict = dDAG.calcLongestPathsFromSource(graph)
    
    return fO.dictSingleKey('Heights', distance_dict)

def identifySpreaderZombies(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        spreader_zombie_list = dDAG.filterForOutgoingNodeTypes(graph, 'Only Sink')
    
    return fO.oneType("Spreader Zombies", spreader_zombie_list)

def identifyRegularZombies(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        regular_zombie_list = dDAG.filterForOutgoingNodeTypes(graph, 'Both')

    return fO.oneType("Regular Zombies", regular_zombie_list)

def identifyZombiePredators(graph, implementation = 'dDAG'):

    if implementation == 'dDAG':
        zombie_predator_list = dDAG.filterForOutgoingNodeTypes(graph, 'Only Intermediary')
    
    return fO.oneType("Zombie Predators", zombie_predator_list)
    

        

