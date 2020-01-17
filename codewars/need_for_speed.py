# -------------------------------------------------------------------------------------------

print([title for (title, year) in list if year < 2000])

# Slower version : print([item[0] for item in list if list[list.index(item)][1] < 2000])

# -------------------------------------------------------------------------------------------

container = (((i, ii) for ii in range(5)) for i in range(5))
for i in container:
    for ii in i:
        print(ii)

# -------------------------------------------------------------------------------------------

