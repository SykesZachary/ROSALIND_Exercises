### Strings and Lists
    ## http://rosalind.info/problems/ini3/
### 23.03.2021

import os
import re

rosalind_path = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_path, 'Datasets/')


def string_splitter(path, exercise):

    os.chdir(path)

    string = ''
    ind = []

    with open(exercise, 'r') as file:
        for line in file:
            if re.match('[A-Za-z]', line):
                string = line
            if re.match('[0-9]+ ', line):
                line = line.strip()
                for num in re.findall('[0-9]{2,3}', line):
                    num = int(num)
                    ind.append(num)
    file.close()

    print(string[ind[0]:(ind[1] + 1)], string[ind[2]:(ind[3] + 1)])


string_splitter(datasets, 'Dataset_3_StringsandLists.txt')
