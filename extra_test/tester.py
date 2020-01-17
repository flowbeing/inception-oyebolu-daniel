import string
contents = "abcdefghijklmnopqrstuvwxyz"
print(contents[14:26])

translated = contents.maketrans(string.ascii_lowercase, string.ascii_lowercase[13:] + string.ascii_lowercase[:13])

first = "In the beginning was the word and the word was with God and the word was God".translate(translated)
print(first)

print(first.translate(translated))


to_string()
