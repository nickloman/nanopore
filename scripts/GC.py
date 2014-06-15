#!/usr/bin/python
import sys

from Bio import SeqIO
from Bio.SeqUtils import GC

for rec in SeqIO.parse(open(sys.argv[1]), "fasta"):
	print GC(rec.seq)

