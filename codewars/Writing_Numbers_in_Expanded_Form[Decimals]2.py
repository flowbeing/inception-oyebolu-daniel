def expanded_form(num):
    print(num)
    num = str(num).split(".")

    expand_before_dec = " + ".join([i + ("0" * (len(num[0]) - p - 1)) for p, i in enumerate(num[0]) if i != "0"])
    expand_after_dec = " + ".join([i + "/1" + ("0" * p) for p, i in enumerate(num[1], start=1) if i != "0"])

    if int(num[0]) > 0 and int(num[1]) == 0:
        return expand_before_dec
    elif int(num[0]) == 0 and int(num[1]) > 0:
        return expand_after_dec
    elif int(num[0]) > 0 and int(num[1]) > 0:
        return expand_before_dec + " + " + expand_after_dec


print(expanded_form(123434.234))
