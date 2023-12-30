from dictionaryDAG import *


def test_create_DAG():

    testDAG = createDictionaryDAG()

    assert (testDAG.relationships == {}) == (testDAG.nodeNames == [])

def test_add_new_node_DAG():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    assert (dict({'1': ["0"]}) == testDAG.relationships) == (testDAG.nodeNames == ["0","1"])

def test_repeated_node_DAG():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("1","0",testDAG)
    assert (dict({'1': ["0"]}) == testDAG.relationships) == (testDAG.nodeNames == ["0","1"])

def test_add_to_same_node_DAG():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("1","10",testDAG)
    assert (dict({'1': ["0","10"]}) == testDAG.relationships) == (testDAG.nodeNames == ["0","1","10"])

def test_add_immutability_key():

    testDAG1 = createDictionaryDAG()
    testDAG2 = testDAG1

    testDAG1 = addDictionaryRelationship("1","0",testDAG1)

    assert testDAG1.relationships != testDAG2.relationships

def test_add_immutability_value():


    testDAG1 = createDictionaryDAG()
    testDAG1 = addDictionaryRelationship("1","0",testDAG1)

    testDAG2 = testDAG1
    testDAG1 = addDictionaryRelationship("1","10",testDAG1)
    
    testDAG1.relationships["1"][0] = "Wrong"

    assert testDAG1.relationships != testDAG2.relationships


def test_find_succesors():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)

    assert ["1","2"] == findSuccesors("0",testDAG)

def test_flatten_predecessors():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)

    assert ["0","0","1","5","6"] == sorted(flattenPredecessors(testDAG))

def test_calc_incoming_degree():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)

    assert {"0": 0,"1": 2,"2":2,"5": 0,"6": 0,"8":1} == calcInDegree(testDAG)

def test_calc_outgoing_degree():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)

    assert {"0": 2,"1": 1,"2":0,"5": 1,"6": 1,"8":0} == calcOutDegree(testDAG)

def test_find_sources():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    
    assert ["0","5","6"] == findSources(testDAG)

def test_find_sinks():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    
    assert ["2","8"] == findSinks(testDAG)

def test_find_intermediaries():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    
    assert ["1"] == findIntermediaries(testDAG)

def test_find_highest_incoming():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    
    assert ["1","2"] == findHighestIncoming(testDAG)

def test_find_highest_outgoing():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    
    assert ["0","1"] == findHighestOutgoing(testDAG)

def test_calculating_distance_from_furthest_source():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("8","2",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    testDAG = addDictionaryRelationship("9","8",testDAG)
    testDAG = addDictionaryRelationship("10","9",testDAG)
    testDAG = addDictionaryRelationship("10","6",testDAG)

    assert {"10":5, "9":4, "8":3, "2": 2, "1":1, "6": 0, "5": 0, "0": 0 } == calcLongestPathsFromSource(testDAG)

def test_evaluate_node_types():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("8","2",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    testDAG = addDictionaryRelationship("9","8",testDAG)
    testDAG = addDictionaryRelationship("10","9",testDAG)
    testDAG = addDictionaryRelationship("10","6",testDAG)

    manualSinks = {node: "Sink" for node in findSinks(testDAG)} 
    manualSources = {node: "Source" for node in findSources(testDAG)} 
    manualIntermediaries = {node: "Intermediary" for node in findIntermediaries(testDAG)} 
    manual =  {**manualSinks,**manualSources,**manualIntermediaries}
    manual = dict(sorted(manual.items()))

    assert manual == evaluateNodeTypes(testDAG)

def test_evaluating_incoming_node_type():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("8","2",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    testDAG = addDictionaryRelationship("9","8",testDAG)
    testDAG = addDictionaryRelationship("10","9",testDAG)
    testDAG = addDictionaryRelationship("10","6",testDAG)

    assert {"1": "Only Source", "2": "Both", "8": "Both", "9": "Only Intermediary", "10": "Both" } == evaluateIncomingNodeTypes(testDAG)

def test_evaluating_outgoing_node_type():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("8","2",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    testDAG = addDictionaryRelationship("9","8",testDAG)
    testDAG = addDictionaryRelationship("10","9",testDAG)
    testDAG = addDictionaryRelationship("10","6",testDAG)
    assert {"0": "Only Intermediary", "1": "Only Intermediary", "2": "Only Intermediary", "5" : "Only Intermediary", "6": "Both", "8": "Only Intermediary", "9": "Only Sink"} == evaluateOutgoingNodeTypes(testDAG)

def test_filtering_incoming_node_type():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("8","2",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    testDAG = addDictionaryRelationship("9","8",testDAG)
    testDAG = addDictionaryRelationship("10","9",testDAG)
    testDAG = addDictionaryRelationship("10","6",testDAG)
    
    assert (["9"] == filterForIncomingNodeTypes(testDAG, "Only Intermediary")) == (["1"] == filterForIncomingNodeTypes(testDAG, "Only Source") ) and  (["10", "2", "8"] == filterForIncomingNodeTypes(testDAG, "Both"))

def test_filtering_outgoing_node_type():

    testDAG = createDictionaryDAG()
    testDAG = addDictionaryRelationship("1","0",testDAG)
    testDAG = addDictionaryRelationship("2","0",testDAG)
    testDAG = addDictionaryRelationship("2","1",testDAG)
    testDAG = addDictionaryRelationship("8","2",testDAG)
    testDAG = addDictionaryRelationship("1","5",testDAG)
    testDAG = addDictionaryRelationship("8","6",testDAG)
    testDAG = addDictionaryRelationship("8","1",testDAG)
    testDAG = addDictionaryRelationship("9","8",testDAG)
    testDAG = addDictionaryRelationship("10","9",testDAG)
    testDAG = addDictionaryRelationship("10","6",testDAG)
    
    assert (["0","1","2","5","8"] == filterForOutgoingNodeTypes(testDAG, "Only Intermediary")) == (["9"] == filterForOutgoingNodeTypes(testDAG, "Only Sink") ) and  (["6"] == filterForOutgoingNodeTypes(testDAG, "Both"))


if __name__ == "__main__":

    test_create_DAG()
    test_add_new_node_DAG()
    test_repeated_node_DAG()
    test_add_to_same_node_DAG()

    test_add_immutability_key()
    test_add_immutability_value()

    test_find_succesors()
    test_flatten_predecessors()

    test_calc_incoming_degree()
    test_calc_outgoing_degree()

    test_find_sinks()
    test_find_sources()
    test_find_intermediaries()

    test_find_highest_incoming()
    test_find_highest_outgoing()

    test_calculating_distance_from_furthest_source()
    
    test_evaluate_node_types()

    test_evaluating_incoming_node_type()
    test_evaluating_outgoing_node_type()

    test_filtering_incoming_node_type()
    test_filtering_outgoing_node_type()

    print("Success!!")

