### Finding a Motif in DNA
    ## http://rosalind.info/problems/subs/
### 10.04.2021

import os

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def motif_identify(dna, substring):

    i = 0
    print(f'\n{substring} present in given strand at loci:')
    while i < (len(dna) - len(substring)):
        if dna[i:i + len(substring)] == substring:
            print(len(dna[:i+1]), end=' ')
        i += 1
    print('\n')


def file_extract(path, file):
    
    os.chdir(path)

    i = 2
    dna = ''
    substring = ''

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if i % 2 == 0:
                dna = line
            else:
                substring = line
            i += 1

    f.close()
    motif_identify(dna, substring)
    

file_extract(datasets,
             'Dataset_10_FindingAMotifinDNA.txt')

# NOTE: The file manipulation here only assumes one dna string and one motif
# from a two lined file
