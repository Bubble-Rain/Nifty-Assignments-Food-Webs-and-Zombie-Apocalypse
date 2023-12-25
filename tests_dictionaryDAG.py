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

def test_add_immutability():

    testDAG1 = createDAG()
    testDAG2 = testDAG1

    testDAG1 = addRelationship("1","0",testDAG1)

    assert testDAG1 != testDAG2

if __name__ == "__main__":

    test_create_DAG()
    test_add_new_node_DAG()
    test_add_to_same_node_DAG()
    test_add_immutability()
    print("Success!!")

