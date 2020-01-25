class Node:

    def __init__(self, data, next_container=None):
        self.data = data
        self.next_container = next_container

    def get_data(self):
        return self.data

    def get_next_container(self):
        return self.next_container

    def set_data(self, data):
        self.data = data

    def set_next_container(self, new_next_container):
        self.next_container = new_next_container


class LinkedList:

    def __init__(self, main_holder=None):
        self.main_holder = main_holder

    def add_node(self, data):
        new_node = Node(data)
        new_node.set_next_container(self.main_holder)
        self.main_holder = new_node

    def size(self):
        container = self.main_holder

        counter = 0

        while container:
            counter += 1
            container = container.get_next_container()

        return counter

    def print_values(self):
        container = self.main_holder

        values = []

        while container:
            values.append(container.get_data())
            container = container.get_next_container()

        if len(values) > 0:
            print(", ".join([str(value) for value in values]))
        elif len(values) == 0:
            print("There are no values in the LinkedList")


    def find_value(self, data):
        container = self.main_holder

        entry_number_locator = self.size()
        entry_number_list = []
        number_of_data_found = 0
        address = []

        while container:
            entry_number_locator -= 1
            if container.get_data() == data:
                entry_number_list.append(entry_number_locator)
                number_of_data_found += 1
                address.append(container)
                container = container.get_next_container()

            elif container.get_data != data:
                container = container.get_next_container()

        print("\n".join(f"The entered value was found as entry {entry_number} in node {str(node)}" for entry_number, node in
                        zip(entry_number_list[::-1], address[::-1])))

        print("")
        print(f"As summary, the entered value was found {number_of_data_found} times in the following nodes: " + "\n"
               + "\n".join(str(add) for add in address[::-1]))


li = LinkedList()
li.add_node("one")
li.add_node("two")
li.add_node("three")
li.add_node("four")
li.add_node("five")
li.add_node("three")

li.find_value("three")