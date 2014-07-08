from Bio import SeqIO
import sys

for rec in SeqIO.parse(open(sys.argv[1]), "fasta"):
	print len (rec), rec.description
