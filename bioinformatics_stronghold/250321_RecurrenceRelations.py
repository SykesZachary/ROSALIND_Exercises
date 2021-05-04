### Recurrence Relations - Determining progeny in a sequence
    ## http://rosalind.info/problems/fib/
### 25.03.2021

import os
import re

rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def progeny_determination(path, file):

    # Determines the number of progeny after n months
    # with k pairs per month. Fibonacci sequence core

    os.chdir(path)

    exercise_data = []
    relation = {1: 1, 2: 1}

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            for num in re.findall('[0-9]+', line):
                num = int(num)
                exercise_data.append(num)

    f.close()

    n = exercise_data[0]
    k = exercise_data[1]

    i = 3
    while i < (n + 1):

        fn1 = relation.get((i - 1))
        fn2 = relation.get((i - 2))

        fn = fn1 + (k * fn2)
        relation[i] = fn

        i += 1

    print(relation)


progeny_determination(datasets, 'Dataset_4_RecurrenceRelations.txt')
