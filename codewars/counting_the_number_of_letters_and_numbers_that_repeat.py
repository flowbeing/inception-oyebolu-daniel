string = "This is a string 235 235 string pzsosP"

def seek():
    return len([item for item in set("".join((string.lower().split()))) if string.lower().count(item) > 1])
    return len([item for item in set(string.lower()) if string.lower().count(item) > 1 and item != " "])


print(seek())