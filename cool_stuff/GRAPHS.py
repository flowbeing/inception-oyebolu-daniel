# Program by Oyebolu Daniel

# The program can accommodate both directed and undirected graphs and makes use of two classes to implement the graph
# Issues may arise with BFS where levels in the graph is greater than 9999
# ARC refers to directed edge while EDGE refers to undirected edge
# DFS refers to DEPTH FIRST SEARCH while BFS refers to BREADTH FIRST SEARCH

from string import ascii_uppercase
from random import randint


class Vertex:

    def __init__(self, name):
        self.name = name  # This defines the name of an instance of the Vertex object
        self.neighbors = set()  # This contains neighbors of an instance of the Vertex object

        self.status = "unexplored"
        self.discovery_marker = 9999

        self.discovery_no = 0
        self.finish_no = 0

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.add(neighbor)
            return True
        else:
            return False


class Graph:

    def __init__(self):
        self.vertices = {}  # Holds the list of vertices and their corresponding node value

        # Holds the index number or id for each vertex. Allows for pin pointing locations in the adj_matrix
        self.vertices_2_num = {}

        # Holds the vertex which belings to each index number or id . Allows for pin pointing locations in the adj_matrix
        self.num_2_vertices = {}

        self.time = 1  # Used during DFS to determine the discovery and finish numbers.

        self.adj_matrix = []

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        elif isinstance(vertex, Vertex) and vertex.name in self.vertices:
            print(f"{vertex.name} is already in the graph!")
            return False
        elif not isinstance(vertex, Vertex):
            print(f"Make sure the value you entered as 'vertex' is a Vertex!")
            return False

    def add_arc(self, name_u, name_v):
        if name_u == name_v:
            print("Cannot add arc! Make sure to enter different values for the starting and endpoint.")

        elif not isinstance(name_u, str) or not isinstance(name_v, str):
            print("Cannot add arc!. One of the values you entered is not a vertex name.")
            return

        elif name_u in self.vertices and name_v in self.vertices:
            self.vertices[name_u].add_neighbor(name_v)

    def add_edge(self, name_u, name_v):
        self.add_arc(name_u, name_v)
        self.add_arc(name_v, name_u)

    def print_adj_list(self):
        for vertex in self.vertices:
            print(f"{vertex} {[neighbor for neighbor in self.vertices[vertex].neighbors]}")

    def _dfs(self, vertex_name):
        if not isinstance(vertex_name, str):
            print("Cannot perform dfs! The value you entered is not a vertex name.")

        elif isinstance(vertex_name, str) and vertex_name in self.vertices:
            self.vertices[vertex_name].status = "exploring"
            self.vertices[vertex_name].discovery_no = self.time

            self.time += 1

            for neighbor in self.vertices[vertex_name].neighbors:
                if self.vertices[neighbor].status == "unexplored":
                    self._dfs(neighbor)

            self.vertices[vertex_name].finish_no = self.time

            self.time += 1

            self.vertices[vertex_name].status = "explored"

    # User Interface for Depth First Search
    def dfs(self, vertex_name):
        self._dfs(vertex_name)
        self.time = 1

        # Resetting the vertex discovery status to 'unexplored' to prevent errors where the user evokes the dfs method
        # more than once
        for vertex in self.vertices:
            self.vertices[vertex].status = "unexplored"

    def print_dfs(self):
        for vertex in self.vertices:
            print(f"{vertex} {[neighbor for neighbor in self.vertices[vertex].neighbors]} "
                  f"{self.vertices[vertex].discovery_no}/{self.vertices[vertex].finish_no}")

    def _bfs(self, vertex_name):

        if vertex_name in self.vertices:

            queue = []

            self.vertices[vertex_name].status = "explored"
            self.vertices[vertex_name].discovery_marker = 0

            explored = [vertex_name]

            for neighbor in self.vertices[vertex_name].neighbors:
                self.vertices[neighbor].discovery_marker = 1

                queue.append(neighbor)

            while queue:

                vertex_in_focus = queue.pop(0)
                self.vertices[vertex_in_focus].status = "explored"

                for neighbor in self.vertices[vertex_in_focus].neighbors:

                    # The highlighted code below is slower.
                    # if self.vertices[neighbor].status == "unexplored" and neighbor not in queue:
                    #     self.vertices[neighbor].discovery_marker = self.vertices[vertex_in_focus].discovery_marker + 1
                    #     queue.append(neighbor)

                    if self.vertices[neighbor].status == "unexplored" and self.vertices[
                        neighbor].discovery_marker == 9999:
                        queue.append(neighbor)

                        self.vertices[neighbor].discovery_marker = self.vertices[vertex_in_focus].discovery_marker + 1

    def print_bfs(self):

        ordering = []

        for vertex in self.vertices:
            ordering.append(f"{self.vertices[vertex].discovery_marker} {vertex} "
                            f"{[n for n in self.vertices[vertex].neighbors]}")

        ordering.sort()
        for elem in ordering:
            print(elem)

    # Converting adj_list to adj_matrix
    def print_adj_matrix(self):
        self.vertices_2_num = {vertex_name: num for num, vertex_name in enumerate(self.vertices)}
        self.num_2_vertices = {num: vertex_name for num, vertex_name in enumerate(self.vertices)}

        for elem in self.vertices:
            self.adj_matrix.append([f"0" for elem in self.vertices])

            for el in self.vertices[elem].neighbors:
                self.adj_matrix[self.vertices_2_num[elem]][self.vertices_2_num[el]] = f"1"

        print(f"  {[elem for elem in self.vertices]}")

        for num, elem in enumerate(self.adj_matrix):
            print(f"{self.num_2_vertices[num]} {elem}")


graph = Graph()

# Adding vertices to the vertices list.
# for LETTER in ascii_uppercase[0:8]:
#     graph.add_vertex(Vertex(LETTER))

# Automatically adding edges to the graph.
# for num in range(7):
#     random_LETTER_I = ascii_uppercase[randint(0, (len(graph.vertices) - 1))]
#     random_LETTER_II = ascii_uppercase[randint(0, (len(graph.vertices) - 1))]

#     if random_LETTER_I != random_LETTER_II:
#         graph.add_edge(random_LETTER_I, random_LETTER_II)

# Adding vertices to the graph
for i in range(ord('A'), ord('K')):
    graph.add_vertex(Vertex(chr(i)))

# Adding edges to the graph.
# Note: Make sure to add vertices and edges to the graph before performing BFS and DFS
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.add_edge(edge[:1], edge[1:])

print("Adjacency list")
print("==============")
graph.print_adj_list()

print()

# Invoking depth First Search
graph.dfs("A")

print()

print("Depth First Search")
print("==================")

graph.print_dfs()

print()

# Invoking bfs
graph._bfs("A")

print("Breadth First Search")
print("====================")
graph.print_bfs()

print()

print("Adj_matrix")
print("==========")
graph.print_adj_matrix()


