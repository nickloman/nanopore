import h5py
from Bio import SeqIO
from StringIO import StringIO
import sys
from collections import defaultdict

keys = ['mean', 'start', 'stdv', 'length', 'model_state', 'model_level', 'move', 'p_model_state', 'mp_model_state', 'p_mp_model_state', 'p_A', 'p_C', 'p_G', 'p_T', 'raw_index']
print "\t".join(keys)

for fn in sys.argv[1:]:
	print >>sys.stderr, "Trying %s" % (fn)
	try:
		hdf = h5py.File(fn, 'r')
	except Exception, e:
		print >>sys.stderr, "Error opening %s" % (fn,)
		continue

	for event in hdf['/Analyses/Basecall_2D_000/BaseCalled_complement/Events'][()]:
		print "\t".join([str(e) for e in event])

	hdf.close()


