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
    world = gameoflife.random_world(width=100, height=50, fill_chance=.05)
    gameoflife.show_world(world)
    print('\n')
    # seen_worlds = dict()
    # world.flags.writeable = False
    # seen_worlds[hash(world.data)] = [-1]
    for tick in range(0, ticks):
        time.sleep(sleep)
        world = gameoflife.next_tick(world, born=[3], survive=[2, 3])
        gameoflife.show_world(world)
        print('\n')
        # world.flags.writeable = False
        # hash_id = hash(world.data)
        # seen_ticks = [tick]
        # if hash_id in seen_worlds:
        #     seen_ticks += seen_worlds[hash_id]
        #     print('Tick ' + str(tick) + ' loops back to tick ' + str(seen_ticks))
        # seen_worlds[hash(world.data)] = seen_ticks
    print("finished")


if __name__ == "__main__":
    main(sys.argv)
