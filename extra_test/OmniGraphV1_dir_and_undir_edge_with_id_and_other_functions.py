# In this graph implementation :
# 0. Graph can accommodate both undirected and directed edges.
# 1. edge(s) refers to undirected edge(s).
# 2. arc(s) refers directed edge(s).
# 2a.edge(s) are represented with two arcs
# 3. Individual nodes have to be added before edges are added.
# 4. Nodes have identifiers.
# 5. edge may or may not have weight.

class OmniGraph:

    def __init__(self, numtonodes=None, edges_list=None):
        self.adj_list = {}
        self.nodes_list = numtonodes
        self.nodes2num = {}  # This assigns identifiers to the nodes

        if numtonodes is not None:
            for node in numtonodes:
                self.adj_list[node] = {}

            for node in numtonodes:
                self.nodes2num[node] = len(self.nodes2num)

        elif numtonodes is None:
            self.nodes_list = []

        if edges_list is not None:
            for node_one, node_two in edges_list:
                self.add_edge(node_one, node_two)

    def get_id(self, u):
        if u in self.nodes_list:
            print(f"{u}'s id is {self.nodes2num[u]}")

    def numnodes(self):
        print(f"Graph's length is {len(self.adj_list)}")

    def numarc(self):
        count = 0
        for i in self.adj_list:
            count += len(self.adj_list[i])

        print(f"Graph contains {count} arc." if count < 2 else f"Graph contains {count} arcs.")

    def numedges(self):  #
        list_hold = self.adj_list
        count = 0

        for node in list_hold:
            for neighbor in list_hold[node]:
                if node in list_hold[neighbor]:
                    del[list_hold[neighbor][node]]
                    count += 1


        print(f"There are {count} edges in the list.")

    def get_neighbors(self, u):
        if u in self.adj_list:
            print(f"Neighbors of {u}: {', '.join((i for i in self.adj_list[u]))}")

    def get_neighbors_and_weights(self, u):
        if u in self.adj_list:
            print(f"Neighbors of {u} and their weights: {self.adj_list[u]}")

    def find_arc(self, u, v):
        #  First four lines can be simplified
        hold = [u, v]
        for item in hold:
            if self.find_node(item) is False:
                return

        if v in self.adj_list[u]:
            print("Found!")
        else:
            print("Arc is not in graph.")

    def find_edge(self, u, v):
        hold = [u, v]
        for item in hold:
            if self.find_node(item) is False:
                print("find_edge operation is not applicable.")
                return

        if v not in self.adj_list[u] and u not in self.adj_list[v]:
            print("Operation is not applicable."
                  "\nBoth items are not neighbors of one another.")
        elif v in self.adj_list[u] and u not in self.adj_list[v]:
            print(f"Only one arc found:" + "\n" + f"{u} -----> {v}." +
                  "\n" f"{v} -----> {u} not found!" +
                  "\nYou should use the find_arc method instead.")
        elif u in self.adj_list[v] and v not in self.adj_list[u]:
            print(f"Only one arc found:" + "\n" + f"{v} -----> {u}." +
                  "\n" f"{u} -----> {v} not found!" +
                  "\nYou should use the find_arc method instead.")

        elif v in self.adj_list[u] and u in self.adj_list[v]:
            print("Edge is in the graph.")

    def rm_arc(self, u, v):
        hold = [u, v]
        for item in hold:
            if self.find_node(item) is False:
                return

        del [self.adj_list[u][v]]

    def rmedge(self, u, v):
        hold = [u, v]
        for item in hold:
            if self.find_node(item) is False:
                return

        if self.find_node(u) is True and self.find_node(v) is True:
            if v not in self.adj_list[u] and u not in self.adj_list[v]:
                print("Operation is not applicable."
                      "\nBoth items are not neighbors of one another.")
            elif v in self.adj_list[u] and u not in self.adj_list[v]:
                print(f"Only one arc found:" + "\n" + f"{u} -----> {v}." +
                      "\n" f"{v} -----> {u} not found!" +
                      "\nYou should use the rm_arc method instead.")
            elif u in self.adj_list[v] and v not in self.adj_list[u]:
                print(f"Only one arc found:" + "\n" + f"{v} -----> {u}." +
                      "\n" f"{u} -----> {v} not found!" +
                      "\nYou should use the rm_arc method instead.")

            elif v in self.adj_list[u] and u in self.adj_list[v]:
                del [self.adj_list[u][v]]
                del [self.adj_list[v][u]]

    def add_node(self, u):
        if u not in self.adj_list:
            self.nodes_list.append(u)
            self.nodes2num[u] = len(self.nodes2num)
            self.adj_list[u] = {}
        else:
            print(f"{u} is already a node.")

    def find_node(self, u):
        if u in self.adj_list:
            print(f"Found! '{u}' is in the Graph with '{self.nodes2num[u]}' as its identifier." +
                  "\nIt's the " + f"{self.nodes2num[u] + 1}th node.")
            return True
        else:
            print(f"{u} is not a node in the graph.")
            return False

    def rmnode(self, u):
        if self.find_node(u) is False:
            return

        for i in self.adj_list[u]:
            if u in self.adj_list[i]:
                del [self.adj_list[i][u]]
        del [self.adj_list[u]]
        index_of_u = self.nodes_list.index(u)
        self.nodes_list.remove(u)
        del [self.nodes2num[u]]

        for node in self.nodes_list[index_of_u:]:
            self.nodes2num[node] = self.nodes_list.index(node)

    def add_arc(self, u, v, weight=None):
        # print("Note: add_arc will automatically add the nodes  you entered if they are not already in the graph")
        if u not in self.adj_list:
            # ans = input(f"{u} is not a node." +
            #            "\nWould you like to add it? "
            #            "\nYes | No : ")
            # if ans == "Yes":

            #self.add_node(u)

            print(f"{u} is not a node. Please enter a valid node to add arc.")
            return

        if v not in self.adj_list:
            # ans = input(f"{v} is not a node." +
            #            "\nWould you like to add it? "
            #            "\nYes | No : ")
            # if ans == "Yes":

            #self.add_node(v)

            print(f"{v} is not a node. Please enter a valid node to add arc.")
            return

        # if u in self.adj_list and v in self.adj_list and weight:
        if v in self.adj_list and u in self.adj_list and v not in self.adj_list[u]:
            self.adj_list[u][v] = weight
        # elif u in self.adj_list and v in self.adj_list and weight is None:
        # self.adj_list[u][v] = 1
        else:
            print(f"Arc: {u} ----> {v} already exists.")

    def add_edge(self, u, v, weight=None):  # Edges are represented as two arcs,
                                            # nodes must be in graph before edge will be created
        if v in self.adj_list and u in self.adj_list:
            self.add_arc(u, v, weight)

            # if u in self.adj_list and v in self.adj_list:
            self.add_arc(v, u, weight)
        elif v not in self.adj_list:
            print(f"{v} is not a node. Please enter a valid node to add edge.")
        elif u not in self.adj_list:
            print(f"{u} is not a node. Please enter a valid node to add edge.")
        elif v in self.adj_list[u] and u in self.adj_list[v]:
            print("Edge is already in graph.")

        # else:
        #    if u not in self.adj_list:
        #        print(f"Operation has failed because {u} is not a node in adjacency list")
        #    elif v not in self.adj_list:
        #        print(f"Operation failed because {v} is not a node in adjacency list")


nodes = ["Seattle", "San Francisco", "Los Angeles", "Denver", "Kansas City",
         "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston", ]

edges = [("Seattle", "San Francisco"), ("San Francisco", "Los Angeles"), ("Seattle", "Denver"), ("Seattle", "Atlanta")]

omni = OmniGraph(nodes, edges)

for num, val in enumerate(zip(omni.adj_list.keys(), omni.adj_list.values()), start=1):
    print(f"{num}.", val)

print("")
omni.numarc()

print("")
print(omni.nodes_list)
print(omni.nodes2num)
print(omni.adj_list)