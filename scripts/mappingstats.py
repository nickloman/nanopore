#!/usr/bin/python

import pysam
import sys

samfile = pysam.Samfile(sys.argv[1], "rb")

fields = ['Name', 'QueryLen', 'AlignLen', 'NumMismatches']
print "\t".join(fields)

for read in samfile:
	t = dict(read.tags)

	results = []
	results.append(read.qname.ljust(25))
	results.append(t['XQ'])
	results.append(t['XL'])
	results.append(t['NM'])

	print "\t".join([str(r) for r in results])


