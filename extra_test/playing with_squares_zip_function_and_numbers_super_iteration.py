def subtractor(container):
    return [int(item/counter) for counter, item in enumerate(container) if item != 0]


print(subtractor([0, 1, 4, 9, 16, 25, 36, 49, 64, 81]))

one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("")

print([item for item in zip(one, two, three)])

print("")

def p_and_c(one, two, three):
    return ((a, b, c) for a in one for b in two for c in three)


def see():
    return f"The length is {len([item for item in p_and_c(one, two, three)])} and item in it are: " \
           f"\n{[item for item in p_and_c(one, two, three)]}"


print(see())

print("")

print([(a, b, c) for (a, b, c) in item if c - b == 1 and b - a == 1] for item in p_and_c(one, two, three))

#for position, item in enumerate(p_and_c(one, two, three), start=1):
#    print(f"{position}. ({item[0]}, {item[1]})")

print(list(p_and_c(one, two, three)))