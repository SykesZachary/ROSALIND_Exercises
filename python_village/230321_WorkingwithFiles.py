### Working with Files
    ## http://rosalind.info/problems/ini5/
### 23.03.2021

import os

rosalind_path = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_path, 'Datasets/')


def file_modify(path, exercise, output_file):

    os.chdir(path)

    line_num = 1
    file_2 = open(output_file, 'w')

    with open(exercise, 'r') as file_1:
        for line in file_1:
            line = line.strip()
            if line_num % 2 == 0:
                file_2.write(line + '\n')
            line_num += 1

        file_2.close()
    file_1.close()

    with open(output_file, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)

    file.close()


file_modify(datasets, 'Datasets_5_WorkingwithFiles.txt',
            'Exercise_5_OutputFile.txt')
