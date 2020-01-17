def to_camel_case(text):
    if text == text.title():
        print("".join("".join(text.split("-")).split("_")))
    elif text == text.lower():
            print( (text.split("-")[0] + "".join(text.title().split("-")[1:]))
                  if "-" in text else (text.split("_")[0] + "".join(text.title().split("_")[1:])) )


to_camel_case("camel-case-2")