import os
from os import listdir
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras


def get_img(data_path, size = 32):
    img = Image.open(data_path).convert('RGB')
    img = img.resize((size,size))
    img = np.asarray(img)
    return img

def get_dataset(dataset_path: str, training=True, client_num = None, im_size=32):
    labels = listdir(dataset_path) # Geting labels
    
    if training:
        X = []
        Y = []
        for i, label in enumerate(labels):
            datas_path = dataset_path+'/'+label
            for data in listdir(datas_path)[:10]:
                try:
                    img = get_img(datas_path+'/'+data, im_size)
                    X.append(img)
                    Y.append(int(label))
                except:
                    print(datas_path+'/'+data)

        # Create dateset:
        X = np.array(X).astype('float32')
        X= X/255.
        Y = np.array(Y).astype('float32')
        print(X.shape)
    else:
        X = []
        Y = []
        for i, label in enumerate(labels):
            datas_path = dataset_path+'/'+label
            for data in listdir(datas_path)[:10]:
                try:
                    img = get_img(datas_path+'/'+data, im_size)
                    X.append(img)
                    Y.append(int(label))
                except:
                    print(datas_path+'/'+data)

        # Create dateset:
        X = np.array(X).astype('float32')
        X= X/255.
        Y = np.array(Y).astype('float32')
    print(X.shape)

    return X, Y

def load_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        # tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])

    return model




