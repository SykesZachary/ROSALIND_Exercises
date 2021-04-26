### Consensus and Profiling Rosalind exercise
    ## http://rosalind.info/problems/cons/
### 23.04.2021


import numpy as np
import os

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def common_ans_identify(dna):

    # Assigning consensus counts per loci to nucleotide marker
    consensus_dict = {'A': [], 'C': [], 'G': [], 'T': []}

    # Building matrix
    dna_mat = []
    for seg in dna:
        base_in_seg = []
        for base in seg:
            base_in_seg.append(base)
        dna_mat.append(base_in_seg)

    dna_mat = np.array(dna_mat)

    # Building the consensus matrix and determining the common ancestor strand
    count = 0
    col = 0
    consensus_str = ''
    while count < len(dna[0]):
        # Checking nucleotide counts per loci
        a, c, g, t = 0, 0, 0, 0

        for base in dna_mat[:, col]:

            if base == 'A':
                a += 1
            elif base == 'C':
                c += 1
            elif base == 'G':
                g += 1
            elif base == 'T':
                t += 1
            else:
                print('Unexpected character in DNA string')
                continue

        # Offloading per column
        consensus_dict['A'].append(a)
        consensus_dict['C'].append(c)
        consensus_dict['G'].append(g)
        consensus_dict['T'].append(t)

        if max((a, c, g, t)) == a:
            consensus_str += 'A'
        elif max((a, c, g, t)) == c:
            consensus_str += 'C'
        elif max((a, c, t, g)) == g:
            consensus_str += 'G'
        elif max((a, c, g, t)) == t:
            consensus_str += 'T'

        col += 1
        count += 1

    # Outputting Results
    print(consensus_str)
    for k, v in consensus_dict.items():
        print(f'{k}:', end=' ')
        for base in v:
            print(f'{base}', end=' ')
        print()


def file_extract(path, file):

    os.chdir(path)

    dna_string = ''
    dna_strings = []

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>') and not dna_string:
                continue
            elif line.startswith('>') and dna_string:
                dna_strings.append(dna_string)
                dna_string = ''
            else:
                dna_string += line

        dna_strings.append(dna_string)

    f.close()
    common_ans_identify(dna_strings)


file_extract(datasets,
             'Dataset_11_ConsensusAndProfile.txt')
