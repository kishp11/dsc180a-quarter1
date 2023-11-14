import os
import csv


def read(filepath:str, label=None) -> list:
    '''
    Reads dataset in .fa format
    returns a list of strings
    '''
    # Open the file in read-only mode ('r')
    output = []
    with open(filepath, 'r') as file:
        for line in file:
            if not line.startswith(">"):
                # This line contains sequence data
                output.append(line.strip())
        file.close()

    return output

def pad(sequence, char='X', length=200):
    """pads start of a string with a character up to given length"""
    pad_needed = length-len(sequence)
    return char*pad_needed + sequence

def conv_amino_to_vector(sequence):
    conversion_dict = {'X':0,
                       'A':1,
                       'C':2,
                       'D':3,
                       'E':4,
                       'F':5,
                       'G':6,
                       'H':7,
                       'I':8,
                       'K':9,
                       'L':10,
                       'M':11,
                       'N':12,
                       'P':13,
                       'Q':14,
                       'R':15,
                       'S':16,
                       'T':17,
                       'V':18,
                       'W':19,
                       'Y':20
    }

    return [conversion_dict[c] for c in sequence]

def writefile(features, outfile):
    with open(outfile, "w") as fp:
        csvwriter = csv.writer(fp)
        csvwriter.writerows(features)

def build_features(directory='data/raw/', output_directory = 'data/processed/'):
    """Creates labeled train/test/split sets and saves in data/processed"""
    for filename in os.listdir(directory):
        if filename == '.gitkeep':
            # ignore this file
            continue

        info = filename.split('.')
        if info[0] == 'AMP':
            label = 1
        else: 
            label = 0
        
        file = os.path.join(directory, filename)
        sequences = read(file)

        features = [[conv_amino_to_vector(pad(s)), label] for s in sequences]

        # save as AMP/DECOY.tr/test/eval.csv
        outfilepath = os.path.join(output_directory, info[0]+'.'+info[1]+'.'+'csv')
        writefile(features, outfilepath)
    
    print('Done extracting features')

if __name__ == "__main__":
    build_features()