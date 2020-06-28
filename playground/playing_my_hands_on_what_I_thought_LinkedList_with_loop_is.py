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

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self, main_holder=None):
        self.main_holder = main_holder

    def add_node(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.main_holder)
        self.main_holder = new_node

    def size(self):
        current = self.main_holder

        counter = 0

        while current:
            counter += 1
            current = current.get_next_node()

        return counter

    # Great loop function according to my current knowings 28, Jan, 2020
    def loop_with_preferred_node_at_specific_node(self, node_to_use_as_loop, specific_node_where_loop_should_be):
        current = self.main_holder

        counter = 0
        size = self.size()
        loop_point = None


        while current:  # Might be slightly off.
            counter += 1
            print(f"Current node's data = {current.get_data()}")

            # The section below holds the node that will later serve as our last node and loop point
            if counter == node_to_use_as_loop:
                loop_point = current
                print(f"'{loop_point.get_data()}': This is the loop point. It becomes last node")
            elif counter == (specific_node_where_loop_should_be - 1):
                print(f'"{current.get_next_node()}": The point where loop is inserted')
                current.set_next_node(loop_point)
                print(f'"{current.get_next_node().get_data()}" has been converted to {loop_point.get_data()}')

            # The section below invalid arg values where the values are greater than the LinkedList's size
            if node_to_use_as_loop > size or specific_node_where_loop_should_be > size:
                return "You've entered an invalid value"

            current = current.get_next_node()


li = LinkedList()

li.add_node("fourteen")
li.add_node("thirteen")
li.add_node("twelve")
li.add_node("eleven")
li.add_node("ten")
li.add_node("nine")
li.add_node("eight")
li.add_node("seven")
li.add_node("six")
li.add_node("five")
li.add_node("four")
li.add_node("three")
li.add_node("two")
li.add_node("one")

print(li.loop_with_preferred_node_at_specific_node(4, 12))
