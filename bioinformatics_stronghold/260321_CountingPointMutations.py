### Counting Point Mutations - Hamming Distance Calucator
    ## http://rosalind.info/problems/hamm/
### 26.03.2021

import os

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def id_point_mutations(path, file):

    os.chdir(path)

    strands = []
    mismatch = []
    hamming_dist = 0

    with open(file, 'r') as f:
        i = 0
        for line in f:
            line = line.strip()
            if i == 0:
                for base in line:
                    strands.append(['', base])
            elif i == 1:
                for idx, base in enumerate(line):
                    strands[idx] = [base, strands[idx][1], idx]
                    strands[idx] = tuple(strands[idx])

                for b1, b2, idx in strands:
                    if b1 != b2:
                        hamming_dist += 1
                        loci = idx + 1
                        mismatch.append((b1, b2, loci))
                    else:
                        continue

            i += 1
            if  i == 2:  # Reset the count
                i = 0

    f.close()

    print('The hamming distance of the two strands is:', hamming_dist)


id_point_mutations(datasets,
                   'Dataset_6_CountingPointMutations.txt')
