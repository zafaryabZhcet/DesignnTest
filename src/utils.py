import os
import numpy as np
import tensorflow as tf
import pandas as pd
import numpy as np
import wfdb
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split

def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in df.filename_lr]
    else:
        data = [wfdb.rdsamp(path+f) for f in df.filename_hr]
    
    data = np.array([signal for signal, meta in data])
    return data


def get_dataset(target=0, client=0):

    path='ECG_data/'
    path_csv = 'annotation_fed.csv'
    sampling_rate=100

    # load and convert annotation data
    Y = pd.read_csv(path_csv)
    Y_data = Y[Y['diagnostic_superclass']==target]
    start = client*200
    Y_data = Y_data.iloc[start:start+200]
    Y = Y_data['diagnostic_superclass'].values

    # Load raw signal data
    X = load_raw_data(Y_data, sampling_rate, path)
    Y = tf.keras.utils.to_categorical(2)
    x_test, y_test = np.load('./X_test.npy'), np.load('./Y_test.npy')

    return X, Y,  x_test, y_test

def load_model():
    model = Sequential()
    model.add(LSTM(50, activation='relu',return_sequences=True, input_shape=(1000,12)))
    model.add(LSTM(50, activation='relu', input_shape=(1000,12)))
    model.add(Dropout(0.2))
    model.add(Dense(2, activation='softmax'))
    # Compile the model
    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

    return model




