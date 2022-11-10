#!/usr/bin/env python

import os
import sys

filename = os.environ['mapreduce_map_input_file'].split("/")[-1]
wine = filename[filename.find('-') + 1: filename.find('.')]

attributes = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide",
    "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"
]

for line in sys.stdin:
    line = line.strip()

    if not line.startswith('"fixed acidity"'):
        line_attributes = line.split(';')

        for i, value in enumerate(line_attributes):
            print('%s\t%s\t%s' % (wine, attributes[i], value))
