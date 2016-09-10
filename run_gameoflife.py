#!/usr/bin/python
# -*- coding: utf-8 -*-

""" GOF Main """

import sys
import time
from GameOfLife import gameoflife


def main(argv):
    """ Main """
    ticks = 10000
    sleep = .05
    world = gameoflife.random_world(width=20, height=20, fill_chance=.15)
    gameoflife.show_world(world)
    (seen_worlds, _, _) = gameoflife.is_unique(0, world)
    print('\n')
    for tick in range(0, ticks):
        time.sleep(sleep)
        world = gameoflife.next_tick(world, born=[3], survive=[2, 3])
        gameoflife.show_world(world)
        (seen_worlds, new, indices) = gameoflife.is_unique(tick, world, seen_worlds)
        if not new:
            print('World looping at tick ' + str(tick) + ', jumping to tick ' + str(indices) + '.')
            return
        print('\n')
    print("finished")


if __name__ == "__main__":
    main(sys.argv)
