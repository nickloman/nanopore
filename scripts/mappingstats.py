#!/usr/bin/python

import pysam
import sys
import re

samfile = pysam.Samfile(sys.argv[1], "rb")

fields = ['Name', 'Direction', 'QueryLen', 'AlignLen', 'NumMismatches']
print "\t".join(fields)

for read in samfile:
	t = dict(read.tags)

	results = []
	results.append(read.qname)
	direction = read.qname.split("_")[-1]
	results.append(direction)

	# BLASR mode
	if 'XQ' in t and 'XL' in t:
		results.append(t['XQ'])
		results.append(t['XL'])
	else:
		results.append(read.qlen)
		results.append(read.alen)
	results.append(t['NM'])

	print "\t".join([str(r) for r in results])


