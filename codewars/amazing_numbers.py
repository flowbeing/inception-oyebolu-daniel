# THE GREAT
def amazing_one(value):
    return value == sum(pow(int(i), len(str(value))) for i in list(str(value)))


print(amazing_one(7))

# NEEDED REFINERY
def amazing_two(value):
    return value == sum([int(i)**len(str(value)) for i in list(str(value))])


print(amazing_two(7))

# THE DIFFERENT ONE. THIS ONE CHECKS THAT EACH NUMBER IN THE RAISED TO THE POWER OF THE LAST NUMBER
# IS EQUAL TO THAT NUMBER

def danielistic_number(value):
    return True if [str(value)[counter] == str(pow(int(str(value)[counter]), int(str(value)[-1])))
                    for counter, item in enumerate(str(value))].count(True) == len(str(value)) else False


print(danielistic_number(122))