import numpy as np

# Define the properties of the protocols (Wi-Fi, LoRa, Bluetooth, LTE)
protocols = {
    "Wi-Fi": {
        "data_rate": 100,
        "power_consumption": 6,
        "coverage_area": 200
    },
    "LoRa": {
        "data_rate": 5,
        "power_consumption": 2,
        "coverage_area": 3000
    },
    "Bluetooth": {
        "data_rate": 75,
        "power_consumption": 4,
        "coverage_area": 10
    },
    "LTE": {
        "data_rate": 150,
        "power_consumption": 9,
        "coverage_area": 10000
    }
}

# Define the weights for each objective
weights = {
    "data_rate": 0.2,
    "power_consumption": 0.8,
    "coverage_area": 0.6
}

# Normalize the objectives (data rate, power consumption, coverage area) and apply weights
normalized_objectives = {}
for property_name in ["data_rate", "power_consumption", "coverage_area"]:
    values = np.array([protocols[protocol][property_name] for protocol in protocols])
    normalized_values = (values - np.min(values)) / (np.max(values) - np.min(values))
    normalized_objectives[property_name] = normalized_values

# Calculate the weighted scores for each protocol
weighted_scores = {}
for protocol in protocols:
    weighted_scores[protocol] = sum(
        normalized_objectives[property_name][i] * weights[property_name]
        for i, property_name in enumerate(normalized_objectives)
    )

# Select the protocol with the highest weighted score
best_protocol = max(weighted_scores, key=weighted_scores.get)

# Print the best protocol
print("The best protocol based on the MOO approach is:", best_protocol)
