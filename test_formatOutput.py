from formatOutput import *

def test_oneType_Empty():
    assert "Test: (None)" == oneType("Test", [])

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

def test_formatRelationships_Single():
   assert "Tests:\n  Test 1 tests Test 2" == formatRelationships("Tests", "tests ", {"Test 1": ["Test 2"]})

def test_formatRelationships_Multiple():
   assert "Tests:\n  Test 1 tests Test 2 and Test 3\n  Test 2 tests Test 2, Test 3 and Test 4" == formatRelationships("Tests", "tests ", {"Test 1": ["Test 2", "Test 3"],"Test 2": ["Test 2", "Test 3", "Test 4"]})

if __name__ == '__main__':

    test_oneType_Empty()
    test_oneType_single()
    test_oneType_two()
    test_oneType_four()
    test_dictSingleKey_Single()
    test_dictSingleKey_Multiple()
    test_formatRelationships_Single()
    test_formatRelationships_Multiple()
    print("Success!!")