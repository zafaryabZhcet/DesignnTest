import flwr as fl
import numpy as np
import csv


from utils import get_dataset,load_model
import os 
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# Load and compile Keras model
model = load_model()
x_test, y_test = np.load('./X_test.npy'), np.load('./Y_test.npy')
initial_parameters = fl.common.ndarrays_to_parameters(model.get_weights())

# class SaveModelStrategy(fl.server.strategy.FedAvg):
#     def __init__(self, min_fit_clients=30, min_available_clients=30, min_evaluate_clients=30, *args, **kwargs):
#         super().__init__(min_fit_clients=min_fit_clients,
#                          min_available_clients=min_available_clients,
#                          min_evaluate_clients=min_evaluate_clients,
#                          *args, **kwargs)
#         self.client_weights = {}
class SaveModelStrategy(fl.server.strategy.FedAdam):
    def __init__(self, min_fit_clients=30, min_available_clients=30, min_evaluate_clients=30, *args, **kwargs):
        super().__init__(min_fit_clients=min_fit_clients,
                         min_available_clients=min_available_clients,
                         min_evaluate_clients=min_evaluate_clients,
                         initial_parameters=initial_parameters,
                         eta=0.005,  # Learning rate
                         eta_l=0.005,  # Server learning rate
                         beta_1=0.85,
                         beta_2=0.999,
                         tau=1e-4,  #L2 regularization
                         *args, **kwargs)
        self.client_weights = {}

    def aggregate_fit(self,rnd,results,failures):
        # Perform aggregation using the superclass method
        aggregated_weights = super().aggregate_fit(rnd, results, failures)
    
        # Access and save weights from individual clients
        for client_res in results:
            client_id = client_res[1].metrics["client_name"]
            weights = client_res[1].parameters
            # np.savez(f"./weights/round-{rnd}-weights-{client_id}.npz", weights)
            client_weights_list = fl.common.parameters_to_ndarrays(weights)
            
            # Convert numpy arrays to lists
            client_weights_as_lists = [w.tolist() for w in client_weights_list]
            
            # Save client weights as lists
            # print(f"Saving round {rnd} client {client_id} weights as lists...")
            np.savez(f"./weights/round-{rnd}-client-{client_id}.npz", *client_weights_as_lists)

        with open("rnd.txt", 'w') as file:
            file.write(str(rnd))
        file.close()

        agg_weights = fl.common.parameters_to_ndarrays(aggregated_weights[0])
        model.set_weights(agg_weights)
        loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

        print(f"After {rnd} Round: loss = {loss}, accuracy: {accuracy}")

        return aggregated_weights
    
    def get_classification_number(self, client_name):
        # Derive classification number from client name
        return int(client_name.replace('client', ''))
    

# Create strategy and run server
strategy = SaveModelStrategy()

fl.server.start_server(
    server_address="localhost:8080",
    config=fl.server.ServerConfig(num_rounds=3), 
    strategy=strategy
    )


with open("rnd.txt", 'w') as file:
    file.write(str(0))
file.close()



#######OLD method where each client was evaluating##############
# import flwr as fl

# import numpy as np
# import csv

# class SaveModelStrategy(fl.server.strategy.FedAvg):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.client_weights = {}

#     def aggregate_fit(
#         self,
#         rnd,
#         results,
#         failures
#     ):
        

#         # Perform aggregation using the superclass method
#         aggregated_weights = super().aggregate_fit(rnd, results, failures)
    
#         # Access and save weights from individual clients
#         for client_res in results:
#             client_id = client_res[1].metrics["client_name"]
#             weights = client_res[1].parameters
#             # np.savez(f"./weights/round-{rnd}-weights-{client_id}.npz", weights)
#             client_weights_list = fl.common.parameters_to_ndarrays(weights)
            
#             # Convert numpy arrays to lists
#             client_weights_as_lists = [w.tolist() for w in client_weights_list]
            
#             # Save client weights as lists
#             print(f"Saving round {rnd} client {client_id} weights as lists...")
#             np.savez(f"./weights/round-{rnd}-client-{client_id}.npz", *client_weights_as_lists)

#         with open("rnd.txt", 'w') as file:
#             file.write(str(rnd))
#         file.close()

#         return aggregated_weights
    
#     def get_classification_number(self, client_name):
#         # Derive classification number from client name
#         return int(client_name.replace('client', ''))
    

# # Create strategy and run server
# strategy = SaveModelStrategy()

# fl.server.start_server(
#     server_address="localhost:8080",
#     config=fl.server.ServerConfig(num_rounds=10), 
#     strategy=strategy
#     )

# with open("rnd.txt", 'w') as file:
#     file.write(str(0))
# file.close()
