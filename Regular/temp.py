import random
from deap import algorithms, base, creator, tools

# Define the problem
class ProtocolSelectionProblem():
    def __init__(self):
        self.toolbox = base.Toolbox()
        self.toolbox.register("bit", random.randint, 0, 1)
        self.toolbox.register("individual", tools.initRepeat, list, self.toolbox.bit, 4)  # Update size to 4
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", self.evaluate)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        self.toolbox.register("select", tools.selNSGA2)

    def evaluate(self, individual):
        # Power Consumption and Latency values for each protocol
        power_consumption = [2.5, 1.2, 1.0, 3.0]
        latency = [5, 10, 8, 7]

        # Calculate the objectives based on the selected protocol
        power_obj = sum(individual[i] * power_consumption[i] for i in range(4))
        latency_obj = sum(individual[i] * latency[i] for i in range(4))

        # Apply decision maker's selection based on battery power
        battery_power = random.uniform(0, 1)  # Randomly generate battery power
        if battery_power > 0.25:  # Latency as priority
            return latency_obj, power_obj
        else:  # Battery saving as priority
            return power_obj, latency_obj

    def optimize(self):
        # Create an instance of the problem
        self.toolbox.register("evaluate", self.evaluate)

        # Define the objective weights
        creator.create("Fitness", base.Fitness, weights=(-1.0, -1.0))
        creator.create("Individual", list, fitness=creator.Fitness)

        # Initialize the toolbox
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.bit, 4)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Define the genetic operators
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        self.toolbox.register("select", tools.selNSGA2)

        # Create the initial population
        population = self.toolbox.population(n=100)

        # Perform the evolution
        offspring = algorithms.varAnd(population, self.toolbox, cxpb=0.5, mutpb=0.1)
        fits = self.toolbox.map(self.toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit

        # Run the optimization
        while len(population) < 1000:
            offspring = algorithms.varAnd(population, self.toolbox, cxpb=0.5, mutpb=0.1)
            fits = self.toolbox.map(self.toolbox.evaluate, offspring)
            for fit, ind in zip(fits, offspring):
                ind.fitness.values = fit
            population.extend(offspring)

        # Get the non-dominated solutions
        pareto_front = tools.selNSGA2(population, k=len(population))
        return pareto_front

# Create an instance of the problem
problem = ProtocolSelectionProblem()

# Run the optimization
pareto_front = problem.optimize()

# Print the results
for solution in pareto_front:
    selected_protocols = [protocol for i, protocol in enumerate(['WiFi', 'LoRa', 'BLE', 'LTE']) if solution[i] == 1]
    print(f"Selected Protocols: {selected_protocols}")
    print(f"Power Consumption: {solution.fitness.values}")
    print(f"Latency: {solution.fitness.values}\n")
