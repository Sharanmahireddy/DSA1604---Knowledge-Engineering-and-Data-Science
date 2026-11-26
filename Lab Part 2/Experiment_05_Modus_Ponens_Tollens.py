# Experiment 5: Modus Ponens and Modus Tollens in Network Fault Diagnosis
# Inference Mechanisms

rules = [
    ('Power', 'RouterOn'),
    ('RouterOn', 'WifiOn'),
    ('WifiOn', 'InternetOK')
]

def infer(known):
    changed = True

    while changed:
        changed = False

        for antecedent, consequent in rules:
            # Modus Ponens
            if known.get(antecedent) is True and consequent not in known:
                known[consequent] = True
                changed = True
                print(f"Modus Ponens: {antecedent} = True and "
                      f"({antecedent} -> {consequent}) => {consequent} = True")

            # Modus Tollens
            if known.get(consequent) is False and antecedent not in known:
                known[antecedent] = False
                changed = True
                print(f"Modus Tollens: {consequent} = False and "
                      f"({antecedent} -> {consequent}) => {antecedent} = False")

    return known

print("Case A: Power = True")
print("Result:", infer({'Power': True}))

print("\\nCase B: InternetOK = False")
print("Result:", infer({'InternetOK': False}))
