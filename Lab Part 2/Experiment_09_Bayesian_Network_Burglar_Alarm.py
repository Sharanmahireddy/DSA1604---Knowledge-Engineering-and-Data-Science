# Experiment 9: Burglar Alarm Inference Using a Bayesian Network
# Bayesian Networks

import itertools

P_B = 0.001
P_E = 0.002

P_A = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

P_J = {True: 0.90, False: 0.05}
P_M = {True: 0.70, False: 0.01}

def joint(b, e, a, j, m):
    probability = (P_B if b else 1 - P_B) * (P_E if e else 1 - P_E)
    probability *= P_A[(b, e)] if a else 1 - P_A[(b, e)]
    probability *= P_J[a] if j else 1 - P_J[a]
    probability *= P_M[a] if m else 1 - P_M[a]
    return probability

def query(variable, evidence):
    names = ['B', 'E', 'A', 'J', 'M']
    distribution = {}

    for value in (True, False):
        total = 0.0

        for combination in itertools.product([True, False], repeat=5):
            world = dict(zip(names, combination))

            if world[variable] != value:
                continue
            if any(world[key] != observed for key, observed in evidence.items()):
                continue

            total += joint(*combination)

        distribution[value] = total

    normalizer = sum(distribution.values())
    return {key: value / normalizer for key, value in distribution.items()}

queries = [
    ('B', {'J': True, 'M': True}),
    ('B', {'J': True}),
    ('E', {'J': True, 'M': True}),
    ('A', {'J': True, 'M': True})
]

for variable, evidence in queries:
    result = query(variable, evidence)
    print(f"P({variable}=True | {evidence}) = {result[True]:.4f}  "
          f"P({variable}=False | ...) = {result[False]:.4f}")
