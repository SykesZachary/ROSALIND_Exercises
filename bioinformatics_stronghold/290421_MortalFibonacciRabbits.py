### Mortal Fibonacci Rabbits
    ## http://rosalind.info/problems/fibd/
### 30.04.2021

import os
import re

# PATH Define
rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def mortal_progeny_determination(n, m):

    total_prog = {1: 1, 2: 1}  # Total progeny check

    i = 3
    while i < (n + 1):

        # Setting up the two months prior
        fn1 = total_prog.get(i - 1)
        fn2 = total_prog.get(i - 2)

        if i < m + 1:
            fn = fn1 + fn2
            total_prog[i] = fn
        elif i == m + 1 or i == m + 2:
            fn = (fn1 + fn2) - 1
            total_prog[i] = fn
        else:
            fn = (fn1 + fn2) - total_prog[i - (m + 1)]
            total_prog[i] = fn

        i += 1

    for k, v in total_prog.items():
        print(k, v)


def file_extract(path, file):

    os.chdir(path)

    data = []

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            for num in re.findall(r'[0-9]+', line):
                num = int(num)
                data.append(num)

    f.close()

    mortal_progeny_determination(data[0], data[1])


file_extract(datasets,
             'Dataset_12_MortalFibonacciRabbits.txt')
