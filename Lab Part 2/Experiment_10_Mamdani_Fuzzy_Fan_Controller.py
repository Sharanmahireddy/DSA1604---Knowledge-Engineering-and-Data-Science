# Experiment 10: Fan Speed Controller Using a Mamdani Fuzzy System
# Fuzzy Logic Systems

def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    if x <= b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)

def temperature_sets(temp):
    return {
        'cold': triangular_membership(temp, -1, 0, 20),
        'warm': triangular_membership(temp, 15, 25, 35),
        'hot': triangular_membership(temp, 30, 40, 41)
    }

def humidity_sets(humidity):
    return {
        'dry': triangular_membership(humidity, -1, 0, 50),
        'humid': triangular_membership(humidity, 40, 100, 101)
    }

speed_sets = {
    'low': (0, 20, 50),
    'medium': (30, 50, 70),
    'high': (50, 80, 100)
}

rules = [
    ('cold', 'dry', 'low'),
    ('cold', 'humid', 'low'),
    ('warm', 'dry', 'medium'),
    ('warm', 'humid', 'high'),
    ('hot', 'dry', 'high'),
    ('hot', 'humid', 'high')
]

def fan_speed(temp, humidity):
    temp_membership = temperature_sets(temp)
    humidity_membership = humidity_sets(humidity)

    strengths = {}

    # Rule evaluation and aggregation
    for temp_set, humidity_set, output_set in rules:
        firing_strength = min(
            temp_membership[temp_set],
            humidity_membership[humidity_set]
        )
        strengths[output_set] = max(
            strengths.get(output_set, 0),
            firing_strength
        )

    # Centroid defuzzification over output range 0 to 100
    numerator = 0.0
    denominator = 0.0

    for x in range(101):
        membership = max(
            min(strengths.get(output, 0), triangular_membership(x, *params))
            for output, params in speed_sets.items()
        )
        numerator += x * membership
        denominator += membership

    output = numerator / denominator if denominator else 0.0
    return temp_membership, humidity_membership, strengths, output

for temperature, humidity in [(10, 30), (28, 60), (38, 80)]:
    t_membership, h_membership, strengths, speed = fan_speed(temperature, humidity)

    print(f"Temp={temperature}C Hum={humidity}%")
    print("Temperature memberships:", {k: round(v, 2) for k, v in t_membership.items()})
    print("Humidity memberships   :", {k: round(v, 2) for k, v in h_membership.items()})
    print("Rule strengths         :", {k: round(v, 2) for k, v in strengths.items()})
    print(f"Fan speed (centroid)   = {speed:.2f}%\\n")
