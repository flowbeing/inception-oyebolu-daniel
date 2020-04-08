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

    def __init__(self, vertices_list=None, arcs_list=None, edges_list=None):
        self.vertices_list = vertices_list
        self.arcs_list = arcs_list
        self.edges_list = edges_list
        self.stats = []
        self.time = 1
        
        if self.vertices_list is None:
            self.vertices_list = []

        self.vertices_to_id = {}
        self.weight = []
        self.neighbors = []

        if self.vertices_list is not None:
            for node in self.vertices_list:
                self.add_node(node)

        if self.arcs_list is not None:
            for name_u, name_v, weight in self.arcs_list:
                self.add_arc(name_u, name_v, weight)

        if self.edges_list is not None:
            for name_u, name_v, weight in self.edges_list:
                self.add_edge(name_u, name_v, weight)

    def add_node(self, u):
        if u not in self.vertices_list:
            self.vertices_list.append(u)

        if u not in self.vertices_list or (self.vertices_list is not None
                                        and u not in self.vertices_to_id): # Assuming that when self.node_list is not None,
                                                                        # its value is a list of graph nodes:
            self.vertices_to_id[u] = len(self.vertices_to_id)
            self.weight.append({})
            self.neighbors.append([])

        elif u in self.vertices_list or (self.vertices_list is not None and u in self.vertices_list):
            print(f"{u} is already a node in the graph!")

    def apply_uniform_spacing_(self, t):
        return (15 - len(t)) * " "

    def add_arc(self, name_u, name_v, weight=None):

        if name_u in self.vertices_list and name_v in self.vertices_list:
            u = self.vertices_to_id[name_u]
            v = self.vertices_to_id[name_v]

            if v not in self.neighbors[u]:
                self.neighbors[u].append(v)
                self.weight[u][v] = weight

            elif v in self.neighbors[u]:
                spacing = self.apply_uniform_spacing_(self.vertices_list[u])
                print(f"{self.vertices_list[u]}{spacing}-----> "
                      f"{self.vertices_list[v]} already exists.")

        elif name_u not in self.vertices_list:
            print(f"{name_u} is not a node in the graph!")
        elif name_v not in self.vertices_list:
            print(f"{name_v} is not a node in the graph!")

    def add_edge(self, name_u, name_v, weight=None):
        self.add_arc(name_u, name_v, weight)
        self.add_arc(name_v, name_u, weight)

    def execute_stats(self):
        self.stats = [["unexplored", 0, 0] for vertex in self.vertices_list]

    def _dfs(self, vertex):  # Made this myself... using the list method (self.stats) without class Vertex
        if vertex in self.vertices_list:
            vertex_index = self.vertices_to_id[vertex]
            self.stats[vertex_index][0] = "exploring"

            self.stats[vertex_index][1] = self.time
            self.time += 1

            for item in self.neighbors[vertex_index]:
                if self.stats[item][0] == "unexplored":
                    self._dfs(self.vertices_list[item])

            self.stats[vertex_index][0] = "explored"

            self.stats[vertex_index][2] = self.time
            self.time += 1

    def dfs(self, vertex):
        self.execute_stats()
        self._dfs(vertex)


    def print_graph(self):
        for num, item in enumerate(self.neighbors):
            print(f"{self.vertices_list[num]} {[self.vertices_list[i] for i in item]}  {self.stats[num][1]}/{self.stats[num][2]}")



nodes = list("abcdefghij".upper())

edges = [('B', 'C'), ('E', 'B'), ('C', 'I'), ('E', 'D'), ('I', 'E'), ('H', 'A'), ('J', 'I'), ('G', 'A'), ('D', 'F'), ('I', 'B')]

omnii = OmniGraph(nodes)

for a, b in edges:
    omnii.add_edge(a, b)



print("")
print(omnii.vertices_list)
print(omnii.vertices_to_id)
print(omnii.neighbors)
print(omnii.weight)
omnii.dfs("A")
omnii.dfs("B")

print(omnii.stats)
omnii.print_graph()