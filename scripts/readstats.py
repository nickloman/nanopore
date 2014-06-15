#!/usr/bin/python

import h5py
from Bio import SeqIO
from StringIO import StringIO
import sys
from collections import defaultdict

for fn in sys.argv[1:]:
	try:
		hdf = h5py.File(fn, 'r')
	except Exception, e:
		print >>sys.stderr, "Error opening %s" % (fn,)
		continue

	if 'UniqueGlobalKey' in hdf:
		k = hdf['UniqueGlobalKey']
	else:
		k = hdf['Key']

	start_time = k['tracking_id'].attrs['exp_start_time']
	channel_number = k['read_id'].attrs['channel_number']
	read_number = k['read_id'].attrs['read_number']

	try:
		template_len = len(hdf['/Analyses/Basecall_2D_000/BaseCalled_template/Events'][()])
	except Exception:
		template_len = 0

	try:
		complement_len = len(hdf['/Analyses/Basecall_2D_000/BaseCalled_complement/Events'][()])
	except Exception:
		complement_len = 0

	print "%s\t%s\t%s\t%s\t%s" % (start_time, channel_number, read_number, template_len, complement_len)

	hdf.close()


