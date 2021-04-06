### Dictionaries - Counts the instances of each word in a file
    ## http://rosalind.info/problems/ini6/
### 23.03.2021

import os
import re

rosalind_path = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_path, 'Datasets/')


def word_counter(path, exercise):

    os.chdir(path)

    word_totals = {}

    with open(exercise, 'r') as file:
        for line in file:
            line = line.strip()
            for word in re.findall('[A-Za-z]+', line):
                if word not in word_totals.keys():
                    word_totals[word] = 0
                if word in word_totals.keys():
                    word_totals[word] += 1

        for word in word_totals.keys():
            print(word, word_totals[word])

    file.close()


word_counter(datasets, 'Dataset_6_Dictionaries.txt')

# NOTE: This could be modified to report nucleotide density
