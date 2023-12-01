import sys

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

if __name__ == '__main__':
    args = sys.argv[1:]
    
    if len(args) == 0:
        args = ['train', 'predict']

    if 'train' in args:
        training_dataset = build.create_dataset('train') # train, eval, test
        model = train_model.train_model(training_dataset)
    
    if 'predict' in args:
        test_dataset = build.create_dataset('test')
        accuracy = predict.evaluate_model(model, test_dataset)
        print(accuracy)

