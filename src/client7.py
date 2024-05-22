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
dist = [0, 0, 0, 0, 0, 0, 0, 1000, 0, 0]
x_train, y_train = getData(dist, x_train, y_train)


# Define Flower client
class FlowerClient(fl.client.NumPyClient):
    def __init__(self, client_name):
        self.client_name = client_name

    def get_parameters(self,config):
        return model.get_weights()

    def fit(self, parameters, config):
        model.set_weights(parameters)
        print(f"Client {self.client_name} - Aggregated Weights (last layer): ", model.get_weights()[-1])
        
        r = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), verbose=0)
        
        hist = r.history
        print(f"Client {self.client_name} - Fit history: ", hist)
        print(f"Client {self.client_name} - Weights after training (last layer): ", model.get_weights()[-1])
        
        return model.get_weights(), len(x_train), {"client_name": self.client_name}


    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
        print(f"Client {self.client_name} - Eval accuracy: ", accuracy)
        return loss, len(x_test), {"accuracy": accuracy, "client_name": self.client_name}


client_name = "client7"  
client = FlowerClient(client_name=client_name)
fl.client.start_numpy_client(server_address="[::]:8080", client=client)