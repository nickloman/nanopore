#!/usr/bin/python

import h5py
from Bio import SeqIO
from StringIO import StringIO
import sys
from collections import defaultdict

def get_hdf5_len(obj, key):
	try:
		return len(obj['key'][()])
	except Exception:
		return 0

for fn in sys.argv[1:]:
	result = []

	try:
		hdf = h5py.File(fn, 'r')
	except Exception, e:
		print >>sys.stderr, "Error opening %s" % (fn,)
		continue

	if 'UniqueGlobalKey' in hdf:
		k = hdf['UniqueGlobalKey']
	else:
		k = hdf['Key']

	result.append(fn)

	result.append(k['tracking_id'].attrs['exp_start_time'])
	result.append(k['read_id'].attrs['channel_number'])
	result.append(k['read_id'].attrs['read_number'])

	result.append(get_hdf5_len(hdf, '/Analyses/Basecall_2D_000/BaseCalled_template/Events'))
	result.append(get_hdf5_len(hdf, '/Analyses/Basecall_2D_000/BaseCalled_complement/Events'))
	result.append(get_hdf5_len(hdf, '/Analyses/Basecall_2D_000/BaseCalled_template/Fastq'))
	result.append(get_hdf5_len(hdf, '/Analyses/Basecall_2D_000/BaseCalled_complement/Fastq'))
	result.append(get_hdf5_len(hdf, '/Analyses/Basecall_2D_000/BaseCalled_2D/Fastq'))

	print "\t".join([str(x) for x in result])

	hdf.close()


