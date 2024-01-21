# Create fake datasets of various sizes

# global variable to determine fake dataset length
import random
import numpy as np

def create_fake_datasets(sizes, vector_length=150):
    vector_length = vector_length
    sizes = sizes
    all_datasets = np.array([])
    for size in sizes:
        data = create_single_dataset(size, vector_length)
        all_datasets = np.append(all_datasets, data)
    return all_datasets

def create_single_dataset(dataset_size, vector_length):
    data = np.array([])
    
    for r in range(dataset_size):
        sequence = np.zeros(200-vector_length)
        rng = np.array([])
        for j in range(vector_length):
            rng = np.append(rng, random.randint(1,20))
        sequence = np.append(rng, sequence)
        data = np.append(data, sequence)
    return data

# Run each fake dataset through model
    # output time taken in milliseconds

# plot time taken
    # x = dataset size
    # y = time taken