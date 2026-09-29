from Bio import SeqIO

def read_fasta(filename): #file name is a place holder
  sequences = []

for record in SeqIO.parse(filename, "fasta"):
  sequences.append(record)

