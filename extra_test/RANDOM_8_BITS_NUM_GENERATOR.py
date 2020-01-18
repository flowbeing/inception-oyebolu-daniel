# ##I'D LIKE TO IMPROVE V2 TO BE ABLE TO ACCOMMODATE ALL POSSIBLE LENGTHS AND AS MUCH NUMBER AS POSSIBLE FOR COMBINATION

# THIS IS A 8 BITS NUMBER GENERATOR v1
# Note tha v1 is more flexible than v2
# IT CAN BE EASILY TWEAKED TO GENERATE A LESS OR MORE NUMBERS
# Just change the 8 in Solution two to get a different result

import random

# Solution one
# r = [random.randint(0, 1) for item in range(0,8)]
# print(("{}" * 8).format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))

# Solution two
print(f'V1 - Your random number is {"".join(str(random.randint(0, 1)) for item in range(0, 10))}')
print(f'V1 - length cannot be applied to random 1')
print("")

# ---------------------------------------------------------------------------------------------------------------------

# RANDOM 8 BIT NUMBER GENERATOR v2
# This version need some extra deleting or code addition within the list comprehension to ensure it print more than
# or less than 8 numbers. The advantage however is that it can list all possible number within an 8 bit number and it
# can easily be tweaked to print all possible number 8 numbers in the combination of other numbers specified in i

i = ["0", "1", ]

# print("\n".join(f"{a}{b}{c}{d}{e}{f}{g}{h}" for a in i for b in i for c in i for d in i for e in i for f in i for g
# in i for h in i))
r = [f"{a}{b}{c}{d}{e}{f}{g}{h}" for a in i for b in i for c in i for d in i for e in i for f in i for g in i for h in
     i]

# print("\n".join(r))

print(f'V2 - Your random number is {r[random.randint(0, 255)]}')
print(f'V2 - length is {len(r)}')
print("")


# Asks the user whether to show all possible numbers or not
ask = input("V2 - Do you want to view all possible numbers? y/n:")
if ask == "y":
    print("\n".join(r))
else:
    pass
