#!/usr/bin/env python

import os
import sys

# Get winetype
file_name=os.environ['mapreduce_map_input_file']
s1=file_name.split('/')
file_name=s1[-1]
file_name=file_name[12:len(file_name)-4]

NOT_VALID_LINE = '"fixed acidity";"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"'
attribute_names = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']

for line in sys.stdin:
  # remove leading and trailing whitespace
  line = line.strip()
  # It cannot count the first line of the document. It is not valid.
  if line == NOT_VALID_LINE:
    continue
  # split the line into values
  winesubtype = line.split(';')

  nAttr = 0
  for attr in winesubtype:
    print('%s\t%s' % (file_name + '-' + attribute_names[nAttr], attr))
    nAttr += 1