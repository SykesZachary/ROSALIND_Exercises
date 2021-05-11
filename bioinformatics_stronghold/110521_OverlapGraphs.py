### Overlap Graph Construction for given DNA strings
    ## http://rosalind.info/problems/grph/
### 11.05.2021

import os

# PATHs set
proj_path = os.path.abspath(os.getcwd())
datasets = os.path.join(proj_path, 'Datasets/')


# Overlap graph generator
def overlap_gen(seqs, k=3):

    directed_edges = list()  # Opening list to store the overlaps

    i = 0
    while i < len(seqs):

        s = seqs[i][1][-k:]
        for tup in seqs:
            t = tup[1][:k]
            if seqs[i][1] == tup[1]:
                continue
            elif s == t:
                if (seqs[i][0], tup[1]) in directed_edges:
                    continue
                elif (tup[1], seqs[i][1]) in directed_edges:
                    continue
                else:
                    directed_edges.append((seqs[i][0], tup[0]))
                    print(seqs[i][0], tup[0])

        i += 1


# Extracting data from file
def data_extract(path, file):

    os.chdir(path)  # CWD changed to load file with data

    with open(file, 'r') as f:

        data = list()  # Open list to store data from file
        string = ''  # Opens a variable to store sequence

        for line in f:
            line = line.strip()
            # Handles line containing sequence id
            if line.startswith('>'):
                seq_id = line.replace('>', '')
                if string:
                    data.append((seq_id, string))
                    string = ''
            else:
                string += line

    f.close()

    return data


# Storing extracted data to pass into overlapping graph generator
sequences = data_extract(
    datasets,
    'Dataset_13_OverlapGraph.txt',
)

# Calling overlap graph method
overlap_gen(sequences, k=3)
