#!/usr/bin/env python

import os
import sys

user = os.environ['mapreduce_map_input_file'].split("/")[-1].split(".")[0]

for line in sys.stdin:
    line = line.strip()
    url = line.split()[3][1:-1]

    if '.ps' in url:
        print('%s\t%s' % (user, 1))
    print('%s\t%s' % (url, 1))
