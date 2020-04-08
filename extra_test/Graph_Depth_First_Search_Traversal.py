class Vertex:

    def __init__(self, name):
        self.name = name
        self.neighbors = []

        self.start = 0
        self.finish = 0

        self.status = "unexplored"

    def add_neighbor(self, neighbor):
        if neighbor not in set(self.neighbors):
            self.neighbors.append(neighbor)
            self.neighbors.sort()
            #print(f"{neighbor} has been added as {self.name}'s neighbor")
            return True

        else:
            return False


class Graph:

    def __init__(self):
        self.vertices = {}
        self.time = 1

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
                if name_v not in self.vertices[name_u].neighbors:
                    self.vertices[name_u].add_neighbor(name_v)
                return True

        else:
            return False

    def dfs(self, vertex):  # making use of the Vertex class method without the self.stats list
        if vertex in self.vertices:

            self.vertices[vertex].status = "exploring"

            self.vertices[vertex].start = self.time
            self.time += 1

            for neighbor in self.vertices[vertex].neighbors:
                if self.vertices[neighbor].status == "unexplored":
                    self.dfs(neighbor)

            self.vertices[vertex].finish = self.time
            self.time += 1

            self.vertices[vertex].status = "fully_explored"

    def _dfs_iter(self, vertex):  # This is just a self trial test. Not yet perfected**
        if vertex in self.vertices:

            to_explore = [vertex]


            explored_tracker = []

            for item in self.vertices:
                explored_tracker.append([0 for i in self.vertices[item].neighbors])

            #exploring = []

            while to_explore:
                vertex_in_focus = to_explore.pop(0)
                #exploring.append(vertex_in_focus)
                self.vertices[vertex_in_focus].status = "exploring"

                self.vertices[vertex_in_focus].start = self.time
                self.time += 1

                position = 0

                for neighbor in self.vertices[vertex_in_focus].neighbors:

                    if self.vertices[neighbor].status == "unexplored":
                        to_explore.insert(position, neighbor)
                        position += 1

                position = 0





    def print_graph(self):

        for v in self.vertices:
            print(f"{v} {self.vertices[v].neighbors} {self.vertices[v].start}/{self.vertices[v].finish}")


graph = Graph()

for i in list("abcdefghij"):
    i = Vertex(i.upper())
    graph.add_vertex(i)

from random import randint

listed = list("abcdefghij".upper())

edges = []


def edges_generator():
    while len(edges) < 10:
        one = listed[randint(0, len(listed) - 1)]
        two = listed[randint(0, len(listed) - 1)]

        while one == two:
            two = listed[randint(0, len(listed) - 1)]

        if (one, two) not in edges and (two, one) not in edges:
            edges.append((one, two))


edges_generator()

#print(edges)

for a, b in edges:
    graph.add_edge(a, b)

#print(graph.vertices)
graph.dfs("B")
graph.print_graph()
