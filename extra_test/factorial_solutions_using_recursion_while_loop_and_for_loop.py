# VERSION 1 - USING RECURSION - Can't go beyond 998 due to recursion limits

def factorial(number): # 637 µs to 633 µs

    new_number = number - 1

    if number > 1:
        return number * factorial(new_number)
    else:
        return number * 1


#print(factorial(1000))


# Version 2 - USING WHILE LOOP - Can go beyond 998 but gets slower as number increases

def factorial_two(number):  # 487 µs to 493 µs

    ans = 1

    while number:
        ans *= number
        number = number - 1

    return ans

print(factorial_two(1000))

# VERSION 3 - USING FOR LOOP AND RANGE() - Shorter code but comes with the limits of version 2

def factorial_three(number):  # 465 µs to 468 µs

    ans = 1

    for num in range(number):
        ans *= (num + 1)

    return ans


print(factorial_three(1000))