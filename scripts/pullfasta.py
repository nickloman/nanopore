#!/usr/bin/python
import sys
from Bio import SeqIO

SeqIO.write((rec for rec in SeqIO.parse(open(sys.argv[1]), "fasta") if rec.id in sys.argv[2:]), sys.stdout, "fasta")

