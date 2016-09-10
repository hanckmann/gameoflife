#!/usr/bin/python
# -*- coding: utf-8 -*-

""" GOF Main """

import sys
from GameOfLife import gameoflife


def main(argv):
    """ Main """
    gof = gameoflife.GameOfLife()
    gof.run()

if __name__ == "__main__":
    main(sys.argv)
