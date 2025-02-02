import halolib.core as hcore

def test_add():
    assert hcore.add(2, 3) == 5
    assert hcore.add(-1, 1) == 0