import pytest

#Function to test squre 
def square(n):
    return n ** 2

#Function to test cube
def cube(n):
    return n ** 3

#Function to test fifth power
def fifth_power(n):
    return n ** 5

#testing the squre function

def test_squre():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-1) == 1
    
#testing the cube function
def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(-1) == -1
    
#testing the fifth power function
def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(-1) == -1    
    
#test for invalid input

def test_invalid_input():
    with pytest.raises(TypeError):
        square("a")
    with pytest.raises(TypeError):
        cube(None)
    with pytest.raises(TypeError):
        fifth_power([])                                                                                                                                                                             