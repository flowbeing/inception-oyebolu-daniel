class ContainerFactory:

    def __init__(self, bid, next_container=None):
        self.bid = bid
        self.next_container = next_container

    def get_bid(self):
        return self.bid

    def set_data(self, new_value):
        self.bid = new_value

    def get_next_container(self):
        return self.next_container

    def set_next_container(self, node_or_none):
        self.next_container = node_or_none

class ContainerOfContainers:

    def __init__(self, main_holder=None):
        self.main_holder = main_holder  # the self here serves as an extra layer hold\holder for the main_holder
                                        # Also, self.main_holder here serves as:
                                        # 1. the initial None value to be setas the second value of the first container
                                        # 2. the holder of the first and subsequent containers
                                        # 3. the holder of the item hat will serve as the next ingredient
                                        # It is the seed itself and it is the life itself
                                        # It basically give all nodes the ingredient for their lifes, next_container,
                                        # their yoke

    def contain_a_bid_and_a_box_if_any(self, bid):  # only bid is required here as we've got the extra ingredient for
                                                    # each container covered by self.main_holder
        new_container = ContainerFactory(bid)
        new_container.set_next_container(self.main_holder)
        self.main_holder = new_container


    def get_num_of_containers_or_nodes(self):
        container = self.main_holder        # it's not the literal self.main_holder or li.main_holder that's being
                                            # referred to here but the value of the self.main_holder or li.main_holder
                                            # i.e the mainly held itself\itthemselves

        count = 0
        while container:
            count += 1
            container = container.next_container  # here, the container is able to turn into the next_container

        return count

    def search_containers_for_value(self, data):            #   ADVANCED SEARCHER GIVEN TO ME
        container = self.main_holder

        count = self.get_num_of_containers_or_nodes()
        found = 0
        found_in = []

        while container:                                    ### Spectacular lesson : you can have an else statement with
            if container.get_bid() == data:                 ###
                print(f'Found data "{data}" in entry {count}')
                found += 1                                  ###
                found_in.append(str(container))
                container = container.get_next_container()
            else:                                           ###
                container = container.next_container        ###
            count -= 1

        return "Found " + str(found) + " in : \n" + " \n".join(found_in) if found > 0 else "Not in list"  ### an external return statement


    def delete_container(self, data):
        container = self.main_holder
        previous = None
        while container:
            if data == container.get_bid():
                if container == self.main_holder:
                    self.main_holder = container.get_next_container()

                elif container != self.main_holder:
                    previous.set_next_container(container.get_next_container())
                return container

            elif data != container.get_bid():
                previous = container
                container = container.get_next_container()
        return "none"


    def print_all_values(self):
        container = self.main_holder
        values = []

        while container:
            values.append(container.get_bid())
            container = container.get_next_container()

        return ", ".join([str(item) for item in values]) if values != [] else "There are no values in the LinkedList"


li = ContainerOfContainers()
li.contain_a_bid_and_a_box_if_any(1)
li.contain_a_bid_and_a_box_if_any(4)
li.contain_a_bid_and_a_box_if_any(2)
li.contain_a_bid_and_a_box_if_any(3)
li.contain_a_bid_and_a_box_if_any(4)
li.contain_a_bid_and_a_box_if_any(5)
print(li.search_containers_for_value(4), li.main_holder.next_container.next_container.next_container.get_bid()) #, li.main_holder.next_container.bid)
#print(f'self.main_holder = {li.main_holder.next_container.next_container.get_bid()}')
#li.delete_container(1)