import argparse

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

def main():
    parser = argparse.ArgumentParser(description='Train, test, and predict using a model.')
    parser.add_argument('--mode', choices=['train', 'test', 'predict'], nargs='+', default=['predict'], help='Specify the mode(s) to run (train, test, predict)')

    # Sub-argument for train mode
    train_parser = parser.add_argument_group('train mode options')
    train_parser.add_argument('--trainset', choices=['train', 'test', 'eval'], nargs='+', default=['train'], help='Specify the subset(s) of the data to use in training')

    # Sub-argument for test mode
    test_parser = parser.add_argument_group('test mode options')
    test_parser.add_argument('--testset', choices=['train', 'test', 'eval'], nargs='+', default=['train'], help='Specify the subset(s) of the data to use in testing')

    # Add other arguments as needed
    # parser.add_argument('--save', action='store_true', help='Toggle checkpoint saving')
    parser.add_argument('--f', help='Specify the file path for .fa file when mode is predict')

    args = parser.parse_args()

    if 'train' in args.mode:
        # TODO: Add --save argument to toggle checkpoint saving
        training_dataset = build.create_dataset(args.trainset)  # train, eval, test
        model = train_model.train_model(training_dataset)
    else:
        model = train_model.load_model()
    
    if 'test' in args.mode:
        test_dataset = build.create_dataset(args.testset)
        accuracy = predict.evaluate_model(model, test_dataset)
        print(f'Test Accuracy: {accuracy}')

    if 'predict' in args.mode:
        if args.f is None:
            parser.error('Prediction requires a filepath to be specified with --f')
        else:
            # Given a file, output predictions
            print(predict.predict_from_file(model, args.f))

if __name__ == '__main__':
    main()