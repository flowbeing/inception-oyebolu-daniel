query = input("Enter your ATM string. You may enter a different string as well: ")
query_list = list(query)

# Solution 1
if len(query) > 4:
    atm_details_holder = []
    for num, char in enumerate(query_list[0:4]):
        query_list[num] = "#"

print("".join(char for char in query_list))


# Solution 2
output = ""

for i in query[0:-4]:
    output += "#"
for i in query[-4:]:
    output += i

print(output)