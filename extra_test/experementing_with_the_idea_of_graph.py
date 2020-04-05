e = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "D"),
     ("C", "A"), ("C", "D"), ("D", "B"), ("D", "C"),
     ("E", "C"), ("E", "D"), ("Z", "C")]


class DiGraph:

    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}

        for a, b in edges:
            self.add_edge_(a, b)

    def print_adj_list(self):
        print(self.adj_list)

    def print_nodes(self):
        nodes = []
        for node in self.adj_list:
            nodes.append(node)
        print(nodes)

    def print_neighbors(self, u):

        hold = []
        if u in self.adj_list:
            for item in self.adj_list[u]:
                hold.append(item)
        print(f'Neighboring nodes to {u} are {", ".join([i for i in hold])}')

    def print_graph_len(self):
        print(f"There are {len(self.adj_list)} nodes in the DiGraph")

    # def print_all_neighbors(self):
    #    print(f"List of neighbors in : {', '.join([i for item in self.adj_list.values() for i in item])}")

    def add_node(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge_(self, u=None, v=None):
        hold = [u, v]
        for item in hold:
            if item is not None and item not in self.adj_list:
                self.adj_list[item] = []
        #    [self.adj_list[item].append(i) for i in hold if i != item and i not in self.adj_list[item]]

        if v is not None and v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if v is not None and u not in self.adj_list[v]:
            self.adj_list[v].append(u)

        # for item in hold:

        # for i in hold:
        #    if i != item and i not in self.adj_list[item]:
        #        self.adj_list[item].append(i)

        # for item in hold:
        #    hold.append(hold.pop(0))
        #    if hold[0] not in self.adj_list[hold[1]]:
        #        self.adj_list[hold[1]].append(hold[0])


act_graph = DiGraph(e)

act_graph.add_edge_("X", "Z")
act_graph.add_node("Z")

act_graph.print_nodes()

act_graph.print_adj_list()

act_graph.print_neighbors("D")

act_graph.print_graph_len()


# for item in nodes:
#    print("")
#    print([i for i in nodes if i != item])

def return_no():
    return "It is none"


dictionair = {
}

dictionair["one"] = len(dictionair)
dictionair["two"] = len(dictionair)
dictionair["three"] = len(dictionair)
dictionair["four"] = len(dictionair)
print(dictionair)