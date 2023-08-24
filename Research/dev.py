import itertools

def generate_combinations(choices):
    # Calculate the total number of elements
    num_elements = len(choices)

    # Calculate the total number of choices for each element
    choices_count = [len(choices[i]) for i in range(num_elements)]

    # Generate all combinations using itertools.product
    all_combinations = list(itertools.product(*choices))

    return all_combinations

# Define the choices for each element
element1_choices = [1, 2, 3]
element2_choices = ['A', 'B']
element3_choices = [True, False]
element4_choices = [10, 20]
element5_choices = ['X', 'Y', 'Z']
element6_choices = ['apple', 'orange']
element7_choices = [100, 200, 300]
element8_choices = ['red', 'blue', 'green']

# Store all the choices in a list
choices_list = [
    element1_choices,
    element2_choices,
    element3_choices,
    element4_choices,
    element5_choices,
    element6_choices,
    element7_choices,
    element8_choices,
]

# Generate all combinations of the choices
all_combinations = generate_combinations(choices_list)

# Print all the combinations
for combination in all_combinations:
    print(combination)
