import pytest

from day_1 import find_floor

def test_solve1():
    assert 0 == find_floor("(())")

def test_solve2():
    assert 0 == find_floor("()()")

def test_solve3():
    assert 3 == find_floor("(((")

def test_solve4():
    assert 3 == find_floor("(()(()(")

def test_solve5():
    assert 3 == find_floor("))(((((")

def test_solve6():
    assert -1 == find_floor("())")

def test_solve7():
    assert -1 == find_floor("))(")

def test_solve8():
    assert -3 == find_floor(")))")

def test_solve9():
    assert -3 == find_floor(")())())")