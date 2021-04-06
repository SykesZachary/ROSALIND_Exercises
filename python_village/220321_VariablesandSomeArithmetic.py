### Variables and Some Arithmetic
    ## http://rosalind.info/problems/ini2/
### 22.03.2021

import os
import re

rosalind_path = '/home/sykes/PycharmProjects/RosalindSets/'
datasets = 'Datasets/'

os.chdir(f'{rosalind_path}{datasets}')

arithmetic_values = ''

with open('Dataset_2_VariableandSomeArithmetic.txt', 'r') as file:
    for line in file:
        arithmetic_values = re.findall('[0-9]+', line)
        print(line)
        for i in range(0, len(arithmetic_values)):
            arithmetic_values[i] = int(arithmetic_values[i])
    file.close()

hypotenuse = ((arithmetic_values[0] ** 2) + (arithmetic_values[1] ** 2))
print(hypotenuse)
