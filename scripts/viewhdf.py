#!/usr/bin/python

import h5view
import sys

for fn in sys.argv[1:]:
	with h5view.open(fn) as f:
        	print(f)
