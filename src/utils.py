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
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam

import numpy as np

def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in df.filename_lr]
    else:
        data = [wfdb.rdsamp(path+f) for f in df.filename_hr]
    
    data = np.array([signal for signal, meta in data])
    return data


def get_dataset(target=0, client=0):

    path='./ECG_data/'
    path_csv = './federated_data.csv'
    sampling_rate=100
    sample_size = 200
  
    # load and convert annotation data
    Y = pd.read_csv(path_csv)
    Y_data = Y[Y['diagnostic_superclass']==target]
    if target==1:
        client = client- 20
        sample_size = 200
    start = client*sample_size
    Y_data = Y_data.iloc[start:start+sample_size]
    Y = Y_data['diagnostic_superclass'].values
    # Load raw signal data
    X = load_raw_data(Y_data, sampling_rate, path)
    
    return X, Y

def load_model():
    model = Sequential([
    Conv1D(filters=32, kernel_size=5, activation='relu', input_shape=(1000, 12)),
    MaxPooling1D(pool_size=2),
    BatchNormalization(),
    Conv1D(filters=64, kernel_size=5, activation='relu'),
    MaxPooling1D(pool_size=2),
    BatchNormalization(),
    Conv1D(filters=128, kernel_size=5, activation='relu'),
    MaxPooling1D(pool_size=2),
    BatchNormalization(),
    Flatten(),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # For binary classification
])
    model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

    return model




#######OLD method where each client was evaluating##############
# import os
# import numpy as np
# import tensorflow as tf
# import pandas as pd
# import numpy as np
# import wfdb
# from tensorflow import keras
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense, Dropout
# from sklearn.model_selection import train_test_split

# def load_raw_data(df, sampling_rate, path):
#     if sampling_rate == 100:
#         data = [wfdb.rdsamp(path+f) for f in df.filename_lr]
#     else:
#         data = [wfdb.rdsamp(path+f) for f in df.filename_hr]
    
#     data = np.array([signal for signal, meta in data])
#     return data


# def get_dataset(target=0, client=0):

#     path='./ECG_data/'
#     path_csv = './filtered_data.csv'
#     sampling_rate=100
#     sample_size = 300
  
#     # load and convert annotation data
#     Y = pd.read_csv(path_csv)
#     Y_data = Y[Y['diagnostic_superclass']==target]
#     if target==1:
#         client -= 20
#         sample_size = 350
#     start = client*sample_size
#     Y_data = Y_data.iloc[start:start+sample_size]
#     Y = Y_data['diagnostic_superclass'].values

#     # Load raw signal data
#     X = load_raw_data(Y_data, sampling_rate, path)
#     Y = tf.keras.utils.to_categorical(Y,2)
#     x_test, y_test = np.load('./X_test.npy'), np.load('./Y_test.npy')

#     return X, Y,  x_test, y_test

# def load_model():
#     model = Sequential()
#     model.add(LSTM(50, activation='relu',return_sequences=True, input_shape=(1000,12)))
#     model.add(LSTM(50, activation='relu', input_shape=(1000,12)))
#     model.add(Dropout(0.2))
#     model.add(Dense(2, activation='softmax'))
#     # Compile the model
#     model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

#     return model




