# In this graph implementation :
# 1. Node neighbors and weights are represented relative to the node id in a different data structure.
# 2. id first, name second.
# 3. Graph can accommodate both undirected and directed edges_list.
# 4. edge(s) refers to undirected edge(s).
# 5. arc(s) refers directed edge(s).
# 5a.edge(s) are represented with two arcs
# 6. Individual nodes have to be added before edges_list are added.
# 7. edge may or may not have weight

class OmniGraph:

    def __init__(self, nodes_list=None, arcs_list=None, edges_list=None):
        self.nodes_list = nodes_list
        self.arcs_list = arcs_list
        self.edges_list = edges_list

        if self.nodes_list is None:
            self.nodes_list = []

        self.nodes_to_id = {}
        self.weight = []
        self.neighbors = []

        if self.nodes_list is not None:
            for node in self.nodes_list:
                self.add_node(node)

        if self.arcs_list is not None:
            for name_u, name_v, weight in self.arcs_list:
                self.add_arc(name_u, name_v, weight)

        if self.edges_list is not None:
            for name_u, name_v, weight in self.edges_list:
                self.add_edge(name_u, name_v, weight)

    def add_node(self, u):
        if u not in self.nodes_list:
            self.nodes_list.append(u)

        if u not in self.nodes_list or (self.nodes_list is not None
                                        and u not in self.nodes_to_id): # Assuming that when self.node_list is not None,
                                                                        # its value is a list of graph nodes:
            self.nodes_to_id[u] = len(self.nodes_to_id)
            self.weight.append({})
            self.neighbors.append([])

        elif u in self.nodes_list or (self.nodes_list is not None and u in self.nodes_list):
            print(f"{u} is already a node in the graph!")

    def apply_uniform_spacing_(self, t):
        return (15 - len(t)) * " "

    def add_arc(self, name_u, name_v, weight=None):

        if name_u in self.nodes_list and name_v in self.nodes_list:
            u = self.nodes_to_id[name_u]
            v = self.nodes_to_id[name_v]

            if v not in self.neighbors[u]:
                self.neighbors[u].append(v)
                self.weight[u][v] = weight

            elif v in self.neighbors[u]:
                spacing = self.apply_uniform_spacing_(self.nodes_list[u])
                print(f"{self.nodes_list[u]}{spacing}-----> "
                      f"{self.nodes_list[v]} already exists.")

        elif name_u not in self.nodes_list:
            print(f"{name_u} is not a node in the graph!")
        elif name_v not in self.nodes_list:
            print(f"{name_v} is not a node in the graph!")

    def add_edge(self, name_u, name_v, weight=None):
        self.add_arc(name_u, name_v, weight)
        self.add_arc(name_v, name_u, weight)


nodes = ["Seattle", "San Francisco", "Los Angeles", "Denver", "Kansas City",
         "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston"]

edges = [("Seattle", "San Francisco", "19"), ("San Francisco", "Los Angeles", "15"), ("Seattle", "Denver", "18"),
         ("Seattle", "Atlanta", "118")]

omnii = OmniGraph(nodes, arcs_list=None, edges_list=edges)

print("")
print(omnii.nodes_list)
print(omnii.nodes_to_id)
print(omnii.neighbors)
print(omnii.weight)
