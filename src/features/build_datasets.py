import numpy as np
import tensorflow as tf # TODO: import only necessary classes

batch_size = 12

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

def conv_amino_to_vector(sequence):
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

class Dataset:
    def __init__(self, positive_file, negative_file, batch_size=32, training=False):
        self.batch_size = batch_size # specifies how big to make batch
        self.data_train = []

        for i in positive_file:
            padded = i.rjust(200, 'X')
            self.data_train.append((conv_amino_to_vector(padded), 1))
        for i in negative_file:
            padded = i.rjust(200, 'X')
            self.data_train.append((conv_amino_to_vector(padded), 0))
        self.indices = np.arange(len(self.data_train))

        if training:
            np.random.shuffle(self.indices)
        
    def __len__(self):
        return int(len(self.data_train)/self.batch_size)
    
    def __getitem__(self, index):
        start = index*self.batch_size
        Xs = []
        Ys = []
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
        np.random.shuffle(self.indices)

def create_dataset(positive_file, negative_file):
    """
    Input: Open files of positive and negatively labeled data
    Output: Tensorflow Dataset
    """
    dataset = tf.data.Dataset.from_generator(
        Dataset(positive_file, negative_file, batch_size = batch_size),
        output_signature=(
            tf.TensorSpec(shape=(batch_size, 200), dtype=tf.int32),
            tf.TensorSpec(shape=(batch_size), dtype=tf.int32)
        )
    )

    return dataset