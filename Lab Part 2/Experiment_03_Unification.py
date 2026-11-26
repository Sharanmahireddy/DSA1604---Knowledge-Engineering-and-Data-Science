# Experiment 3: Unification for Student-Course Queries
# Predicate Logic

def is_var(x):
    return isinstance(x, str) and bool(x) and x[0].isupper()

def unify(x, y, substitution):
    if substitution is None:
        return None
    if x == y:
        return substitution
    if is_var(x):
        return unify_var(x, y, substitution)
    if is_var(y):
        return unify_var(y, x, substitution)

    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            substitution = unify(a, b, substitution)
            if substitution is None:
                return None
        return substitution

    return None

def unify_var(variable, term, substitution):
    if variable in substitution:
        return unify(substitution[variable], term, substitution)
    if is_var(term) and term in substitution:
        return unify(variable, substitution[term], substitution)
    return {**substitution, variable: term}

tests = [
    (('enrolled', 'S', 'ds101'), ('enrolled', 'alice', 'ds101')),
    (('teaches', 'P', 'C'), ('teaches', 'rao', 'ke201')),
    (('teaches', 'rao', 'C'), ('teaches', 'kumar', 'ke201')),
    (('advisor', 'X', ('dept', 'Y')), ('advisor', 'meena', ('dept', 'cse'))),
    (('f', 'X', 'Y'), ('f', 'Y', 'a'))
]

for first, second in tests:
    print(first, '<->', second, '=>', unify(first, second, {}))
