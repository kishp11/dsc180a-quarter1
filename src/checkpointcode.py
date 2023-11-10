#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import keras
from keras import layers
import sklearn
import pandas as pd
import numpy as np


# In[16]:


def read(filepath:str, label=True, seq=True):
    '''
    Reads dataset in .fa format
    returns a list of strings
    '''
    # Open the file in read-only mode ('r')
    output = []
    with open(filepath, 'r') as file:
        for line in file:
            if label==True:
                if line.startswith(">"):
                    # This line is a header line
                    output.append(line.strip())
            if seq==True:
                if not line.startswith(">"):
                    # This line contains sequence data
                    output.append(line.strip())
        file.close()

    return output


# In[ ]:


def modelNoLSTM(dataTrain):
    # runs data through classifier without the LSTM layers to train it and returns the trained model
    # Define Sequential model with 3 layers
    model = keras.Sequential(
        # code TBD here
    )
    # Call model on a test input
    x = tf.ones((3, 3))
    y = model(x)

def pipelineNoLSTM(dataTest, labels):
    # uses trained classifier without lstm layers from model function on the validation set to check for accuracy
    # runs classifier on test set
    # returns accuracy of model
    ...


# In[ ]:


def model(dataTrain):
    # runs data through classifier to train it and returns the trained model
    # Define Sequential model with 3 layers
    model = keras.Sequential(
        [
            layers.Dense(2, activation = 'tbd', name="layer1"),
            layers.Dense(3, activation = "tbd", name="layer2"),
            layers.Dense(4, name="layer3"),
        ]
    )
    # Call model on a test input
    x = tf.ones((3, 3))
    y = model(x)

def pipeline(dataTest, labels):
    # uses trained classifier with lstm layers from model function on the validation set to check for accuracy
    # runs classifier on test set
    # returns accuracy of model
    ...


# In[ ]:


def MSE(model, data, labels):
    """
    accepts data string as input
    returns an error score for the model
    """
    y_pred = model.predict(data)
    mse = tf.keras.losses.MeanSquaredError(labels)
    return mse(labels, y_pred)


# In[ ]:


def visualizations1():
'''
Compare model's accuracy with other existing model accuracies
'''
def visualizations2():
'''
Comparing model's accuracy with and without LSTM layers
'''

# etc... Likely to add more visualizations
# return different graphs regarding the model's statistics i.e. the accuracy


# In[ ]:




