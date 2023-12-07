import numpy as np
from tensorflow import TensorSpec, data, int32

batch_size = 8

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
                # Only appends sequence data
                output.append(line.strip())
        file.close()

    return output

def conv_amino_to_vector(sequence):
    '''
    Converts peptide sequences to numerical vectors
    '''
    conversion_dict = {
        'X':0,
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

def vectorize(filepath):
    '''
    Used to convert a single file into vector format
    Useful for run.py --mode predict
    '''
    sequences = read(filepath)
    vectors = []
    for i in sequences:
        # zero-padding vectors of length 200
        padded = i.rjust(200, 'X')
        vectors.append(conv_amino_to_vector(padded))
    return vectors

class Dataset:
    def __init__(self, positive_files, negative_files, batch_size=32, training=False):
        # Constructor initializes dataset containing AMP and non-AMP data
        self.batch_size = batch_size # specifies how big to make each batch
        self.data_train = [] # list to store processed data

        # Processing AMP data
        for positive_file in positive_files:
            for i in positive_file:
                padded = i.rjust(200, 'X')
                self.data_train.append((conv_amino_to_vector(padded), 1))
        # Processing non-AMP data
        for negative_file in negative_files:
            for i in negative_file:
                padded = i.rjust(200, 'X')
                self.data_train.append((conv_amino_to_vector(padded), 0))
        self.indices = np.arange(len(self.data_train)) # indices used for shuffling

        self.training = training
        if self.training:
            np.random.shuffle(self.indices) # shuffle data during training
        
    def __len__(self):
        # number of batches in dataset
        return int(len(self.data_train)/self.batch_size)
    
    def __getitem__(self, index):
        # retrieves batch of data given an index
        start = index*self.batch_size
        Xs = []
        Ys = []

        # Loop for creating batch
        for i in self.indices[start:start+self.batch_size]:
            x,y = self.data_train[i]
            Xs.append(x)
            Ys.append(y)
        return np.array(Xs, dtype = np.int32), np.array(Ys, dtype = np.int32)
    
    def __call__(self):
        for i in range(self.__len__()):
            yield self.__getitem__(i)
            
            self.on_epoch_end()

    def on_epoch_end(self):
        # Shuffles indices at the end of each epoch if training
        if self.training:
            np.random.shuffle(self.indices)

def create_dataset(dataset_types):
    """
    Input: dataset type
    Output: Tensorflow Dataset
    Description: Convert training, evaluation, and test
    datasets to tensorflow datasets.
    """

    positive_files = []
    negative_files = []
    training = False
    if 'train' in dataset_types:
        positive_files.append(read('./data/raw/AMP.tr.fa'))
        negative_files.append(read('./data/raw/DECOY.tr.fa'))
        training = True
    elif 'test' in dataset_types:
        positive_files.append(read('./data/raw/AMP.te.fa'))
        negative_files.append(read('./data/raw/DECOY.te.fa'))
    elif 'evaluate' in dataset_types:
        positive_files.append(read('./data/raw/AMP.eval.fa'))
        negative_files.append(read('./data/raw/DECOY.eval.fa'))
    else:
        raise KeyError('Type must be "train", "evaluate" or "test"')

    dataset = data.Dataset.from_generator(
        Dataset(positive_files, negative_files, batch_size = batch_size, training=training),
        output_signature=(
            TensorSpec(shape=(batch_size, 200), dtype=int32),
            TensorSpec(shape=(batch_size), dtype=int32)
        )
    )

    return dataset
