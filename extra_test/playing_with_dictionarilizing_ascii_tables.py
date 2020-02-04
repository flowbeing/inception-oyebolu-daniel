import string

# The code below puts the ascii table starting from number 33 in a dictionary
ascii = ["NUL","SOH","STX","ETX","EOT","ENQ","ACK","BEL","BS","HT","LF","VT","FF","CR","SO","SI","DLE","DC1","DC2",
         "DC3","DC4","NAK","SYN","ETB","CAN","EM","SUB","ESC","FS","GS","RS","US","SPACE"] + \
        list(f"!“#$%&‘()*+,-./{string.digits}:;<=>?@{string.ascii_letters[26:]}[\u005c]^_`{string.ascii_letters[:26]}"
             + "{|}~") + ["DEL"]

dict_1 = {item: str(i) for i, item in enumerate(ascii, start=0)}  # V1
dict_2 = {chr(i): i for i in range(128)}  # V2 This is the simpler and less time_taking to code and run solution

# This code below checks to see if the items and numberings in the above generated dictionaries are equal
comparator = [(value_one, value_two) for value_one, value_two in zip(dict_1.keys(), dict_2.keys())]

for i, value in enumerate(comparator):
    print(i, value)