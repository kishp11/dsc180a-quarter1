# import src.features.build_datasets as build
import src.models.train_model as train_model
# import src.models.predict_model as predict
import src.visualization.time_complexity as tc

import time
import json

def main():
    model = train_model.load_model()

    # creating 10,000 
    dataset_sizes = range(1, 10000, 100)
    # dataset_sizes = [2,1]
    datasets = tc.create_fake_datasets(sizes = dataset_sizes)

    runtimes = {}
    for d in datasets:
        # Given a file, output predictions
        start = time.time()
        model.predict(d)
        end = time.time()

        run = end - start

        print(run)
        runtimes[len(d)] = run
    
    print(runtimes)

    # Save the dictionary to a file
    with open('runtimes.json', 'w') as file:
        json.dump(runtimes, file)

    # TODO: make visualization and save chart to file
        # KISHAN DOES THIS PART
        # plot time taken
            # x = dataset size
            # y = time taken
            # runtimes is a dictionary in the format x: y
        
    # Load the dictionary from the file
    with open('runtimes.json', 'r') as file:
        loaded_dict = json.load(file)

    # Print the loaded dictionary
    print(loaded_dict)


if __name__ == '__main__':
    main()