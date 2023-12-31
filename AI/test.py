import time


def Cost(H, condition, weight=1):
    cost = {}
    if 'AND' in condition:
        AND_nodes = condition['AND']
        Path_A = ' AND '.join(AND_nodes)
        PathA = sum(H[node] + weight for node in AND_nodes)
        cost[Path_A] = PathA

    if 'OR' in condition:
        OR_nodes = condition['OR']
        Path_B = ' OR '.join(OR_nodes)
        PathB = min(H[node] + weight for node in OR_nodes)
        cost[Path_B] = PathB
    return cost


def update_cost(H, Conditions, weight=1):
    Main_nodes = list(Conditions.keys())
    Main_nodes.reverse()
    least_cost = {}
    for key in Main_nodes:
        condition = Conditions[key]
        print(key, ':', Conditions[key], '>>>', Cost(H, condition, weight))
        c = Cost(H, condition, weight)
        H[key] = min(c.values())
        least_cost[key] = Cost(H, condition, weight)
    return least_cost


def shortest_path(Start, Updated_cost, H):
    Path = Start
    if Start in Updated_cost.keys():
        Min_cost = min(Updated_cost[Start].values())
        key = list(Updated_cost[Start].keys())
        values = list(Updated_cost[Start].values())
        Index = values.index(Min_cost)
        Next = key[Index].split()
        if len(Next) == 1:

            Start = Next[0]
            Path += '<--' + shortest_path(Start, Updated_cost, H)
        else:
            Path += '<--(' + key[Index] + ') '

            Start = Next[0]
            Path += '[' + shortest_path(Start, Updated_cost, H) + ' + '

            Start = Next[-1]
            Path += shortest_path(Start, Updated_cost, H) + ']'

    return Path


# Gather user input for H values
try:
    H = {}
    nodes = input("Enter node names separated by spaces: ").split()
    for node in nodes:
        H[node] = int(input(f"Enter H({node}): "))

    # Gather user input for conditions
    Conditions = {}
    while True:
        node = input("Enter node name (or 'done' to finish): ")
        if node == 'done':
            break
        condition_type = input(f"Enter condition type for {node} ('OR' or 'AND'): ")
        if condition_type not in ['OR', 'AND']:
            print("Invalid condition type. Please enter 'OR' or 'AND'.")
            continue
        sub_conditions = input(f"Enter sub-nodes for {node} separated by spaces: ").split()
        Conditions[node] = {condition_type: sub_conditions}
    start = time.time()
    weight = int(input("Enter weight: "))
    print('Updated Cost :')
    Updated_cost = update_cost(H, Conditions, weight)
    print('*' * 75)
    print('Shortest Path :\n', shortest_path('A', Updated_cost, H))
    stop= time.time()
    print("Execution time: ",stop-start)
except:
    print("Invalid inputs: Restart the program")
