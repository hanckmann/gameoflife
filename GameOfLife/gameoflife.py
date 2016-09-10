""" Game of life, basic implementation.

author: Patrick Hanckmann
e-mail: patrick@hanckmann.com
"""

import numpy
from random import uniform


def random_world(width=10, height=10, fill_chance=.15):
    """ Generate random world """
    world = numpy.zeros((width, height))
    # Generate random world
    for wi in range(0, width):
        for hi in range(0, height):
            rvalue = uniform(0.0, 1.0)
            if rvalue <= fill_chance:
                world[wi, hi] = 1
    return world


def next_tick(world, born=[3], survive=[2, 3]):
    """ Execute gol rules on world (default rules: B3,S23) """
    (width, height) = world.shape
    next_world = numpy.zeros((width, height))
    for wi in range(0, width):
        for hi in range(0, height):
            wi_plus = wi + 1
            hi_plus = hi + 1
            if wi == width - 1:
                wi_plus = -1
            if hi == height - 1:
                hi_plus = -1
            neighbours = 0
            neighbours += world[wi - 1, hi - 1]
            neighbours += world[wi - 1, hi]
            neighbours += world[wi - 1, hi_plus]
            neighbours += world[wi, hi - 1]
            neighbours += world[wi, hi_plus]
            neighbours += world[wi_plus, hi - 1]
            neighbours += world[wi_plus, hi]
            neighbours += world[wi_plus, hi_plus]
            if not world[wi, hi]:
                if neighbours in born:
                    next_world[wi, hi] = 1
            else:
                if neighbours in survive:
                    next_world[wi, hi] = 1
    return next_world


def is_unique(tick, world, seen_worlds=dict()):
    """ Check if the world has been seen before (and when) """
    new = True
    world_hash = hash(world.tostring())
    if world_hash in seen_worlds.keys():
        new = False
        tick = seen_worlds[world_hash]
    else:
        seen_worlds[world_hash] = tick

    return (seen_worlds, new, tick)


def show_world(world):
    """ Print the world to screen """
    (width, height) = world.shape
    for hi in range(0, height):
        line = ''
        for wi in range(0, width):
            if world[wi, hi]:
                line += 'X'
            else:
                line += '-'
            line += ''
        print(line)
