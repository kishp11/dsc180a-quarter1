import keras
from keras import layers
from src.models.metrics import sens, spec, mcc, acc

checkpoint_filepath = 'src/models/checkpoints/model_weights'

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
    model.compile(loss='binary_crossentropy', metrics = [sens, spec, acc, mcc], optimizer=adam)
    
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
