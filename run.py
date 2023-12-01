import sys

import src.features.build_datasets as build
import src.models.train_model as train_model

if __name__ == '__main__':
    args = sys.argv[1:]

    args = ['train']

    if 'train' in args:
        training_dataset = build.create_dataset(build.read('data/raw/AMP.tr.fa', 'r'), build.read('data/raw/DECOY.tr.fa', 'r'))
        # model = train_model.train_model(training_dataset)
    
    if ... in args:
        ...

