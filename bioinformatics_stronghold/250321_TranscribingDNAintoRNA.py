### Transcribing DNA into RNA from a file of DNA
    ## http://rosalind.info/problems/rna/
### 25.03.2021

import os
import shutil

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')
rna_output = os.path.join(rosalind_sets, 'Output/')


def rna_transcriber(in_path, out_path, input_file, output_file):

    os.chdir(in_path)

    # Output file
    rna_file = open(output_file, 'w+')

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                rna_file.write(line + '\n')
            else:
                rna_file.write(line.replace('T', 'U') + '\n')

    rna_file.close()
    file.close()

    shutil.move(f'{in_path}{output_file}',f'{out_path}{output_file}')


rna_transcriber(datasets, rna_output, 'Homo_sapiens_AUTS2_201_sequence.fa',
                'H_sapiens_AUTS2_201_RNA_transcribe_speed_test.fa')
