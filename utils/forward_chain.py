def forward_chain(rules, facts):
    conclusions = set(facts)
    changed = True
    while changed:
        changed = False
        for antecedents, consequent in rules:
            if all(f in conclusions for f in antecedents) and consequent not in conclusions:
                conclusions.add(consequent)
                changed = True
    return conclusions
