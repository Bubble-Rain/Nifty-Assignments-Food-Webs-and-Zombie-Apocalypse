from dictionaryDAG import *


def test_create_DAG():
    assert len(createDAG()) == 0

def test_add_new_node_DAG():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    assert dict({'1': ["0"]}) == testDAG

def test_add_to_same_node_DAG():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("1","10",testDAG)
    assert dict({'1': ["0","10"]}) == testDAG

def test_add_immutability_key():

    testDAG1 = createDAG()
    testDAG2 = testDAG1

    testDAG1 = addRelationship("1","0",testDAG1)

    assert testDAG1 != testDAG2

def test_add_immutability_value():


    testDAG1 = createDAG()
    testDAG1 = addRelationship("1","0",testDAG1)

    testDAG2 = testDAG1
    testDAG1 = addRelationship("1","10",testDAG1)
    
    testDAG1["1"][0] = "Wrong"

    assert testDAG1 != testDAG2

def test_flatten_predecessors():

    testDAG = createDAG()
    testDAG = addRelationship("1","0",testDAG)
    testDAG = addRelationship("2","0",testDAG)
    testDAG = addRelationship("2","1",testDAG)
    testDAG = addRelationship("1","5",testDAG)
    testDAG = addRelationship("8","6",testDAG)

    assert ["0","0","1","5","6"] == sorted(flattenPredecessors(testDAG))

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
    test_find_sources()
    test_find_sinks()
    test_find_highest_incoming()
    test_find_highest_outgoing()
    print("Success!!")

