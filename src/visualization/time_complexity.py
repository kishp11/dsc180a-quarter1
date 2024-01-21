# Create fake datasets of various sizes

# global variable to determine fake dataset length
import random
import numpy as np

def create_fake_datasets(sizes, vector_length=150):
    vector_length = vector_length
    sizes = sizes
    all_datasets = np.array([])
    for i in sizes:
        data = np.array([])
        for r in range(i):
            sequence = np.zeros(200-vector_length)
            rng = np.array([])
            for j in range(vector_length):
                rng = np.append(rng, random.randint(1,20))
            sequence = np.append(rng, sequence)
            print(sequence)
            data = np.append(data, sequence)
        all_datasets = np.append(all_datasets, data)
    return all_datasets

# Run each fake dataset through model
    # output time taken in milliseconds

# plot time taken
    # x = dataset size
    # y = time taken