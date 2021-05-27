### Calculating Expected Offspring
    ## http://rosalind.info/problems/iev/
### 27.05.2021

import os

# PATHs set
rosalind_sets = os.path.abspath(os.getcwd())
datasets = os.path.join(rosalind_sets, 'Datasets/')


def expected_offspring(genotypes):
    # Frequency of dominance in offspring per genotype (gt)
    freq = {
        0: 1.00,
        1: 1.00,
        2: 1.00,
        3: 0.75,
        4: 0.50,
        5: 0.00
    }

    # Final result of expected dominant offspring
    dominant_offspring = 0

    # Updating genotypes to contain tuples of couples and frequency
    for i, v in enumerate(genotypes):
        genotypes[i] = (v, freq[i])

    # Looks at the number of couples with the current gt
    # Multiplies each couple by 2 and get the frequency the offspring has a dominant allele
    # Adds to the total
    for couple, frequency in genotypes:
        dom_expect = 0  # Expected dominant offspring for couple with current gt
        for num in range(0, couple):
            dom_expect += 2 * frequency  # Each couple has two offspring, times frequency

        # Expected dominance per couple with current gt added to total
        dominant_offspring += dom_expect

    print(dominant_offspring)


def file_extract(path, file):

    os.chdir(path)

    data = ''

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            data = [int(i) for i in line.split(' ')]

        f.close()

    return data


gt = file_extract(
    datasets,
    'Dataset_14_CalculatingExpectedOffspring.txt',
)
expected_offspring(gt)

