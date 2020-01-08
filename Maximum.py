def maximum(a, b, c):
    if (a > b) and (a > c):
        return print("'a' is the maximum number")
    elif (b > a) and (b > c):
        return print("'b' is the maximum number")
    elif (c > a) and (c > b):
        return print("'c' is the maximum number")
    else:
        return print("There is no maximum number")


maximum(1, 1, 1)