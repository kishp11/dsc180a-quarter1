# Create fake datasets of various sizes

# global variable to determine fake dataset length
import random
import numpy as np

def create_fake_datasets(sizes, vector_length = 150):
    vector_length = vector_length
    sizes = sizes
    data = np.array([])
    for i in sizes:
        for r in range(i):
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