# hashing? assuming length of hash table is the total number of data to be input
# The essence of this software is to ensure that we detect collisions first hand when using the hashing method:
# key Mod n
# where key is the sum of the ascii values of characters in an input data and n is the length of the hash table
# We assume that string contains data to be stored separated by whitespace


get_ascii_num = {chr(i): i for i in range(128)}

#for i, value in enumerate(get_ascii_num):
#    print(i, str(value))


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList:

    def __init__(self, main_holder=None, value_holder=0):
        self.main_holder = main_holder
        self.value_holdor = value_holder

    def add_node(self, data):    # This method adds the sum of the ascii values of each character in a data to a node

        #print(data)
        data = sum([get_ascii_num[i] for i in data])

        new_node = Node(data)
        new_node.set_next_node(self.main_holder)
        self.main_holder = new_node

    def size(self):               # This method get the size of the LinkedList
        current = self.main_holder
        counter = 0

        while current:
            counter += 1
            current = current.get_next_node()

        return counter

    def get_hash_position(self):  # This method decides the position a data should be placed by dividing the sum of each
                                  # data's ascii decimal values by the total number of data to be stored. In some cases
                                  # it can be tweaked to ensure it is divided by
                                  # (total num of data to be stored * 10) / 7

        current = self.main_holder

        size = self.size()
        counter = 0
        detect_duplicates = []

        while current:
            counter += 1
            # print(current.get_data(), size)
            # print(f"{counter}.", current.get_data() % ((size * 10) / 7))
            #detect_duplicates.append(current.get_data() % size)
            detect_duplicates.append(current.get_data() % ((size * 10) / 7))
            #print(f"{counter:02}.", current.get_data() % size)
            current = current.get_next_node()


        total_collisions = sum([detect_duplicates.count(i) for i in set(detect_duplicates)
                            if detect_duplicates.count(i) > 1])

        print([{i: f"{detect_duplicates.count(i)} times"} for i in set(detect_duplicates)
               if detect_duplicates.count(i) > 1], f"Total collisions = {total_collisions}")


# Random 8 letter string generator
import string, random


def gen_eight_letter_str():
    return "".join([string.ascii_letters[random.randint(0, 51)] for i in range(3)])


li = LinkedList()
[li.add_node(gen_eight_letter_str()) for range in range(10)]
li.get_hash_position()