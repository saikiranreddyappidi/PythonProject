import random
import math

protocols = ["Wi-Fi", "Bluetooth", "LoRa", "LTE"]
# in meters
protocol_ranges = {
    "Wi-Fi": 100,
    "Bluetooth": 10,
    "LoRa": 3000,
    "LTE": 10000
}
data_rate_scores = [random.uniform(0, 1) for _ in range(4)]
power_consumption_scores = [random.uniform(0, 1) for _ in range(4)]
distance_scores = [random.uniform(0, 1) for _ in range(4)]


class Selector:
    def entropy(self):
        data_rate_sum = sum(data_rate_scores)
        data_rate_entropy = 0

        for score in data_rate_scores:
            p = score / data_rate_sum
            data_rate_entropy -= p * math.log(p)

        power_consumption_sum = sum(power_consumption_scores)
        power_consumption_entropy = 0

        for score in power_consumption_scores:
            p = score / power_consumption_sum
            power_consumption_entropy -= p * math.log(p)

        distance_sum = sum(distance_scores)
        distance_entropy = 0

        for score in distance_scores:
            p = score / distance_sum
            distance_entropy -= p * math.log(p)

        total_entropy = data_rate_entropy + power_consumption_entropy + distance_entropy
        data_rate_weight = data_rate_entropy / total_entropy
        power_consumption_weight = power_consumption_entropy / total_entropy
        distance_weight = distance_entropy / total_entropy

        weighted_scores = []
        for i in range(len(data_rate_scores)):
            weighted_score = (data_rate_scores[i] * data_rate_weight) + (
                    power_consumption_scores[i] * power_consumption_weight) + (distance_scores[i] * distance_weight)
            weighted_scores.append(weighted_score)

        return weighted_scores

    def selections(self):
        for _ in range(10):
            weights = self.entropy()
            best = None
            distance_range = random.randint(0, 1000)
            max_weight = float(0)
            for i, j in zip(weights, protocols):
                if max_weight < i and protocol_ranges[j] >= distance_range:
                    best = j
                    max_weight = i
            print(data_rate_scores, power_consumption_scores, distance_scores, sep="\n")
            print(distance_range, best)


Sel = Selector()
Sel.selections()
