#!/usr/bin/env python
import os
import sys

for line in sys.stdin:

    line = line.strip()
    town = os.environ['mapreduce_map_input_file'].split("_")[2]
    t_daily_max, t_daily_min = float(line.split()[5]), float(line.split()[6])

    if t_daily_max > 27.:
        print('%s\t%s' % (town, t_daily_max))
    if -99. < t_daily_min < -.1:
        print('%s\t%s' % (town, t_daily_min))
