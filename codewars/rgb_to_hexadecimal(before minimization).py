def rgb_to_hexadecimal(r, g, b):
    from math import floor

    def transform(num):
        # This function converts each of the r, g, b numbers to hex

        # If r or g or b is lesser than 0, the line below converts it to 0
        num = 0 if num < 0 else num

        decoder = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"
        }

        # This converts the number into two parts; the right and left part of the each hex number
        first_part = str(floor(num / 16))
        second_part = str(num % 16)

        # This section dictates the value of the second part of each number \
        # when it is greater than 9

        if 9 < int(second_part) <= 15:
            second_part = decoder[second_part]
        elif int(second_part) > 15:
            first_part = decoder["15"]

        # This section dictates the value of the first part (and sometimes of the second part)
        # of each number when it is greater than 9

        if 9 < int(first_part) <= 15:
            first_part = decoder[first_part]
        elif int(first_part) > 15:
            first_part = decoder["15"]
            second_part = decoder["15"]

        return first_part + second_part

    return transform(r) + transform(g) + transform(b)


print(rgb_to_hexadecimal(254,275,125))
