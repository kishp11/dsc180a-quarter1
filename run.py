# import src.features.build_datasets as build
import src.models.train_model as train_model
# import src.models.predict_model as predict
import src.visualization.time_complexity as tc

import time

def main():
    # model = train_model.load_model()

    # creating 10,000 
    # dataset_sizes = range(1, 10000, 100)
    dataset_sizes = [1,2]
    datasets = tc.create_fake_datasets(sizes = dataset_sizes)
    
    print(len(datasets))
    print(len(datasets[0]))
    print(len(datasets[0][0]))
    print(len(datasets[1]))

    return

    runtimes = {}
    for d in datasets:
        # Given a file, output predictions
        start = time.time()
        model.predict(d)
        end = time.time()

        run = end - start

        print(run)
        runtimes[len(d)] = run
    


    # TODO: make visualization and save chart to file
        # KISHAN DOES THIS PART
        # plot time taken
            # x = dataset size
            # y = time taken
            # runtimes is a dictionary in the format x: y


if __name__ == '__main__':
    main()