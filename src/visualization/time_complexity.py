# Create fake datasets of various sizes

# global variable to determine fake dataset length
import random
import numpy as np

MAX_ARRAY_SIZE = 200

def create_fake_datasets(sizes, vector_length=150):
    vector_length = vector_length
    sizes = sizes
    all_datasets = np.array([])
    for size in sizes:
        data = create_single_dataset(size, vector_length)
        all_datasets = np.append(all_datasets, data, axis = 0)
    return all_datasets

def create_single_dataset(dataset_size, vector_length):
    data = np.array([])
    for r in range(dataset_size):
        line = np.random.randint(1, 21, size=vector_length)
    
        num_padding = MAX_ARRAY_SIZE - dataset_size
        zeroes = np.zeros(num_padding)
        
        sequence = np.append(line, zeroes)
        data = np.append(data, sequence)
    return data

# Run each fake dataset through model
    # output time taken in milliseconds

# plot time taken
    # x = dataset size
    # y = time taken