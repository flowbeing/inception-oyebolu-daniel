def to_camel_case(text):
    return "" if text == "" else "".join("".join(text.title().split("-")).split("_")) if text[0] == text[0].upper() else text[0] + "".join("".join(text.title().split("-")).split("_"))[1:] if text[0] == text[0].lower() else text


#print(to_camel_case("the_stealth_warrior"))


def c_case(string):
    return string[0] + string.title().translate(str.maketrans("", "", "-_"))[1:] if string else string


print(c_case("this is_a- string"))

