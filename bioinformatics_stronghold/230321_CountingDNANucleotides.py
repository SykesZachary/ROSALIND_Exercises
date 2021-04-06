### Counting DNA Nucleotodes -- Going to use a dictionary
    ## http://rosalind.info/problems/dna/
### 23.03.2021

import os
import re

rosalind_path = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_path, 'Datasets/')


def nucleotide_counter(path, file):

    os.chdir(path)

    nuc = {}

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            for word in re.findall('(A|G|C|T)', line):
                if word not in nuc.keys():
                    nuc[word] = 0
                if word in nuc.keys():
                    nuc[word] += 1

    print('A:', nuc['A'],
          'C:', nuc['C'],
          'G:', nuc['G'],
          'T:', nuc['T'])

    f.close()


nucleotide_counter(datasets, 'Dataset_1_CountingDNANucleotides.txt')
