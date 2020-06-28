import string
contents = string.ascii_lowercase

# Creating the encryption table form contents above
translated = contents.maketrans(string.ascii_lowercase, string.ascii_lowercase[13:] + string.ascii_lowercase[:13])

# The normal text to be converted
first = "In the beginning was the word and the word was with God and the word was God"

# converting | substituting the normal text | string - first with rot13 encryption
first_translated = first.translate(translated)

print("")

print(first_translated)

print("")

print(first_translated.translate(translated))