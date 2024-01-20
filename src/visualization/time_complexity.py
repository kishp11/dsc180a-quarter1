# Create fake datasets of various sizes

# global variable to determine fake dataset length
import random
import numpy

def create_fake_datasets(vector_length, dataset_size):
    vector_length = vector_length
    dataset_size = dataset_size
    data = np.array([])
    for i in dataset_size:
        sequence = np.array([])
        padding = 200 - vector_length
        for x in padding:
            sequence.append(0)
        for j in vector_length:
            sequence.append(random.randint(1,20))
        data.append(sequence)
    return data

# Run each fake dataset through model
    # output time taken in milliseconds

# plot time taken
    # x = dataset size
    # y = time taken