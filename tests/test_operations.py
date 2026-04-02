from src.math_operations import add, sub, mul

def test_add():
    assert add(2,9) == 11
    assert add(-1,10) == 9
    assert add(0,0) == 0
    assert add(-5,1) == -4


def test_sub(): 
    assert sub(5,2) == 3
    assert sub(0,1) == -1
    assert sub(-3,-11) == -8
    assert sub(29,5) == 24
    assert sub(0,0) == 0

def test_mul():
    assert mul(3,4) == 12
    assert mul(-2,7) == -14
    assert mul(0,10) == 0
    assert mul(-3,-1) == 3
    assert mul(5,0) == 0