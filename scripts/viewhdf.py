import h5view
import sys

with h5view.open(sys.argv[1]) as f:
        print(f)
