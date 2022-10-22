#!/usr/bin/env python

import sys

current_item = None
current_count = 0
item = None

for line in sys.stdin:

    line = line.strip()
    item, count = line.split('\t', 1)
    count = int(count)

    if current_item == item:
        current_count += count
    else:
        if current_item:
            print('%s\t%s' % (current_item, current_count))

        current_count, current_item = count, item

if current_item == item:
    print('%s\t%s' % (current_item, current_count))
