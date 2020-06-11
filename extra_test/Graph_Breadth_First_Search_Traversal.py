class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

        self.status = "unexplored"

        self.distance = 9999

    def add_neighbor(self, vertex):
        if vertex not in set(self.neighbors):
            self.neighbors.append(vertex)
            self.neighbors.sort()
            return True
        else:
            return False



class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, name_u, name_v, undirected=True):
        if name_u in self.vertices and name_v in self.vertices:
            if undirected:
                self.vertices[name_u].add_neighbor(name_v)
                self.vertices[name_v].add_neighbor(name_u)
                return True
            if not undirected:
                self.vertices[name_u].add_neighbor(name_v)
                return True

        else:
            return False

    def bfs(self, vertex):
        if vertex in self.vertices:
            vertex_node = self.vertices[vertex]
            vertex_node.distance = 0
            vertex_node.status = "explored"

            to_be_explored = []

            for n in vertex_node.neighbors:
                self.vertices[n].distance = vertex_node.distance + 1
                to_be_explored.append(n)

            while to_be_explored:
                u = to_be_explored.pop(0)
                self.vertices[u].status = "explored"

                for v in self.vertices[u].neighbors:
                    if self.vertices[v].status == "unexplored":
                        to_be_explored.append(v)
                        if self.vertices[v].distance > self.vertices[u].distance:
                            self.vertices[v].distance = self.vertices[u].distance + 1

    def reset_attr(self):   # To reset value of attributes "distance" and "status"
        for vertexx in self.vertices:
            self.vertices[vertexx].distance = 9999
            self.vertices[vertexx].status = "unexplored"



    def print_graph(self):
        holdor = []
        for vertex in self.vertices:
            holdor.append([self.vertices[vertex].distance, f"{vertex}{self.vertices[vertex].neighbors} "])
        holdor.sort()

        for a, b in holdor[::-1]:
            print(a, b)

    def bfs_two(self, vertex):  # I devised this.
        if vertex in self.vertices:
            vertex_node = self.vertices[vertex]
            vertex_node.distance = 0

            to_be_explored = [vertex]

            while to_be_explored:
                u = to_be_explored.pop(0)
                node_u = self.vertices[u]

                if u != vertex and u in vertex_node.neighbors:
                    node_u.distance = vertex_node.distance + 1

                node_u.status = "explored"

                for v in node_u.neighbors:
                    if self.vertices[v].status == "unexplored":
                        to_be_explored.append(v)
                        if self.vertices[v].distance > node_u.distance:
                            self.vertices[v].distance = node_u.distance + 1




g = Graph()
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs("A")
g.print_graph()

g.reset_attr()
print("")

# print(g.vertices["A"].status)
# g.bfs_two("A")
# g.print_graph()

print("")

# for vertex in g.vertices:
#     print(f"{vertex} {g.vertices[vertex].neighbors}")
