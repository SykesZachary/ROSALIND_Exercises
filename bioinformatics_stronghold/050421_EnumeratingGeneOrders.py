### Enumerating Gene Orders
    ## http://rosalind.info/problems/perm/
### 05.04.2021

import os, re

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def enumerate_gene(path, file):

    os.chdir(path)

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            print(line)

    f.close()


enumerate_gene(datasets,
               'Dataset_7_EnumeratingGeneOrders.txt')
