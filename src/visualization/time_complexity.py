# Create fake datasets of various sizes

# global variable to determine fake dataset length
import random
import json

# import numpy as np
import time
import numpy as np
import matplotlib.pyplot as plt
#from train_model import train_model

MAX_ARRAY_SIZE = 200

def create_fake_datasets(sizes, vector_length=150):
    all_datasets = []
    for size in sizes:
        data = create_single_dataset(size, vector_length)
        all_datasets.append(data)
    return all_datasets

def create_single_dataset(dataset_size, vector_length):
    data = []
    for l in range(dataset_size):
        line = np.random.randint(1, 21, size=vector_length)
    
        num_padding = MAX_ARRAY_SIZE - vector_length
        zeroes = np.zeros(num_padding)
        
        sequence = np.append(line, zeroes)
        data.append(sequence.tolist())
    return data

# Run each fake dataset through model
    # output time taken in milliseconds

sizes = [100, 200, 300]
def model_time(datasets):
    timings = []
    for dataset in datasets:
        start_time = time.time()
        train_model(dataset)#find model func? 
        end_time = time.time()
        timings.append((end_time - start_time) *1000)  
    return timings

# plot time taken
    # x = dataset size
    # y = time taken
def plot_timings(sizes, timings):
    plt.figure(figsize=(10, 7))
    plt.plot(sizes, timings)
    plt.xlabel('dataset size')
    plt.ylabel('time taken in milliseconds)')
    plt.grid(True)
    plt.show()


#chart for model runtime comparison 
    #change path to whoever is using 
runtimes_path = r'C:\Users\kisha\Downloads\dsc180ab\runtimes.json'
with open(runtimes_path, 'r') as f:
    runtimes = json.load(f)

sorted_sizes = sorted(runtimes.keys(), key=int)
time_taken = [runtimes[size] for size in sorted_sizes]
time_ms = [time * 1000 for time in time_taken]

plt.figure(figsize=(10, 5))
plt.plot('sorted_sizes, time_ms')
plt.title('Time Taken by Model for Datasets of Varying Sizes')
plt.xlabel('dataset size')
plt.ylabel('time taken in milliseconds)')
plt.show()








# def run_model(data, batch_size=8, epochs=10, save_checkpoint=False):
#     time.sleep(np.random.random())  

# def create_single_dataset(dataset_size, vector_length):
#     return np.random.rand(dataset_size, vector_length).tolist()

# dataset_sizes = [100, 200, 300]
# vector_length = 75
# smaller_timings = model_time(dataset_sizes, vector_length)
# smaller_sequences_file_path = ''
# with open(smaller_sequences_file_path, 'w') as file:
#     json.dump(smaller_timings, file, indent=4)#indent??

# def plot_comparison(original_timings_path, smaller_timings_path):


#     original_sizes= list(map(int, original_timings.keys()))
#     original_times= list(original_timings.values())
#     smaller_sizes =list(map(int, smaller_timings.keys()))
#     smaller_times = list(smaller_timings.values())


# plot_comparison(original_timings_path, smaller_timings_path)


