# Experiment 2: Resolution Refutation for a Login System
# Propositional Logic

from itertools import combinations

def neg(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal

def resolve(c1, c2):
    results = []
    for literal in c1:
        opposite = neg(literal)
        if opposite in c2:
            resolvent = frozenset((c1 - {literal}) | (c2 - {opposite}))
            results.append(resolvent)
    return results

def fmt(clause):
    return '{' + ', '.join(sorted(clause)) + '}' if clause else '{} (empty)'

# CNF clauses: (~P OR Q), (~Q OR R), P, and NOT R (negated query)
clauses = [
    frozenset({'~P', 'Q'}),
    frozenset({'~Q', 'R'}),
    frozenset({'P'}),
    frozenset({'~R'})
]

print("Initial clauses:")
for i, clause in enumerate(clauses, 1):
    print(f"C{i}: {fmt(clause)}")

known = set(clauses)
step = 0
proved = False

while not proved:
    new = set()

    for c1, c2 in combinations(list(known), 2):
        for resolvent in resolve(c1, c2):
            if resolvent not in known and resolvent not in new:
                step += 1
                print(f"Step {step}: resolve {fmt(c1)} & {fmt(c2)} -> {fmt(resolvent)}")
                new.add(resolvent)

                if not resolvent:
                    proved = True
                    break
        if proved:
            break

    if not new:
        break

    known |= new

print("\\nQuery R proved by refutation:", proved)
