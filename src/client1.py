import flwr as fl
import tensorflow as tf
from tensorflow import keras
import numpy as np
import sys


def getData(dist, x, y):
    dx = []
    dy = []
    counts = [0 for i in range(10)]
    for i in range(len(x)):
        if counts[y[i]]<dist[y[i]]:
            dx.append(x[i])
            dy.append(y[i])
            counts[y[i]] += 1
        
    return np.array(dx), np.array(dy)

# Load and compile Keras model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])

# Load dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0
dist = [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x_train, y_train = getData(dist, x_train, y_train)


# Define Flower client
class FlowerClient(fl.client.NumPyClient):
    def get_parameters(self,config):
        return model.get_weights()

    def fit(self, parameters, config):
        
        model.set_weights(parameters)
        print("Aggregated Weights: ",model.get_weights()[-1])
        
        r = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), verbose=0)
        print("Weights: ",model.get_weights()[-1])
        hist = r.history
        print("Fit history : " ,hist)

        print(model)
        return model.get_weights(), len(x_train), {}

    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
        print("Eval accuracy : ", accuracy)
        return loss, len(x_test), {"accuracy": accuracy}


fl.client.start_client(server_address="[::]:8080", client=FlowerClient().to_client())
