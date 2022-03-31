import random
import numpy as np


def test_foo():
    assert True

def test_unordered_collections():
    """
    This test is flaky due to the non-deterministic builtin-function hash()
    that controls the ordering within sets
    """
    s = {"hello", "world"}
    assert next(s.__iter__()) == "hello"


def test_random():
    assert random.randint(0, 1) == 1


def test_numpy_random():
    assert np.random(0, 2) == 1

x = 0;

def test_victim():
    assert x == 0

def test_polluter():
    global x
    x = 5;

