### Enumerating Gene Orders - Permutations
    ## http://rosalind.info/problems/perm/
### 05.04.2021

import os, shutil
from itertools import permutations

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')
output = os.path.join(rosalind_sets, 'Output/')

def enumerate_gene(in_path, out_path, in_file, out_file):

    os.chdir(in_path)

    permutation_file = open(out_file, 'w+')
    n = None

    with open(in_file, 'r') as f:
        for line in f:
            line = line.strip()
            n = int(line)

    f.close()

    # Permutation calculations
    fact = 1


    for num in range(1, (n + 1)):
        fact *= num

    perms = list(permutations(range(1, (n + 1))))

    print(fact)
    for tup in perms:
        print((str(tup)[1:-1]).replace(', ', ' '))
        permutation_file.write(str(tup)[1:-1].replace(', ', ' ') + '\n')

    shutil.move(f'{in_path}{out_file}', f'{out_path}{out_file}')

enumerate_gene(datasets, output,
               'Dataset_7_EnumeratingGeneOrders.txt',
               'Output_3_EnumeratingGeneOrders.txt')
