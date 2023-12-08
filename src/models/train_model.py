import keras
from keras import layers

import keras.backend as K
from keras.metrics import TruePositives, FalsePositives, TrueNegatives, FalseNegatives

checkpoint_filepath = 'src/models/checkpoints/model_weights'

tp = TruePositives()
fp = FalsePositives()
tn = TrueNegatives()
fn = FalseNegatives()

def __TPTNFPFN(y_true, y_pred):
    return tp(y_true, y_pred), tn(y_true, y_pred), fp(y_true, y_pred), fn(y_true, y_pred)

def __sens(y_true, y_pred):
    # Assuming binary classification
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    sens = true_positives/(true_positives + false_negatives + K.epsilon()) * 100 # K.epsilon() is a small constant that prevents divide by zero errors
    return sens

def __spec(y_true, y_pred):
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    spec = true_negatives/(true_negatives + false_positives + K.epsilon()) * 100
    return spec

def __acc(y_true, y_pred):
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    acc = (true_positives + true_negatives)/(true_positives + false_positives + true_negatives + false_negatives + K.epsilon()) * 100
    return acc

def __mcc(y_true, y_pred):
    true_positives, true_negatives, false_positives, false_negatives = __TPTNFPFN(y_true, y_pred)
    mcc = (((true_positives * true_negatives) - (false_negatives * false_positives)) / 
            K.sqrt((true_positives + false_negatives) * (true_negatives + false_positives) * (true_positives + false_positives) * (true_negatives + false_negatives)) + K.epsilon())
    return mcc

def __create_model():
    # define sequential model
    model = keras.Sequential(
        [
            layers.Embedding(200, 128, input_shape = (200,), name="embed"),
            layers.Conv1D(filters = 64, kernel_size = 16, activation="relu", name="conv"),
            layers.MaxPooling1D(pool_size = 5, name = 'pooling'),
            layers.LSTM(units = 100, unroll = True, stateful = False, dropout = 0.1, name = 'lstm'),
            layers.Dense(1, activation = 'sigmoid')
        ]
    )

    # Compile model using binary crossentropy loss and Adam optimizer
    adam = keras.optimizers.Adam()
    model.compile(loss='binary_crossentropy', metrics = [__sens, __spec, __acc, __mcc], optimizer=adam)
    
    return model

def train_model(data_train, batch_size=8, epochs=10, save_checkpoint=False):
    '''
    trains the model on provided training dataset
    '''
    model = __create_model()

    model.fit(data_train, batch_size=batch_size, epochs=epochs)

    if save_checkpoint:
        # Saves model weights to models/checkpoints/
        model.save_weights(checkpoint_filepath)

    return model

def load_model():
    """
    Loads model weights from checkpoint file
    """
    model = __create_model()
    model.load_weights(checkpoint_filepath).expect_partial() # expect_partial as otherwise many warnings thrown in console
    return model
