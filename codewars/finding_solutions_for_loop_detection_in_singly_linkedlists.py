def loop_size(node):
    current = node

    length = 0
    node_list = []
    node_list_set = set()

    while current:
        # print(f"Current item = {current}")
        length += 1
        node_list.append(current)
        print(f"node_list = {node_list}")
        node_list_set.add(current)
        for item in node_list_set:
            if node_list.count(item) > 1:
                print("It worked")
                # return len(node_list[node_list.index(item):node_list[-1]:1])
                return (len(node_list) - 1) - node_list.index(item)
        current = current.next


def loop_size_two(node):
    current = node
    node_list = []

    while current:
        node_list.append(current)
        if node_list.count(current) > 1:
            return (len(node_list) - 1) - node_list.index(current)
        current = current.next


def loop_size_three(node):
    def loop_size(node):
        current = node
        length = 0
        node_list = []

        while current:
            length += 1
            if node_list.count(current) < 1:
                node_list.append(current)
                current = current.next
            else:
                break

        if length != length + 1:
            node_list.append(current)

        return (len(node_list) - 1) - node_list.index(current)


def loop_size_four(node):
    current = node
    node_list = []

    while current:
        node_list.append(current)
        if node_list.count(current) > 1:
            [node_list.pop(i) for i in range(node_list.index(current) + 1)[::-1]]
            return len(node_list)
            # return (len(node_list) - 1) - node_list.index(current)
        current = current.next


def loop_size_five(node):
    current = node
    node_list = []

    while current:
        node_list.append(current)
        if node_list.count(current) > 1:
            del [node_list[0:(node_list.index(current) + 1)]]
            return len(node_list)
            # return (len(node_list) - 1) - node_list.index(current)
        current = current.next


def loop_size(node):
    current = node
    node_list = ""

    while current:
        node_list += f"{str(current)} "
        if node_list.split().count(current) > 1:
            del [node_list[0:(node_list.index(current) + 1)]]
            return len(node_list)
            # return (len(node_list) - 1) - node_list.index(current)
        current = current.next