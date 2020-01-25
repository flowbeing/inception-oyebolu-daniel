class Person:

    def __init__(self, name, age, address, robot_owned=None, is_looking_at=None):
        self.name = name
        self.age = age
        self.address = address
        self.robot_owned = robot_owned
        self.is_looking_at = is_looking_at

    def introduce_yourself(self):
        if self.robot_owned is None:
            print(f"Hi, my name is {self.name}. I am {self.age} years old and I live at {self.address}")
        elif self.robot_owned is not None:
            print(f"Hi, my name is {self.name}. I am {self.age} years old and I live at {self.address}\n"
                  f"Also, you should know that daniel owns an {self.robot_owned} robot.")

    def is_looking_at_who(self):
        if self.is_looking_at is not None and self.is_looking_at[0] == True:
            print(f'{self.name} is looking at {self.is_looking_at[1]}')
        else:
            print(f"{self.name} is not looking at anyone or anything")


Dann = Person("Dann", 21, "4, Talitakumi street,", robot_owned=None)
Dan = Person("Daniel", 12, "2, Bami Oye, Olomo", "r2", (True))

Dan.introduce_yourself()
Dann.is_looking_at_who()

print(Dann.age)

# ---------------------------------------------------------------------------------------------------------

set_one = {1, 2, 3, 4, 5, 6}
print(set_one.pop())

if set_one:
    print("yay")

elif not set_one:
    print("nay")

# -----------------------------------

import array as arr

# -----------------------------------

a = {
    "1": 1,
    2: 3,
    4: 5,
    6: 7}

# del a[1]
print("", a.pop("1"))
c = a.popitem()
print(a)
print([(a, b) for a in c for b in c])
print(a.popitem())
print(a)

# -----------------------------------
import collections as c

que = c.deque(["1", "2", "3", "4", 5])
print("Que", que.popleft())
print(que)

# -----------------------------------
ar = arr.array("i", [1, 2, 3, 4, 5])
ar.pop(1)
print(ar)


# -----------------------------------

listed = [[1, 2], [3, 4, 5]]
print([num for item in listed for num in item])

from math import pi
print(-3//2)

object