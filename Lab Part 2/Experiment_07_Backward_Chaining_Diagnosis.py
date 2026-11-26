# Experiment 7: Laptop Fault Diagnosis Using Backward Chaining
# Forward and Backward Chaining

rules = {
    'battery_fault': [
        ['screen_black', 'power_led_off', 'charger_connected']
    ],
    'display_fault': [
        ['screen_black', 'power_led_on', 'fan_running']
    ],
    'ram_fault': [
        ['power_led_on', 'beeps']
    ]
}

facts = {'screen_black', 'power_led_off', 'charger_connected'}

def backward_chain(goal, depth=0):
    padding = ' ' * depth

    if goal in facts:
        print(f"{padding}{goal}: found in facts -> True")
        return True

    if goal not in rules:
        print(f"{padding}{goal}: no fact, no rule -> False")
        return False

    for premises in rules[goal]:
        print(f"{padding}Goal {goal}: need {premises}")

        if all(backward_chain(p, depth + 1) for p in premises):
            print(f"{padding}{goal} -> True")
            return True

    print(f"{padding}{goal} -> False")
    return False

for goal in ['battery_fault', 'display_fault', 'ram_fault']:
    print(f"\\n== Proving {goal} ==")
    print("Result:", backward_chain(goal))
