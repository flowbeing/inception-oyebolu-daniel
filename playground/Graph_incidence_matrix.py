# IMPLEMENTATION OF INCIDENCE MATRIX IN PYTHON... MY STYLE. This was built from scratch from mind
# This is the incidence matrix representation of graph data structure.

# IT'S DYNAMIC. The program can work :
# a. When edge_size is not specified and vertex_list is not specified (You'd need to add vertices to the list)
# b. When edge_size is specified and vertex_list is specified

# When edge_size is specified and vertex_list is not specified. Make sure to add vertices before adding their
# corresponding edges.

# The representation allows for directed and undirected edges. It can contain and present both directed and undirected
# edges in a given representation.

# Directed graphs: +1 represents start point while 1 represents the endpoint.
# Undirected graphs: +1 is used to represent start point and endpoint.
# Edge here may mean directed edge or undirected edge.
# Where you enter the value for edge_size, make sure to enter input the vertex list.
# Before adding edges, make sure the vertex in the graph's vertex_list

# The challenge with the program is that:
# 1. After the to_String method is used, adding edges becomes non feasible.
# 2. Where edge size is specified for instance as two and two edges are added while the last one was later deleted with
#    the del_edge function, where the user adds a new edge, that edge won't get displayed when the to_String method is
#    applied

