class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class LinkedList:

    def __init__(self, main_holder=None):
        self.main_holder = main_holder

    def prepend(self, data):  # This adds a new node to the beginning of the linked list
        new_node = Node(data)
        new_node.set_next(self.main_holder)

        if self.main_holder is not None:
            self.main_holder.prev = new_node

        self.main_holder = new_node

    def append(self, data):  # This adds a new node to the end of the linked list
        current = self.main_holder

        new_node = Node(data)
        new_node.set_next(None)

        while current.get_next():
            current = current.next

        if current is None:
            new_node.set_prev(None)

        else:
            current.set_next(new_node)
            new_node.set_prev(current)

        # while current:
        #    if current is None:
        #        self.prepend(data)
        #        break

        #    if current.get_next() is None:
        #        new_node = Node(data)
        #        new_node.set_next(None)
        #        new_node.set_prev(current)
        #        current.set_next(new_node)
        #        break

        #    current = current.get_next()

    # This is to get the number of nodes in the linked list
    def size(self):
        current = self.main_holder

        count = 0

        while current:
            count += 1
            current = current.get_next()

        return f"The size of the LinkedList is {count}"

    # This is to reverse the linked list
    def reverse(self):
        current = self.main_holder

        hold = []
        size = int("".join(item for item in self.size() if item in "1234567890"))

        while current:
            hold.insert(0, current.get_data())
            current = current.get_next()

            if current.get_next() is None:
                hold.insert(0, current.get_data())
                break

        #print(hold)

        count = 0

        while current:
            count += 1
            current.set_data(hold[size - count])
            current = current.get_prev()



    def delete_node(self, data):  # used the brute-force approach i.e Checking through the linked list.
        current = self.main_holder

        prev_holder = None

        while current:

            if data == current.get_data():
                if current == self.main_holder:
                    self.main_holder = self.main_holder.get_next()
                    #self.main_holder.set_prev(None)
                    current = current.get_next()

                elif current != self.main_holder:
                    (current.get_prev()).set_next(current.get_next())
                    (current.get_next()).set_prev(current.get_prev())
                    current = current.get_next()

            elif data != current.get_data():
                current = current.get_next()

    def print(self):
        current = self.main_holder

        data = []

        while current:
            data.append(current.get_data())
            current = current.get_next()

        current = self.main_holder

        print("\n".join(f"{num}. {item}" for num, item in enumerate(data, start=1)))

    # This is to search through the linked list for specified data
    def search(self, data):
        current = self.main_holder

        found = 0
        nodes = []

        while current:
            if current.get_data() == data:
                found += 1
                nodes.append(str(current))

            current = current.get_next()

        return f"Found {found} in the following nodes:" \
               + "\n" + f"\n".join([node for node in nodes])


li = LinkedList()

li.prepend("three")
li.prepend("two")
li.prepend("one")
li.prepend("three")
li.append("four")
li.append("five")

#print(li.main_holder.next.next.next.prev.data)
#print(li.size())
li.reverse()
#li.print()
print(li.search("three"))
