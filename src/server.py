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
            np.savez(f"./weights/round-{rnd}-weights-{client_id}.npz", weights)
           
        if aggregated_weights is not None:
            print(f"Saving round {rnd} aggregated weights...")
            np.savez(f"./weights/round-{rnd}-aggregated-weights.npz", aggregated_weights)

        # self.save_weights_to_csv(rnd)
        print("clients weights info: ", self.client_weights)
        return aggregated_weights

    def get_classification_number(self, client_name):
        # Derive classification number from client name
        return int(client_name.replace('client', ''))
    
# Create strategy and run server
strategy = SaveModelStrategy()

fl.server.start_server(
    server_address="localhost:8080",
    config=fl.server.ServerConfig(num_rounds=5), 
    strategy=strategy
    )
