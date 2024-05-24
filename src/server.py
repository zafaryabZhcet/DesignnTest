import flwr as fl
import numpy as np
import csv

class SaveModelStrategy(fl.server.strategy.FedAvg):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_weights = {}

    def aggregate_fit(
        self,
        rnd,
        results,
        failures
    ):
        

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

        return aggregated_weights
    
    def get_classification_number(self, client_name):
        # Derive classification number from client name
        return int(client_name.replace('client', ''))
    

# Create strategy and run server
strategy = SaveModelStrategy()

fl.server.start_server(
    server_address="localhost:8080",
    config=fl.server.ServerConfig(num_rounds=10), 
    strategy=strategy
    )

with open("rnd.txt", 'w') as file:
    file.write(str(0))
file.close()
