def rgb_to_hexadecimal(r, g, b):
    contain = lambda value: min(255, max(value, 0))
    return ("{:02X}" * 3).format(contain(r), contain(g), contain(b))

print(rgb_to_hexadecimal(255, 255, 255))