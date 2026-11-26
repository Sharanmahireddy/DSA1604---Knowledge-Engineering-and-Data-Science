# Experiment 8: Medical Screening with Bayes' Theorem
# Probabilistic Reasoning

prior = 0.02
sensitivity = 0.95
specificity = 0.90

def update(probability, positive=True):
    likelihood_disease = sensitivity if positive else 1 - sensitivity
    likelihood_no_disease = (1 - specificity) if positive else specificity

    evidence = (likelihood_disease * probability
                + likelihood_no_disease * (1 - probability))

    posterior = likelihood_disease * probability / evidence
    return posterior, evidence

# First positive test
p1, evidence1 = update(prior)

# Second independent positive test, using the first posterior as prior
p2, _ = update(p1)

# One negative test
p_negative, _ = update(prior, positive=False)

print(f"Prior P(Disease)              = {prior:.4f}")
print(f"P(Test+)                      = {evidence1:.4f}")
print(f"P(Disease | Test1 +)          = {p1:.4f}")
print(f"P(Disease | Test1 +, Test2 +) = {p2:.4f}")
print(f"P(Disease | Test1 -)          = {p_negative:.4f}")
