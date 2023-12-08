import argparse

import src.features.build_datasets as build
import src.models.train_model as train_model
import src.models.predict_model as predict

def main():
    parser = argparse.ArgumentParser(description='Predict whether a peptide has antimicrobial properties using a Deep Neural Network')
    parser.add_argument('--mode', choices=['train', 'test', 'predict'], nargs='+', default=['predict'], help='Specify the mode(s) to run (train, test, predict)')

    # Sub-arguments for train mode
    train_parser = parser.add_argument_group('train mode options')
    train_parser.add_argument('--trainset', choices=['train', 'test', 'evaluate'], nargs='+', default=['train'], help='Specify the subset(s) of the data to use in training')
    train_parser.add_argument('--save_weights', action='store_true', help='[Optional] Choose whether to save the model weights')

    # Sub-arguments for test mode
    test_parser = parser.add_argument_group('test mode options')
    test_parser.add_argument('--testset', choices=['train', 'test', 'evaluate'], nargs='+', default=['test'], help='Specify the subset(s) of the data to use in testing')

    # Sub-arguments for predict mode
    test_parser = parser.add_argument_group('predict mode options')
    test_parser.add_argument('--f', help='Specify the file path for .fa file')
    test_parser.add_argument('--p', action='store_true', help='[Optional] Choose whether to print predictions to console')
    # test_parser.add_argument('--s', default='/', help='[Optional] Saves predictions to given filepath')

    args = parser.parse_args()

    if 'train' in args.mode:
        training_dataset = build.create_dataset(args.trainset)  # train, eval, test
        model = train_model.train_model(training_dataset, save_checkpoint=args.save_weights)
    else:
        model = train_model.load_model()
    
    if 'test' in args.mode:
        test_dataset = build.create_dataset(args.testset)
        accuracy = predict.evaluate_model(model, test_dataset)
        metrics = ['SENS(%)', 'SPEC(%)', 'ACC(%)', 'MCC']
        for a,m in zip(accuracy[1:], metrics):
            print(f'{m}: {a}')

    if 'predict' in args.mode:
        if args.f is None:
            parser.error('Prediction requires a filepath to be specified with --f')
        else:
            # Given a file, output predictions
            prediction = predict.predict_from_file(model, args.f)
            if args.p:
                print(prediction)
            # if args.s:
            #     # TODO: Save prediction to filepath
            #     ...


if __name__ == '__main__':
    main()