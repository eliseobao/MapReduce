#!/usr/bin/env python

import sys

results = {}

for line in sys.stdin:
    line = line.strip()
    wine, attribute, value = line.split('\t')
    value = float(value)

    if wine in results:
        if attribute in results[wine]:
            results[wine][attribute].append(value)
        else:
            results[wine][attribute] = [value]
    else:
        results[wine] = {}
        results[wine][attribute] = [value]

for wine in results:
    for attribute in results[wine]:
        mean_value = sum(results[wine][attribute]) / float(len(results[wine][attribute]))
        print('%s\t%s\t%.4f' % (wine, attribute, mean_value))
