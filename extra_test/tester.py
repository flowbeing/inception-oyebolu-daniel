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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.main_holder

        if self.main_holder is not None:
            self.main_holder.prev = new_node

        self.main_holder = new_node

    def append(self, data):
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

    def size(self):
        current = self.main_holder

        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def reverse(self):
        current = self.main_holder

        hold = []
        size = self.size()

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



    def delete_node(self, data):  # used the brute-force approach
        current = self.main_holder

        prev_holder = None

        while current:

            if data == current.get_data():
                if current == self.main_holder:
                    self.main_holder = self.main_holder.get_next()
                    self.main_holder.set_prev(None)
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

        print("\n".join(f"{num}. {item}" for num, item in enumerate(data, start=1)))


li = LinkedList()

li.prepend("three")
li.prepend("two")
li.prepend("one")
li.append("four")
li.append("five")

#print(li.main_holder.next.next.next.prev.data)
#print(li.size())
li.reverse()
li.print()
