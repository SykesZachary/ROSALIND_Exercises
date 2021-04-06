### Computing GC Content
    ## http://rosalind.info/problems/gc/
### 26.03.2021

import os
import re

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def gc_calc(path, file, max=False):

    os.chdir(path)

    dna_seqs = {}

    string_tag = None
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                string_tag = line
                dna_seqs[string_tag] = ''
            else:
                dna_seqs[string_tag] = [line.replace('\n', ''),
                                        dna_seqs[string_tag]]

            dna_seqs[string_tag] = ''.join(dna_seqs[string_tag])

    f.close()

    if max == True:  ## Change to True
        max_perc_gc = [0, '']

        for k, v in dna_seqs.items():
            gc_content = len(re.findall('(G|C)', v))
            perc_gc_content = (gc_content / len(v)) * 100
            if perc_gc_content > max_perc_gc[0]:
                 max_perc_gc[0] = perc_gc_content
                 max_perc_gc[1] = k
            dna_seqs[k] = [v, perc_gc_content]

        print(max_perc_gc[1])
        print(max_perc_gc[0])

    elif max == False:
        for k, v in dna_seqs.items():
            gc_content = len(re.findall('(G|C)', v))
            perc_gc_content = (gc_content / len(v)) * 100
            dna_seqs[k] = [v, perc_gc_content]
            print(k)
            print(dna_seqs[k][1])

gc_calc(datasets, 'Homo_sapiens_AUTS2_201_sequence.fa', max=True)
