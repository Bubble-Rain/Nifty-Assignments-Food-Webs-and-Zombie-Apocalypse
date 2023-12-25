from dictionaryDAG import *


def test_create_DAG():

    testDAG = createDAG()

    assert (testDAG.relationships == {}) == (testDAG.nodeNames == [])

def test_add_new_node_DAG():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    assert (dict({'1': ["0"]}) == testDAG.relationships) == (testDAG.nodeNames == ["0","1"])

def test_add_to_same_node_DAG():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("1","10",testDAG)
    assert (dict({'1': ["0","10"]}) == testDAG.relationships) == (testDAG.nodeNames == ["0","1","10"])

def test_add_immutability_key():

    testDAG1 = createDAG()
    testDAG2 = testDAG1

    testDAG1 = addRelationship("1","0",testDAG1)

    assert testDAG1.relationships != testDAG2.relationships

def test_add_immutability_value():


    testDAG1 = createDAG()
    testDAG1 = addRelationship("1","0",testDAG1)

    testDAG2 = testDAG1
    testDAG1 = addRelationship("1","10",testDAG1)
    
    testDAG1.relationships["1"][0] = "Wrong"

    assert testDAG1.relationships != testDAG2.relationships

def test_flatten_predecessors():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)

    assert ["0","0","1","5","6"] == sorted(flattenPredecessors(testDAG))

def test_calc_incoming_degree():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)

    assert {"0": 0,"1": 2,"2":2,"5": 0,"6": 0,"8":1} == calcInDegree(testDAG)

def test_calc_outgoing_degree():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)

    assert {"0": 2,"1": 1,"2":0,"5": 1,"6": 1,"8":0} == calcOutDegree(testDAG)

def test_find_sources():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)
    
    assert ["0","5","6"] == findSources(testDAG)

def test_find_sinks():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)
    
    assert ["2","8"] == findSinks(testDAG)

def test_find_incoming():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)
    
    assert ["1","2"] == findHigestIncoming(testDAG)





def test_find_highest_incoming():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)
    
    assert ["1","2"] == findHigestIncoming(testDAG)

def test_find_highest_outgoing():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)
    testDAG = addRelationship("8","1",testDAG)
    
    assert ["0","1"] == findHighestOutgoing(testDAG)

if __name__ == "__main__":

    test_create_DAG()
    test_add_new_node_DAG()
    test_add_to_same_node_DAG()

    test_add_immutability_key()
    test_add_immutability_value()

    
    test_flatten_predecessors()

    
    test_calc_incoming_degree()
    test_calc_outgoing_degree()

    test_find_sinks()
    test_find_sources()

    test_find_highest_incoming()
    """
    test_find_sources()
    test_find_sinks()
    test_find_highest_incoming()
    test_find_highest_outgoing()
    """
    print("Success!!")

