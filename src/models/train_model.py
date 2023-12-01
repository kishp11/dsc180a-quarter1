import keras
from keras import layers
import sys

checkpoint_filepath = 'src/models/checkpoints/model_weights'

def __create_model():
    model = keras.Sequential(
        [
            layers.Embedding(200, 128, input_shape = (200,), name="embed"),
            layers.Conv1D(filters = 64, kernel_size = 16, activation="relu", name="conv"),
            layers.MaxPooling1D(pool_size = 5, name = 'pooling'),
            layers.LSTM(units = 100, unroll = True, stateful = False, dropout = 0.1, name = 'lstm'),
            layers.Dense(1, activation = 'sigmoid')
        ]
    )

    adam = keras.optimizers.Adam()
    model.compile(loss='binary_crossentropy', metrics = 'accuracy', optimizer=adam)

    return model

def train_model(data_train, batch_size=8, epochs=10, save_checkpoint=True):
    model = __create_model()

    model.fit(data_train, batch_size=batch_size, epochs=epochs)

    if save_checkpoint:
        model.save_weights(checkpoint_filepath)

    return model

def load_model():
    model = __create_model()
    model.load_weights(checkpoint_filepath).expect_partial()
    return model