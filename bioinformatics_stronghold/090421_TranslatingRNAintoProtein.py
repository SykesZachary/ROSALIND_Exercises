### Translating RNA into Protein
    ## http://rosalind.info/problems/prot/
### 09.04.2021

import os, shutil

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')
output = os.path.join(rosalind_sets, 'Output/')

codon_table = {'F': ['UUU', 'UUC'],
               'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
               'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
               'Y': ['UAU', 'UAC'], 'Stop': ['UAA', 'UAG', 'UGA'],
               'C': ['UGU', 'UGC'], 'W': ['UGG'],
               'P':['CCU', 'CCC', 'CCA', 'CCG'],
               'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'],
               'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
               'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'],
               'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'N': ['AAU', 'AAC'],
               'K': ['AAA', 'AAG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'],
               'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'],
               'E': ['GAA', 'GAG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG']}


def rna_translate(rna):

    prot = ''
    i = 0
    while i < len(rna):
        for k,v in codon_table.items():
            if rna[i:(i + 3)] in v:
                if k == 'Stop':
                    break
                else:
                    prot += k
        i += 3

    return list(prot)


def file_extract(in_path, out_path, in_file, out_file):

    os.chdir(in_path)

    prot_file_out = open(out_file, 'w')

    gen_string = ''
    with open(in_file, 'r') as f:
        for line in f:
            line = line.strip()
            gen_string += line

    f.close()
    for idx, aa in enumerate(rna_translate(gen_string)):
        prot_file_out.write(aa)
        if (idx + 1) / 60 in range(1, 101):
            prot_file_out.write('\n')

    shutil.move(f'{in_path}{out_file}', f'{out_path}{out_file}')


file_extract(datasets, output,
             'Dataset_9_TranslatingRNAintoProtein.txt',
             'Output_4_TranslatingRNAintoProtein.txt')
