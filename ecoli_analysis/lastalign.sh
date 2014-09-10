#!/bin/bash -x

ref=$1
fasta=$2

export PATH=$PATH:/home/ubuntu/ecoli_nanopore/last-475/src:/home/ubuntu/ecoli_nanopore/last-475/scripts:/home/ubuntu/ecoli_nanopore/samtools-1.0

lastdb "$ref".lastindex "$ref".fna
lastal -a1 -b1 -q2 "$ref".lastindex $fasta > "$fasta".last.txt
maf-sort.sh "$fasta".last.txt > "$fasta".last.sorted.txt
maf-convert.py sam -d "$fasta".last.sorted.txt > "$fasta".last.sam
samtools view -bS "$fasta".last.sam | samtools sort - "$fasta".last.sorted
samtools index "$fasta".last.sorted.bam
