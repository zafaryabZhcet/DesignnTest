import flwr as fl
import tensorflow as tf
from tensorflow import keras
import numpy as np
import sys
from utils import get_dataset,load_model
import os 
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# Load and compile Keras model
model = load_model()

x_train, y_train, x_test, y_test = get_dataset(target=1, client=46)

# Define Flower client
class FlowerClient(fl.client.NumPyClient):
    def __init__(self, client_name):
        self.client_name = client_name

    def get_parameters(self,config):
        if not os.path.exists("/rnd.txt"):
            weights_path = './weights_active.h5'
            # Load the weights into the model
            print("\n***************Load Active learnings weights*****************\n")
            return model.load_weights(weights_path)
        
        return model.get_weights()

    def fit(self, parameters, config):
        with open("./rnd.txt", 'r') as file:
            rnd = int(file.read())
        file.close()

        print(rnd)
        model.set_weights(parameters)
        print(f"Client {self.client_name} - Aggregated Weights (last layer): ", model.get_weights()[-1])
        
        r = model.fit(x_train[rnd*20:rnd*(20)+20], y_train[rnd*20:rnd*(20)+20], epochs=1,batch_size=8, validation_data=(x_test, y_test), verbose=0)
        # r = model.fit(x_train, y_train, epochs=1,batch_size=8, validation_data=(x_test, y_test), verbose=0)
        
        hist = r.history
        print(f"Client {self.client_name} - Fit history: ", hist)
        print(f"Client {self.client_name} - Weights after training (last layer): ", model.get_weights()[-1])
        
        return model.get_weights(), len(x_train), {"client_name": self.client_name}


    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
        print(f"Client {self.client_name} - Eval accuracy: ", accuracy)
        return loss, len(x_test), {"accuracy": accuracy, "client_name": self.client_name}


client_name = "client46"  
client = FlowerClient(client_name=client_name).to_client()
fl.client.start_client(server_address="localhost:8080", client=client)