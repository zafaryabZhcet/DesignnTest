# import flwr as fl
# import sys
# import numpy as np

# class SaveModelStrategy(fl.server.strategy.FedAvg):
#     def aggregate_fit(
#         self,
#         rnd,
#         results,
#         failures
#     ):
#         aggregated_weights = super().aggregate_fit(rnd, results, failures)
#         if aggregated_weights is not None:
#             # Save aggregated_weights
#             print(f"Saving round {rnd} aggregated_weights...")
#             np.savez(f"round-{rnd}-weights.npz", *aggregated_weights)
#         return aggregated_weights

# # Create strategy and run server
# strategy = SaveModelStrategy()

# fl.server.start_server(config=fl.server.ServerConfig(num_rounds=5), strategy = strategy)

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
        aggregated_weights = super().aggregate_fit(rnd, results, failures)

        for fit_res in results:
            client_name = fit_res.metrics["client_name"]
            classification_number = self.get_classification_number(client_name)
            last_layer_weights = self.extract_last_layer_weights(fit_res.parameters)
            self.client_weights[client_name] = (last_layer_weights, classification_number)

        if aggregated_weights is not None:
            # Save aggregated_weights
            print(f"Saving round {rnd} aggregated_weights...")
            np.savez(f"round-{rnd}-weights.npz", *aggregated_weights)

        self.save_weights_to_csv(rnd)
        return aggregated_weights

    def get_classification_number(self, client_name):
        # Derive classification number from client name
        return int(client_name.replace('client', ''))

    def extract_last_layer_weights(self, parameters):
        # Assuming parameters is a list of numpy arrays, extract the last layer's weights
        return parameters[-1].flatten().tolist()

    def save_weights_to_csv(self, rnd):
        csv_file = f"round-{rnd}-weights.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Client Name", "Classification Number", "Last Layer Weights"])
            for client_name, (last_layer_weights, classification_number) in self.client_weights.items():
                writer.writerow([client_name, classification_number] + last_layer_weights)
        print(f"Weights and classification numbers saved to {csv_file}")

# Create strategy and run server
strategy = SaveModelStrategy()

fl.server.start_server(config=fl.server.ServerConfig(num_rounds=5), strategy=strategy)
