from formatOutput import *

def test_oneType_single():

    assert "Test: Test 1" == oneType("Test", ["Test 1"])

def test_oneType_two():
    assert "Test: Test 1 and Test 2" == oneType("Test", ["Test 1", "Test 2"])

def test_oneType_four():
    assert "Test: Test 1, Test 2, Test 3 and Test 4" == oneType("Test", ["Test 1", "Test 2", "Test 3", "Test 4"])

def test_dictSingleKey_Single():
    assert "Tests:\n  Test 1: 1" == dictSingleKey("Tests", {"Test 1": 1})

def test_dictSingleKey_Multiple():
    assert "Tests:\n  Test 1: 1\n  Test 2: 2\n  Test 3: 3\n  Test 4: 4" == dictSingleKey("Tests", {"Test 1": 1, "Test 2": 2, "Test 3": 3, "Test 4": 4})

#def test_relationships_Multiple():
 #   assert "Tests:\n  Test 1: 1\n  Test 2: 2\n  Test 3: 3\n  Test 4: 4" == formatRelationships("Tests", "test " {"Test 1": 1, "Test 2": 2, "Test 3": 3, "Test 4": 4})

if __name__ == '__main__':

    test_oneType_single()
    test_oneType_two()
    test_oneType_four()
    test_dictSingleKey_Single()
    test_dictSingleKey_Multiple()
    print("Success!!")