from formatOutput import *

def test_oneType_single():

    assert "Test: Test 1" == oneType("Test", ["Test 1"])

def test_oneType_two():
    assert "Test: Test 1 and Test 2" == oneType("Test", ["Test 1", "Test 2"])

def test_oneType_four():
    assert "Test: Test 1, Test 2, Test 3 and Test 4" == oneType("Test", ["Test 1", "Test 2", "Test 3", "Test 4"])


if __name__ == '__main__':

    test_oneType_single()
    test_oneType_two()
    test_oneType_four()
    print("Success!!")