# This program adds up to four numbers together
# My concern is how to make the program up to infinite number parameters togethers

def addition(a=None, b=None, c=None, d=None):
    if a is not None and b is not None and c is not None and d is not None:
        return a + b + c + d

    elif a is not None and b is not None and c is not None and d is None:
        return a + b + c

    elif a is not None and b is not None and c is None and d is None:
        return a + b

    elif a is not None and b is None and c is None and d is None:
        return a


print(addition(4,6,7,9))
