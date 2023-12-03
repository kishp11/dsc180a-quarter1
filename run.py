import sys

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

if __name__ == '__main__':
    args = sys.argv[1:]
    
    if len(args) == 0:
        args = ['predict']

    if 'train' in args:
        # TODO: Add --save argument to toggle checkpoint saving
        training_dataset = build.create_dataset('train') # train, eval, test
        model = train_model.train_model(training_dataset)
    else:
        model = train_model.load_model()
    
    if 'test' in args:
        test_dataset = build.create_dataset('test')
        accuracy = predict.evaluate_model(model, test_dataset)
        print(accuracy)

    if 'predict' in args:
        # TODO: input a file or peptide string and make a prediction on it
        # Given a file, output predictions
        print(predict.predict_from_file(model, 'data/raw/AMp.te.fa'))