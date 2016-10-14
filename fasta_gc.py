# fasta_gc.py
#
# Reads a fasta file and prints out the GC content percentage of each sequence
# in the file
#
# Usage: python fasta_gc.py sequences.fa
#

import sys

def read_fasta_dict(filename):
    """
    Reads sequences from a fasta file, and returns a dictionary that maps the 
    sequence description (key) to the sequence (value) 
    
    For example:
    
    >seq1
    AACCGG
    >seq2
    CCTTTG
    
    would result in {'seq1':'AACCGG','seq2':'CCTTG'}
    
    """
    sequences = {}
    f = open(filename)
    for line in f:
        line = line.strip()
        if '>' in line:
            sequence_name = line # Need to keep track of the name since "line" will change next time
            sequences[sequence_name] = ''
        else:
            # Append to the last sequence
            sequences[sequence_name] = sequences[sequence_name] + line
    f.close()
    return sequences

def gc_content_percent(sequence):
    """
    Calculates the GC-content percentage of the input sequence
    Returns the percentage as an integer out of 100
    """
    gc = sequence.count('G') + sequence.count('C')
    atcg = len(sequence)
    percent_gc = (gc * 100) / atcg
    return percent_gc

# Make sure we have a file name
if not len(sys.argv) == 2:
    print "Usage: python", sys.argv[0], "<sequences.fa>"
    exit(1)

filename = sys.argv[1]

# Read the sequences into a dictionary
sequences = read_fasta_dict(filename)

# Loop over the keys (sequence names) in the dictionary
for name in sequences:
    sequence = sequences[name]
    gc = gc_content_percent(sequence)
    print gc, name
    