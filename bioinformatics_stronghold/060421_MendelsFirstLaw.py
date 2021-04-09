### Mendel's First Law
    ## http://rosalind.info/problems/iprb/
### 07.04.2021

import os, re
from scipy.special import comb

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def mendel_inherit(path, file):

    os.chdir(path)

    pop = []

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            for num in re.findall(r'\d{2,3}', line):
                num = int(num)
                pop.append(num)


    f.close()

    k = pop[0]
    m = pop[1]
    n = pop[2]
    pop_total = sum(pop)
    print(pop)

    # All posible combinations of k,m,n which can be picked
    C_any = comb(pop_total, 2)

    # All combinations containing a dominant allele
    C_dom_k = comb(k, 2) + k*m + k*n
    C_dom_m = (comb(m, 2)*0.75) + ((m*n)*0.5)
    C_dom = C_dom_k + C_dom_m

    P_dom = C_dom/C_any
    print(P_dom)

mendel_inherit(datasets,
               'Dataset_8_MendelsFirstLaw.txt')


# NOTE: Admittedly I had to do a bit of Googling for this one.
    # I understood the genetics but I struggled to get it into code.
