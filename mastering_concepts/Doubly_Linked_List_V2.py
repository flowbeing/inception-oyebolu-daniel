class Node:

    def __init__(self, val, previous=None, next=None):
        self.val = val
        self.previous = previous
        self.next = next

    def get_val(self):
        return self.val

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def set_val(self, new_val):
        self.val = new_val

    def set_previous(self, new_previous):
        self.previous = new_previous

    def set_next(self, new_next):
        self.next = new_next


class DoublyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def prepend(self, val):
        new_node = Node(val)

        if self.head:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)

        self.head = new_node

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node

        elif self.head:
            current = self.head

            while current.get_next():
                current = current.get_next()

            current.set_next(new_node)
            new_node.set_previous(current)

    def get_size(self):
        current = self.head

        count = 0

        while current:
            count += 1
            current = current.get_next()

        print(f"The size of the linked list is {count}")

    def print(self):
        current = self.head

        hold = []

        while current:
            hold.append(current.get_val())
            current = current.get_next()

        print(f"{', '.join(item for item in hold)}")

    def delete(self, val):
        current = self.head

        previous = None

        while current:
            if current.get_val() == val:
                if current == self.head:
                    self.head = self.head.get_next()
                    current = current.get_next()

                elif current != self.head:
                    previous.set_next(current.get_next())
                    (current.get_next()).set_previous(previous)
                    current = current.get_next()

            if current.get_val() != val:
                previous = current
                current = current.get_next()

    def reverse_list(self):
        current = self.head

        previous = None

        while current:
            if previous is not None:
                previous.set_previous(current)

            nxt = current.get_next()
            current.set_next(previous)
            previous = current
            current = nxt

        previous.set_previous(None)

        self.head = previous


    def print_list(self):
        current = self.head

        while current:
            print(current.get_val())
            current = current.get_next()

    def print_next_and_previous(self):
        current = self.head

        while current:
            if current.get_previous() is None and current.get_next():
                print(f"previous: N val: {current.get_val()}  next: {(current.get_next()).get_val()}")

            elif current.get_previous() and current.get_next() is None:
                print(f"previous: {current.get_previous().get_val()} val: {current.get_val()}  next: N")
            else:
                print(f"previous: {(current.get_previous()).get_val()} val: {current.get_val()}  next: {(current.get_next()).get_val()}")

            current = current.get_next()





g = DoublyLinkedList()

g.prepend("a")
g.prepend("b")
g.prepend("c")
g.prepend("d")
g.prepend("e")

g.delete("e")

g.reverse_list()
g.print_list()

g.print_next_and_previous()