class Graph:

    def __init__(self, edge_size=None, vertex_list=None):
        self.edge_size = edge_size
        self.vertex_list = vertex_list
        self.vertex_to_num = {}
        self.in_matrix = []
        self.edge_counter = 0
        self.in_matrix_copy = self.in_matrix

        if self.edge_size and self.vertex_list is None:
            try:
                assert self.vertex_list
            except:
                print("You have entered the edge size without a vertex list! Please enter the vertex list or add "
                      "vertices manually!")

        if self.edge_size and self.vertex_list:  # this helps to plot the vertices against the edge size where both value
                                                 # of edge_size and vertex list above are entered
            for item in self.vertex_list:
                self.vertex_to_num[item] = len(self.vertex_to_num)
                self.in_matrix.append([0 for i in range(self.edge_size)])

        if self.edge_size is None and self.vertex_list:  # To create in matrix positions when there is self.edge_size
                                                         # but not self.vertex_list
            for item in vertex_list:
                self.vertex_to_num[item] = len(self.vertex_to_num)
                self.in_matrix.append([])

        if self.vertex_list is None:
            self.vertex_list = []


    def add_vertex(self, name_u):

        if name_u not in self.vertex_list:
            self.vertex_list.append(name_u)
            self.vertex_to_num[name_u] = len(self.vertex_to_num)

            if self.vertex_list and self.edge_size:
                self.in_matrix.append([0 for i in range(self.edge_size)])
            if self.vertex_list and self.edge_size is None: # This creates a space in the incidence matrix for a vertex
                                                            # where edge_size is not specified.
                self.in_matrix.append([])

        else:
            print(f'{name_u} is already a vertex in the list!')

    def add_edge(self, name_u, name_v, undirected=True):  # Adding of edge takes longer time than adjacency matrix.
                                                          # due to need to check if edge already exits in a horizontal
                                                          # manner

            # Stops the process of adding edges where the vertices specified are the same.
            if name_u == name_v:
                print("You've entered similar vertex names! Please enter non common vertex names.")
                return

            if name_u in self.vertex_to_num and name_v in self.vertex_to_num:   # To check if name_u and name_v in
                                                                                # self.vertex_to_num
                u = self.vertex_to_num[name_u]
                v = self.vertex_to_num[name_v]

            elif name_u not in self.vertex_to_num:
                print(f"Cannot add edge! {name_u} is not a vertex in the graph.x")
                return
            elif name_v not in self.vertex_to_num:
                print(f"Cannot add edge! {name_v} is not a vertex in the graph.x")
                return


            if self.vertex_list[u] == name_u and self.vertex_list[v] == name_v:  # To check if name_u and name_v are
                                                                                 # in self.vertex_list
                if self.edge_size and self.vertex_list: # if user has specified both edge size and vertex list or
                                                        # vertex list is not empty.
                    track = 0

                    if undirected:  # if edge are undirected...
                        # Check if the edge exists or not by looping through the lists in the index of u and v.
                        # if it exists, stop the edge addition process.
                        if (1, -1) in zip(self.in_matrix[u], self.in_matrix[v]) and (-1, 1) in zip(self.in_matrix[u],
                                                                                                   self.in_matrix[v]) \
                                or (1, 1) in zip(self.in_matrix[u], self.in_matrix[v]):
                            print(f"Edge {name_u} ----- {name_v} is already in list!")
                            return

                        # This is to loop through lists in the incidence matrix in the index of u and v
                        for (i, ii) in zip(self.in_matrix[u], self.in_matrix[v]):

                            # Where the edge is undirected, this will detect if a directed edge in either direction
                            # of the specified vertices already exists. Where it exists, a corresponding edge is added
                            # if it doesn't already exist.

                            val_one, val_two = 1, -1
                            if (i, ii) == (val_one, val_two):
                                print(f"Directed edge {name_u} -----> {name_v} was detected! "
                                      f"Inverse arc will be added")
                                self.add_edge(name_v, name_u, undirected=False)
                                return
                            if (i, ii) == (val_two, val_one):
                                print(f"Directed edge {name_v} -----> {name_u} was detected! "
                                      f"Inverse arc will be added.")
                                self.add_edge(name_u, name_v, undirected=False)
                                return

                            # Where undirected edge does not exist in each column of zip of lists in index of u and v,
                            # increase track by 1
                            if (i, ii) != (1, 1):
                                track += 1

                            # Where size of 'track' equals the edge size, this means the edge doesn't exist in
                            # the incidence matrix. In that case, add the edge into the matrix.
                            if track == self.edge_size:
                                self.in_matrix[u][self.edge_counter] = 1
                                self.in_matrix[v][self.edge_counter] = 1

                                self.edge_counter += 1
                                print(f"Edge {name_u} ----- {name_v} has been added.")
                                track = 0
                                return


                    # If the edge to be added is undirected...
                    elif not undirected:
                        # loop through the list in the incidence matrix in the index of u and v...
                        for (i, ii) in zip(self.in_matrix[u], self.in_matrix[v]):

                            # and if the directed edge or undirected edge of the specified vertices exist,
                            # let the user know.
                            if (i, ii) == (1, -1) or (i, ii) == (1, 1):
                                print(f"Edge {name_u} -----> {name_v} is already in list!")
                                return

                            # Where directed edge does not exist in each column of zip of lists in index of u and v,
                            # increase track by 1
                            if (i, ii) != (1, -1):
                                track += 1

                            # Where size of 'track' equals the edge size, this means the edge doesn't exist in
                            # the incidence matrix. In that case, add the edge into the matrix.
                            if track == self.edge_size:
                                self.in_matrix[u][self.edge_counter] = 1
                                self.in_matrix[v][self.edge_counter] = -1
                                self.edge_counter += 1

                                # This helps prevent errors where user specifies edge size but the edge_size spills over
                                # That is the edge size ends up being more than the specified edge size.
                                # *Take a look at this later*
                                if self.edge_size == self.edge_counter or self.edge_size < self.edge_counter:
                                    self.edge_size += 1

                                print(f"Edge {name_u} -----> {name_v} has been added.")
                                track = 0
                                return

                # If edge size wasn't specified and vertex list was specified...
                if self.edge_size is None and self.vertex_list:
                    track = 0

                    # if lists in incidence matrix in the index of u and v are both empty...
                    if not self.in_matrix[u] and not self.in_matrix[v]:
                        # where edge is undirected,
                        if undirected:

                            # append 0 to every other vertex that is not represented as name_u or name_v
                            for num, i in enumerate(self.in_matrix, start=0):   # }
                                if num != u and num != v:                       #  } TRYING TO UNDERSTAND THIS LOGIC
                                    self.in_matrix[num].append(0)               # }

                            # append 1 to vertex name_u and vertex name_v
                            self.in_matrix[u].append(1)
                            self.in_matrix[v].append(1)

                        # where the edge is undirected
                        if not undirected:

                            # append 0 to every other vertex that is not represented as name_u or name_v
                            for num, i in enumerate(self.in_matrix, start=0):
                                if num != u and num != v:
                                    self.in_matrix[num].append(0)

                            # append 1 to vertex name_u and -1 to vertex name_v respectively
                            self.in_matrix[u].append(1)
                            self.in_matrix[v].append(-1)

                    # if lists in incidence matrix  in the index of u and v are not empty...
                    elif self.in_matrix[u] and self.in_matrix[v]:
                        # if edge is undirected,
                        if undirected:
                            # loop through zip of lists in the incidence matrix in the index of u and v
                            for (i, ii) in zip(self.in_matrix[u], self.in_matrix[v]):
                                # stop the edge adding process where edge already exists in the incidence matrix.
                                if (i, ii) == (1, 1):
                                    print(f"Edge {name_u} ----- {name_v} is already in list!")
                                    return

                            # loop through zip of lists in the incidence matrix in the index of u and v
                            for (i, ii) in zip(self.in_matrix[u], self.in_matrix[v]):

                                # Where the edge is undirected, this will detect if a directed edge in either direction
                                # of the specified vertices already exists. Where it exists, a corresponding edge is added
                                # if it doesn't already exist.
                                val_one, val_two = 1, -1
                                if (i, ii) == (val_one, val_two):
                                    print(f"Directed edge {name_u} -----> {name_v} was detected! "
                                          f"Inverse arc will be added")
                                    self.add_edge(name_v, name_u, undirected=False)
                                    return
                                if (i, ii) == (val_two, val_one):
                                    print(f"Directed edge {name_v} -----> {name_u} was detected! "
                                          f"Inverse arc will be added.")
                                    self.add_edge(name_u, name_v, undirected=False)
                                    return

                                # Where undirected edge does not exist in each column of zip of lists
                                # in index of u and v increase track by 1.
                                if (i, ii) != (1, 1):
                                    track += 1

                                # Where size of 'track' equals the edge size, this means the edge doesn't exist in
                                # the incidence matrix. In that case, append 0 to all other vertices in the matrix that
                                # are not represented as name_u and name_v and add the edge into the matrix.
                                if track == len(self.in_matrix[u]) == len(self.in_matrix[v]):
                                    for num, i in enumerate(self.in_matrix):
                                        if num != u and num != v:
                                            self.in_matrix[num].append(0)
                                    self.in_matrix[u].append(1)
                                    self.in_matrix[v].append(1)

                                    # reset track for future additions of edges
                                    track = 0

                        if not undirected:
                            # Check if the edge exists or not by looping through the lists in the index of u and v.
                            # if it exists, stop the edge addition process.
                            if (1, -1) in zip(self.in_matrix[u], self.in_matrix[v]) or (1, 1) in zip(self.in_matrix[u],
                                                                                                     self.in_matrix[v]):
                                    print(f"Edge {name_u} -----> {name_v} is already in list!")
                                    return

                            # loop through the zip of the lists in the incidence matrix in the index of u and v
                            for (i, ii) in zip(self.in_matrix[u], self.in_matrix[v]):

                                # increase 'track' by 1 where column in zip of incidence matrix lists present in the index
                                # of u and v do not signify existence of edge
                                if (i, ii) != (1, -1) or (i, ii) != (1, 1):
                                    track += 1

                                # if size of 'track' equals the length of both incidence matrix list of name_u and
                                # name_v...
                                if track == len(self.in_matrix[u]) == len(self.in_matrix[v]):
                                    for num, i in enumerate(self.in_matrix):
                                        if num != u and num != v:

                                            # append 0 to all lists in the incidence matrix that are not represented
                                            # as name_u or name_v
                                            self.in_matrix[num].append(0)
                                    # append 1 to list represented as name_u or name_v
                                    self.in_matrix[u].append(1)
                                    self.in_matrix[v].append(-1)

                                    # reset track to 0 for future addition of edges
                                    track = 0


            elif self.vertex_list[u] != name_u:
                    print(f"There's an error with locating {name_u} in the vertex list")
                    return
            elif self.vertex_list[v] != name_v:
                    print(f"There's an error with locating {name_v} in the vertex list")
                    return


    def del_edge(self, name_u, name_v, edge_num):
        if name_u == name_v:
            print("You've entered similar vertex names! Please enter non common vertex names.")

        if name_u in self.vertex_to_num and name_v in self.vertex_to_num:   # To check if name_u and name_v in
                                                                            # self.vertex_to_num
            u = self.vertex_to_num[name_u]
            v = self.vertex_to_num[name_v]

        elif name_u not in self.vertex_to_num:
            print(f"Cannot add edge! {name_u} is not a vertex in the graph.x")
            return
        elif name_v not in self.vertex_to_num:
            print(f"Cannot add edge! {name_v} is not a vertex in the graph.x")
            return

        # Where the specified edge position i.e edge_num exists in the incidence matrix lists, delete it from lists
        # in the incidence matrix. That way, the edge and edge position gets deleted. *User should ensure that the edge
        # exists in the specified position. Otherwise, a different edge could be deleted*

        if self.in_matrix[u][edge_num - 1] and self.in_matrix[v][edge_num - 1]:
            for i in self.in_matrix:
                i.pop(edge_num - 1)

        else:
            print(f"The edge does not exist in the specified position! Check if the edge exists in a different position"
                  f"and try again.")


    def to_String(self):  # Converting the incidence matrix to physical format.
        hold_num = []

        longest = max(len(i) for i in self.vertex_list)

        for num in range(len(self.in_matrix[0])):
            hold_num.append(f"{(num + 1):02}")

        print(f"{' ' * (longest + 2)} {hold_num}")

        def extra_space(item_length):   # This calculates and determines the required space to display the vertices name
                                        # equally. The function is applied in line 353.
            if item_length < longest:
                difference = longest - item_length
                spacing = f" " * difference
                return spacing
            else:
                return ""

        # holdor is a pun gotten from GOT's 'holdoor' slang
        holdor = [item for item in self.in_matrix]

        # This converts integers in each list within incidence matrix into two letter string with 0 as the first
        # character where the length of the character is two
        for i in holdor:
            for ii in i:
                hold = i.pop(0)
                i.append(f"{hold:02}")

        # This adds the name of each vertex to each item in the incidence matrix
        for num, (vertex_name, i) in enumerate(zip(self.vertex_list, holdor)):
            holdor[num] = f"[{vertex_name}{extra_space(len(self.vertex_list[num]))}] {i}"

        # This code presents to the user the 2 dimensional representation that is the incidence matrix.
        for item in holdor:
            print(item)


v_list = ["one", "two", "three", "four", "five", "six"]

test = Graph(edge_size=2, vertex_list=v_list)
test.add_edge("one", "six", undirected=True)
test.add_edge("six", "one", undirected=False)
test.add_edge("four", "one")

test.to_String()