### Conditions and Loops
    ## http://rosalind.info/problems/ini4/
### 23.03.2021

import os
import re

rosalind_path = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_path, 'Datasets/')


def conditional_loops(path, exercise):

    os.chdir(path)

    file_extract = []
    odds = []

    with open(exercise, 'r') as file:
        for line in file:
            line = line.strip()
            for num in re.findall('[0-9]+', line):
                num = int(num)
                file_extract.append(num)
        a = file_extract[0]
        b = file_extract[1]

        for i in range(a, b):
            if i % 2 != 0:
                odds.append(i)

        if b % 2 != 0:  # range(0, n) n not included when looped
            odds.append(b)

    print(sum(odds))
    file.close()


conditional_loops(datasets, 'Datasets_4_ConditionalandLoops.txt')
