def test_foo():
    assert True


# Flaky due to non-deterministic builtin-function hash()
def test_unordered_collections():
    s = {"hello", "world", ", how", "are", "you"}
    assert next(s.__iter__()) == "hello"


x = 0;

def test_victim():
    assert x == 0

def test_polluter():
    global x
    x = 5;

