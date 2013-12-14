from __future__ import print_function, division

from itertools import *
from functools import *
from operator import *

from scipy import sparse
import numpy as np
from matplotlib import pylab as pl

def union(a):
    return reduce(set.union, a, set())


def possible_adjacents((x, y)):
    """
    """
    return set(map(
        lambda (dx, dy): (x + dx, y + dy),
        product(
            range(-1, 1 + 1),
            range(-1, 1 + 1),
        )
    )) - {(x, y)}


def count_adjacent(world, cell):
    return len(
        possible_adjacents(cell) & world
    )


def evolve(world):
    """
    world : {(x, y)}
        set of alive cells
    """
    active_cells = union(map(possible_adjacents, world))
    dead_active_cells = active_cells - world

    still_alive = set(filter(
        lambda cell: count_adjacent(world, cell) in (2, 3),
        world
    ))

    newborns = set(filter(
        lambda cell: count_adjacent(world, cell) in (3,),
        dead_active_cells
    ))

    new_world = still_alive | newborns

    return new_world


def render_matrix(cells):
    if len(cells) == 0:
        return np.array([[0]])
    def min_index(cells, index):
        return min(cells, key=itemgetter(index))[index]

    mins = map(partial(min_index, cells), range(2))

    xs, ys = zip(*cells)

    xs, ys = map(
        lambda (min_k, ks):\
            map(neg, map(partial(sub, min_k), ks)),
        zip(mins, [xs, ys])
    )
    matrix_representation = sparse.coo_matrix(
        ([1,] * len(cells), (xs, ys))
    ).todense()

    return matrix_representation


from time import sleep


diehard = {
    (2, 1),
    (2, 2),
    (1, 2),

    (7, 3),

    (6, 1),
    (7, 1),
    (8, 1),
}


def render(world):
    view = render_matrix(world)
    pl.clf()
    pl.imshow(view, interpolation='nearest')
    pl.axis([0, 15, 0, 15])
    pl.draw()
    pl.show()
    sleep(0.1)
    render(evolve(world))

pl.ion()

render(diehard)
