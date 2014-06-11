import h5py
from Bio import SeqIO
from StringIO import StringIO
import sys
from collections import defaultdict

keys = {'template' : '/Analyses/Basecall_2D_000/BaseCalled_template/Fastq',
        'complement' : '/Analyses/Basecall_2D_000/BaseCalled_complement/Fastq',
        'twodirections' : '/Analyses/Basecall_2D_000/BaseCalled_2D/Fastq'}

stats = defaultdict(int)

for fn in sys.argv[1:]:
	print >>sys.stderr, "Trying %s" % (fn)
	stats['files'] += 1
	try:
		hdf = h5py.File(fn, 'r')
	except Exception, e:
		print >>sys.stderr, "Error opening %s" % (fn,)
		continue

	for id, key in keys.iteritems():
		try:
			fq = hdf[key][()]
			rec = SeqIO.read(StringIO(fq), "fastq")
			rec.id += "_" + id
			rec.description = fn
			SeqIO.write([rec], sys.stdout, "fasta")

			stats[key] += 1
		except Exception, e:
			print >>sys.stderr, e
	hdf.close()

for k in stats.keys():
	print >>sys.stderr, "%s\t%s" % (k, stats[k])

