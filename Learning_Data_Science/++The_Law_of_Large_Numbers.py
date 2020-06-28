from random import randint

coin = {
    1: 'h',
    2: 't'
}

outcome = []

while len(outcome) < 1001:
    outcome.append(coin[randint(1, 2)])

print(outcome)

outcome_h = outcome.count('h')
outcome_t = outcome.count('t')

print(f" Head: {outcome_h}")
print(f" Tail: {outcome_t}")

print()
print(f"Head:Tail = {outcome_h / outcome_t}")