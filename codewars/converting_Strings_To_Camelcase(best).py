# One
def to_camel_case(text):
    return text[:1] + "".join("".join(text.title().split("_")).split("-"))[1:]

print(to_camel_case("Camel_case-2"))

# Two
def to_camel_case(text):
    return text[:1] + text.title().replace("-", "").replace("_", "")[1:]

print(to_camel_case("Camel_case-2"))