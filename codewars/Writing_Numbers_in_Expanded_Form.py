def expanded_form(num):
    num = str(num)
    return " + ".join(str(item) for item in reversed([(int(number) * 10**power) for power,
            number in enumerate(reversed(num))]) if item != 0)

print(expanded_form(70834))


def expanded_form2(num):
    num = list(str(num))
    return " + ".join([i + ("0" *  (len(num) - 1 - r)) for r, i in enumerate(num) if int(i) != 0])
    # where ""0" *  (len(num) - 1 - to_deduct)" is clever manipulation
print(expanded_form2(70834))

contain = [number + 1 for number in range(100)]
print(contain)

container = [1000, 2200, 3345, 4345345, 523451130]