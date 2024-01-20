# import src.features.build_datasets as build
import src.models.train_model as train_model
# import src.models.predict_model as predict
import src.visualization.time_complexity as tc

import time

def main():
    model = train_model.load_model()

    # runs test metrics with given test datasets 
    datasets = tc.create_fake_datasets('NUMBER OF FAKE DATASETS') # TODO

    runtimes = []
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


if __name__ == '__main__':
    main()