### Complementing a Strand of DNA - Returns a file of the reverse complement
    ## http://rosalind.info/problems/revc/
### 25.03.2021

import os
import shutil

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')
complement_output = os.path.join(rosalind_sets, 'Output/')


def get_dna_complement(in_path, out_path, input_file, output_file):

    os.chdir(in_path)

    comp_file = open(output_file, 'w+')
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                comp_file.write(line + '\n')
            else:
                print(line)
                bases = list(line)
                bases = reversed([complement.get(base, base) for base in bases])
                bases = ''.join(bases)
                comp_file.write(bases + '\n')

    comp_file.close()
    file.close()

    shutil.move(f'{in_path}{output_file}', f'{out_path}{output_file}')


get_dna_complement(datasets, complement_output,
                   'Homo_sapiens_AUTS2_201_sequence.fa',
                   'H_sapiens_AUTS2_201_CDNA_speed_test.fa')
