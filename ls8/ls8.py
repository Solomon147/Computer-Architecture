#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

file = open(sys.argv[1], "r")

program = []

for line in file:
    line = line.split(' ')[0]
    line = line.split('#')[0]

cpu = CPU()

if len(sys.argv) != 2:
    print("ERROR: must have file name")
    sys.exit(1)

cpu.load(sys.argv[1])
cpu.run()
