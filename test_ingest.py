import ingestCSV
import dictionaryDAG

def test_ingest_dictDAG_simple():

    DAG = dictionaryDAG.createDictionaryDAG()

    DAG = ingestCSV.fileIngestion("testCSV.txt", DAG, dictionaryDAG.addDictionaryRelationship )

    assert (DAG.relationships == {'Darren': ['Shan'], 'Shan': ['George']}) == (DAG.nodeNames == ['Darren', 'George', 'Shan'])

def test_ingest_dictDAG_hard():

    DAG = dictionaryDAG.createDictionaryDAG()

    DAG = ingestCSV.fileIngestion("testCSVHard.txt", DAG, dictionaryDAG.addDictionaryRelationship )

    assert (DAG.relationships == {'Bird': ['Crab', 'Limpets', 'Mussels', 'Prawn', 'Whelk'], 'Crab': ['Limpets', 'Mussels'], 'Fish': ['Prawn'], 'Limpets': ['Seaweed'], 'Lobster': ['Crab', 'Limpets', 'Mussels', 'Whelk'], 'Mussels': ['Phytoplankton', 'Zooplankton'], 'Prawn': ['Zooplankton'], 'Whelk': ['Limpets', 'Mussels'], 'Zooplankton': ['Phytoplankton']}) == (DAG.nodeNames == ['Bird', 'Crab', 'Fish', 'Limpets', 'Lobster', 'Mussels', 'Phytoplankton', 'Prawn', 'Seaweed', 'Whelk', 'Zooplankton'])

if __name__ == '__main__':

    test_ingest_dictDAG_simple()
    test_ingest_dictDAG_hard()
    print("Success!!")