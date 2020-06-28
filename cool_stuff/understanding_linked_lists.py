class ContainerFactory:

    def __init__(self, data, next_container=None):
        self.data = data
        self.next_container = next_container

    def get_data(self):
        return self.data

    def set_data(self, new_value):
        self.data = new_value

    def get_next_container(self):
        return self.next_container

    def set_next_container(self, node_or_none):
        self.next_container = node_or_none


class ContainerOfContainers:

    def __init__(self, main_holder=None):
        self.main_holder = main_holder  # the self here serves as an extra layer hold\holder for the main_holder
        # Also, self.main_holder here serves as:
        # 1. the initial None value to be set as the second value of the first container
        # 2. the holder of the first and subsequent containers
        # 3. the holder of the item hat will serve as the next ingredient
        # It is the seed itself and it is the life itself
        # It basically give all nodes the ingredient for their lifes, next_container,
        # their yoke

    def prepend(self, data):  # only data is required here as we've got the extra ingredient for
        # each container covered by self.main_holder
        new_container = ContainerFactory(data)
        new_container.set_next_container(self.main_holder)
        self.main_holder = new_container

    def size(self):
        container = self.main_holder  # it's not the literal self.main_holder or li.main_holder that's being
        # referred to here but the value of the self.main_holder or li.main_holder
        # i.e the mainly held itself\itthemselves

        count = 0
        while container:
            count += 1
            container = container.next_container  # here, the container is able to turn into the next_container

        return count

    def search(self, data):  # ADVANCED SEARCHER GIVEN TO ME
        container = self.main_holder

        count = self.size()
        found = 0
        found_in = []

        while container:  ### Spectacular lesson : you can have an else statement with
            if container.get_data() == data:  ###
                print(f'Found data "{data}" in entry {count}')
                found += 1  ###
                found_in.append(str(container))
                container = container.get_next_container()
            else:  ###
                container = container.next_container  ###
            count -= 1

        return "Found " + str(found) + " in : \n" + " \n".join(
            found_in) if found > 0 else "Not in list"  ### an external return statement

    def delete(self, data):
        container = self.main_holder
        previous = None
        while container:
            if data == container.get_data():
                if container == self.main_holder:
                    self.main_holder = container.get_next_container()

                elif container != self.main_holder:
                    previous.set_next_container(container.get_next_container())
                return container

            elif data != container.get_data():
                previous = container
                container = container.get_next_container()
        return "none"

    def reverse(self):

        container = self.main_holder

        previous = None

        while container:
            next_container = container.get_next_container()
            container.set_next_container(previous)
            previous = container
            container = next_container

        self.main_holder = previous


        #hold = []

        #while container:
        #    hold.insert(0, container.get_data())
        #    container = container.get_next_container()

        #container = self.main_holder
        #count = 0

        #while container:
        #    container.set_data(hold[count])

        #    container = container.get_next_container()
        #    count += 1


    def print(self):
        container = self.main_holder
        values = []

        while container:
            values.append(container.get_data())
            container = container.get_next_container()

        print(", ".join([str(item) for item in values]) if values != [] else "There are no values in the LinkedList")


li = ContainerOfContainers()
li.prepend("1")
li.prepend("2")
li.prepend("3")
li.prepend("4")
li.prepend("5")

# print(f'self.main_holder = {li.main_holder.next_container.next_container.get_data()}')
li.delete("3")
print(li.main_holder.next_container.next_container.data)

li.reverse()
li.print()