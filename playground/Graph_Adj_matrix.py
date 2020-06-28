# This adjacency matrix of graph allows for accommodation of both directed and undirected edges
# edge in this representation may refer to directed or undirected edge.
# names of vertices are required in list format

# COMPLETE APPLICATION OF NAMES OF ROW AND COLUMNS.
class Graph:

    def __init__(self, size_of_the_graph, name_of_vertices):
        self.size_of_graph = size_of_the_graph  #
        self.name_of_vertices = name_of_vertices  # Collects the names of the vertices. Useful in the toString method.
        self.adj_matrix = []  # collects the adj_matrix lists in one place.
        self.name_of_vertices_to_id = {}

        for num in range(size_of_the_graph):
            self.adj_matrix.append([0 for num_two in range(size_of_the_graph)])

        for name in self.name_of_vertices:
            self.name_of_vertices_to_id[name] = len(self.name_of_vertices_to_id)

    # User has to be very careful to ensure that both values 'u' and 'v' are in the graph, otherwise error(s) will
    # be raised. Also, user has to be correct on choice of whether edge is directed or not. Otherwise,
    # there is a good chance errors will be raised.
    def add_edge(self, name_u, name_v, undirected_edge=True):
        if name_u == name_v:
            print("name_u cannot be equal name_v")
            return
        u = self.name_of_vertices_to_id[name_u]
        v = self.name_of_vertices_to_id[name_v]

        if self.adj_matrix[u][v] > 0:
            print("Edge is already in list!")
            return
        self.adj_matrix[self.name_of_vertices_to_id[name_u]][self.name_of_vertices_to_id[name_v]] = 1
        if undirected_edge is True:  # freestyle
            self.adj_matrix[self.name_of_vertices_to_id[name_v]][self.name_of_vertices_to_id[name_u]] = 1
        else:
            return

    def rem_edge(self, u, v, undirected_edge):
        if u == v:
            print("Value of u cannot be equal to the value of v")
            return
        if self.adj_matrix[u][v] == 0:
            print("Edge is not in the list!")
            return

        self.adj_matrix[u][v] = 0
        if undirected_edge is True:
            self.adj_matrix[v][u] = 0
        else:
            return

    def contains_edge(self, u, v, undirected_edge=True):
        if u == v:
            print("Value of u cannot be equal to the value of v")
            return
        if undirected_edge is True:
            if v in self.adj_matrix[u] and u in self.adj_matrix[v]:
                print(f"{u} ----- {v} exists in the graph.")
            elif v not in self.adj_matrix[u] and u not in self.adj_matrix[v]:
                print(f"{u} ----- {v} is not in the graph.")
        if undirected_edge is False:
            if v in self.adj_matrix[u]:
                print(f"{u} -----> {v} exists in the graph.")
            elif v not in self.adj_matrix[u]:
                print(f"{u} -----> {v} is not in the graph.")

    def toString(self):
        print(f"       {name_of_vertices}")
        print(f'        {f"_" * ((len(name_of_vertices) + 2) * (int(len(name_of_vertices) / 2)))}')

        adj_matrix_two = self.adj_matrix[:]
        count = 0

        for num, i in enumerate(adj_matrix_two, start=0):
            for num_two, ii in enumerate(adj_matrix_two[num]):
               adj_matrix_two[num][num_two] = str(adj_matrix_two[num][num_two])
            adj_matrix_two[num] = f"{[self.name_of_vertices[count]]} | {adj_matrix_two[num]}"
            count += 1

        for i in adj_matrix_two:
            print(i)


name_of_vertices = list("abcdefghij")

graph = Graph(10, name_of_vertices)

graph.add_edge('a', "b")
graph.add_edge("b", "a")
graph.add_edge("a", "e")
graph.add_edge("b", "a")
graph.add_edge("b", "f")
graph.add_edge("c", "g")
graph.add_edge("d", "e")
graph.add_edge("d", "h")
graph.add_edge("e", "a")
graph.add_edge("e", "d")
graph.add_edge("e", "h")
graph.add_edge("f", "b")
graph.add_edge("f", "i")
graph.add_edge("f", "j")
graph.add_edge("g", "c")
graph.add_edge("g", "f")
graph.add_edge("g", "j")
graph.add_edge("h", "d")
graph.add_edge("h", "e")
graph.add_edge("h", "i")
graph.add_edge("i", "h")
graph.add_edge("i", "f")
graph.add_edge("j", "f")
graph.add_edge("j", "g")

graph.toString()

print()

for i in graph.adj_matrix:
    print(i)