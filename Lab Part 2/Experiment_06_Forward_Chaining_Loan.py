# Experiment 6: Loan Eligibility Using Forward Chaining
# Forward and Backward Chaining

rules = [
    ({'employed', 'salary_above_30k'}, 'stable_income'),
    ({'stable_income', 'credit_score_good'}, 'low_risk'),
    ({'low_risk', 'has_collateral'}, 'loan_approved'),
    ({'loan_approved'}, 'send_offer_letter')
]

facts = {
    'employed',
    'salary_above_30k',
    'credit_score_good',
    'has_collateral'
}

print("Initial facts:", sorted(facts))

fired = True
cycle = 0

while fired:
    fired = False

    for premises, conclusion in rules:
        if premises <= facts and conclusion not in facts:
            facts.add(conclusion)
            cycle += 1
            fired = True
            print(f"Cycle {cycle}: {sorted(premises)} => {conclusion}")

print("Final facts:", sorted(facts))
print("Loan approved?", 'loan_approved' in facts)
