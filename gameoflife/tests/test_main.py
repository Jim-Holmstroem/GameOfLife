from __future__ import print_function, division

from main import *
from nose.tools import *

def test_evolve_none():
    assert_equal(
        evolve(set()),
        set()
    )

def test_evolve_lonestar():
    assert_equal(
        evolve({(1, 1)}),
        set()
    )

def test_evolve_pair():
    assert_equal(
        evolve({(1, 1), (1, 2)}),
        set()
    )

def test_blinker():
    assert_equal(
        evolve({(1, 1), (1, 2), (1, 3)}),
        {(0, 2), (1, 2), (2, 2)}
    )

def test_possible_adjacents():
    assert_equal(
        len(possible_adjacents((1, 1))),
        8
    )

def test_adjacent_3():
    assert_equal(
        count_adjacent({(1, 1), (1, 2), (1, 3)}, (0, 2)),
        3
    )

