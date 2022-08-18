import random
import numpy as np
from pathlib import Path


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
    assert np.random.randint(0, 2) == 1

x = 0

def test_victim():
    assert x == 0

def test_polluter():
    global x
    x = 5


def test_self_polluter():
    # assert that file does NOT exists and create it if not
    self_polluter_file = Path("/tmp/.minimal_flaky_example_self_polluter_file")
    file_existed = self_polluter_file.exists()
    self_polluter_file.touch(exist_ok=True)
    assert not file_existed

def test_self_statesetter():
    # assert that file exists and create it if not
    self_state_setter_file = Path("/tmp/.minimal_flaky_example_self_state_setter_file")
    file_existed = self_state_setter_file.exists()
    self_state_setter_file.touch(exist_ok=True)
    assert file_existed
