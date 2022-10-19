#!/usr/bin/env python

import sys

current_town = None
current_town_max, current_town_min = 0, 0

for line in sys.stdin:

    line = line.strip()
    town, temp = line.split('\t', 1)
    temp = float(temp)

    if current_town == town:
        if temp < current_town_min: current_town_min = temp
        if temp > current_town_max: current_town_max = temp
    else:
        if current_town:
            print('%s\t%s' % (current_town, current_town_max))
            print('%s\t%s' % (current_town, current_town_min))
        current_town = town

if current_town == current_town:
    print('%s\t%s' % (current_town, current_town_max))
    print('%s\t%s' % (current_town, current_town_min))
