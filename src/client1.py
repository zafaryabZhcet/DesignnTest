import flwr as fl
import tensorflow as tf
from tensorflow import keras
import numpy as np
import sys
from utils import get_dataset,load_model


# Load and compile Keras model
model = load_model()

x_train, y_train = get_dataset(dataset_path='dataset/train/client1', training=True)

x_test, y_test = get_dataset(dataset_path='dataset/test')


# Define Flower client
class FlowerClient(fl.client.NumPyClient):
    def __init__(self, client_name):
        self.client_name = client_name

    def get_parameters(self,config):
        return model.get_weights()

    def fit(self, parameters, config):
        with open("./rnd.txt", 'r') as file:
            rnd = int(file.read())
        file.close()

        print(rnd)      

        model.set_weights(parameters)
        print(f"Client {self.client_name} - Aggregated Weights (last layer): ", model.get_weights()[-1])
        
        r = model.fit(x_train[rnd*100:rnd*(100)+100], y_train[rnd*100:rnd*(100)+100], epochs=1,batch_size=8, validation_data=(x_test, y_test), verbose=0)
        
        hist = r.history
        print(f"Client {self.client_name} - Fit history: ", hist)
        print(f"Client {self.client_name} - Weights after training (last layer): ", model.get_weights()[-1])
        
        return model.get_weights(), len(x_train), {"client_name": self.client_name}


    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
        print(f"Client {self.client_name} - Eval accuracy: ", accuracy)
        return loss, len(x_test), {"accuracy": accuracy, "client_name": self.client_name}


client_name = "client1"  
client = FlowerClient(client_name=client_name).to_client()
fl.client.start_client(server_address="localhost:8080", client=client)
