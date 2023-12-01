import keras
from keras import layers
import sys

def train_model(data_train):
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
    model.fit(data_train, batch_size = batch_size, epochs = 10)
    return model