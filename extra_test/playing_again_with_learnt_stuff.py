import string
hello = "This is the meaning"
#dictionary = hello.maketrans()

hold = ["a", "b", "c", "d", "3", 6, "d", "d", "d", "d", "d"]
xtem = [[i == ii] for i in hold for ii in hold]
ytem = [1, 4, 3, 8, 9]

print("\n".join(f"Is {x} equal to {y}? {str(x) == str(y)}" for x,y in zip(xtem,ytem)))

print(f"'{hello[:0]}'")

#print([i for item in xtem for i in item])

print([i for i in xtem].count([False]))

print(hold.index(6))

#print(hold[-5:-1:1])

holdr = ["a", "b", "c", "d", "3", 6, "d", "d", "d", "d", "d"]

while "d" in holdr:
    holdr.remove("d")

print(holdr)