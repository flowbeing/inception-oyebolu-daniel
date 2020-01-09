import re

# ----------------------------------------

container = "This is 15 a 6 str1nig517126"

print(re.findall(r'.*[a]', container))

# ----------------------------------------

string = "Your phone number is (444)-888-2813, (231)-654-2813"

print(re.findall(r'[(]\d\d\d[)]-\d\d\d-\d\d\d\d', string))
print(re.findall(r'[(]\d+[)]-\d{3}-\d{4}', string))
print(re.findall(r'[(]\w{3}[)]-\w{3}-\w{4}', string))
print(re.findall(r'[(]\d{3}[)]-\d{3}-\d{4}', "".join(re.findall(r'[(].+', string))))

print("")

print(re.findall(r'\d+', string))
print(re.findall(r'\d{3,4}', string))

print("")

print(re.findall(r'[0-9a-zA-Z]{1,3}', string))

# ----------------------------------------

print("Here")

print("".join(re.findall(r'[^aeiouAEIOU]', string)))

# ----------------------------------------

string2 = "Aron, AAron, Arron, Eron, Eeron"

print(re.findall(r'[A-Z][a-z]*', string2))

# ----------------------------------------

name_age = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

names = re.findall(r'[A-Z][a-z]+', name_age)
ages = re.findall(r'\d{1,2}', name_age)

age_dictionary = {}

for name, age in zip(names, ages):
    age_dictionary[name] = age

print(age_dictionary)

# ----------------------------------------
print("")


def returner():
    return (word.span() for word in re.finditer(r'inform', "we need to inform him with the latest information"))


print(returner())

# --------------------------------------------------------------------------------

print("")

for i in re.findall(r'[a-zA-Z]at', "Sat, hat, mat, pat"):
    print(i)

print("")
to_edit = "Sat, rat, hat, mat, pat, karate"

print(re.sub(r', ', "\n", re.sub(r'[r]at', "food", to_edit)))

# --------------------------------------------------------------------------------

print("")

print(re.findall(r"\\", "This is a balc \\drogba"))

print("This is a test\t of v")

# --------------------------------------------------------------------------------

print(re.search(r'\w{2,20}\s\w{2,20}', "Oyebolu Dan"))

print(re.search(r'\w{1,25}[@]\w{1,25}[.](com|net|org)', "oyeboludaniel@gmail.net"))
print(re.findall(r'\w{1,25}[@]\w{1,25}[.][a-zA-Z]{2,3}', "oyeboludaniel@tech.io tantalize@nan.org"))


# --------------------------------------------------------------------------------

print(re.findall(r'^\s+|\s$', " apple, Banana, eon, can, ioen  "))

# --------------------------------------------------------------------------------

string3 = " This is another string. I guess so "

if re.findall(r'^(\s+)|(\s+)$', string3):
    string3 = re.sub(r'^\s+|\s+$', "",  string3)

# --------------------------------------------------------------------------------

print("After")

print(re.split(r'(\s+)', string3))


# --------------------------------------------------------------------------------
print("")
print("AfterAfter")
dictionary_three = {
    "This": "H",
    "is": "E",
    "another": "Y",
    "string": "J",
    "I": "U",
    "guess": "D",
    "so": "E"
}

print(string3.strip().split("   "))

print("")
print("Marker")
#print(' '.join(''.join(dictionary_three[letter] for letter in word.split(' ')) for word in string3.strip().split('   ')))

splitted = string3.strip().split("   ")
#print("Splitted:", splitted)

#for word in splitted:
#    word_split = word.split(" ")

contained = " This is another string. I guess so "
print(contained.strip())
#' '.join(''.join(dictionary_three[letter] for letter in word.split(' ')) for word in string3.strip().split('   '))


#print("Hello: ", "".join(item for item in string3.strip().split("   ")))
#print(string3.strip("").split("   "))

list_one = list("hhelloo")
list_one.pop(), list_one.pop(0)
print("".join(list_one))