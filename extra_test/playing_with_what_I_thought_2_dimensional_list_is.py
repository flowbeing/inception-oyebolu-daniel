list = []
for num in range(100):
    list.append(num + 1)

r1, r2 = 0, 5
count = 0

holdor = []

while r2 < len(list) + 1:
    # hold = []
    holdor.append([])

    for i in range(r1, r2):
        holdor[count].append(list[i])
        # hold.append(list[i])
    count += 1
    # print(hold)
    # print(f"{count:02}) {', '.join(f'{item:02}' for item in hold)}") useful for printing number outside of list
    # hold.clear()
    d = r2 - r1
    r1, r2 = r1 + d, r2 + d

count = 0
# print(f"{count:02}) {', '.join(f'{item:02}' for item in holdor)}")

# print("\n ".join(f"{i}" for i in holdor))

for num, i in enumerate(holdor, start=0):
    for num_two, ii in enumerate(holdor[num], start=0):
        holdor[num][num_two] = f"{ii:02}"
    print(f"{(num + 1):02}) {i}")

print(__name__)