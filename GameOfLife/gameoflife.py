""" Game of life, basic implementation.

author: Patrick Hanckmann
e-mail: patrick@hanckmann.com
"""

import numpy
import time
from random import uniform


class GameOfLife(object):
    """ Basic game-of-world implementation """

    def __init__(self, world_width=10, world_height=10, fill_chance=.15):
        """ Init """
        self.world_width = world_width
        self.world_height = world_height
        self.world = numpy.zeros((world_width, world_height))
        # Set start world (at random)
        for wi in range(0, world_width):
            for hi in range(0, world_height):
                rvalue = uniform(0.0, 1.0)
                if rvalue <= fill_chance:
                    self.world[wi, hi] = 1

    def run(self, steps=100, wait_time=1.0):
        """ Start time """
        next_world = self.world
        self.show_world(next_world)
        for _ in range(0, steps):
            time.sleep(wait_time)
            next_world = self.next_tick(next_world)
            self.show_world(next_world)
        print("finished")

    def next_tick(self, world):
        """ implements the gol rules: B3,S23 """
        next_world = numpy.zeros((self.world_width, self.world_height))
        for wi in range(0, self.world_width):
            for hi in range(0, self.world_height):
                wi_plus = wi + 1
                hi_plus = hi + 1
                if wi == self.world_width - 1:
                    wi_plus = -1
                if hi == self.world_height - 1:
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
                    # born
                    if neighbours == 3:
                        next_world[wi, hi] = 1
                else:
                    # survive
                    if neighbours == 2 or neighbours == 3:
                        next_world[wi, hi] = 1
                # print('c=' + str(world[wi, hi]) + '\tn=' + str(neighbours) + '\tt=' + str(next_world[wi, hi]))
        return next_world

    def show_world(self, world):
        """ Print the world to screen """
        for hi in range(0, self.world_height):
            line = ''
            for wi in range(0, self.world_width):
                if world[wi, hi]:
                    line += 'X'
                else:
                    line += '-'
                line += ''
            print(line)
        print('\n\n\n')
