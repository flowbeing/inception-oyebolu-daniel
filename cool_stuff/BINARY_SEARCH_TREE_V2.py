# Binary Search Tree By Oyebolu Daniel
# BST refers to Binary Search Tree

class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val  # Holds a node's value
        self.left = left  # Holds the value in a node on the left
        self.right = right  # Holds the value in a node on the right

        self.address_tracker = ["root"]  # It helps get the address of a node. It also helps track the level a value is
                                   # in. In addition, it helps pinpoint the deepest level when the number of items it 
                                   # contains is greater than the number of item in self.deepest_level_tracker

        self.deepest_level_tracker = []  # This signifies the total number of levels in the Binary Search Tree

        self.geometric_series = []   # geometric series consists of max number of items each BST level can contain.

        self.model_list = []  # The aim of this is to present the BST in a one dimensional format from which the visual
                              # two dimensional tree will is devised.

        self.traversal_no_tracker = 0  # this variable was created to effectively account for absent values in the BST

    # Method to retrieve the value in a node.
    def get_val(self):
        return self.val

    # Method to retrieve the value in a node on the left hand side.
    def get_left(self):
        return self.left

    # Method to get the value in a node on the right hand side.
    def get_right(self):
        return self.right

    # Method to set or reset the value in a node.
    def set_val(self, new_val):
        self.val = new_val

    # Method to set or reset the value in a node on the left hand side.
    def set_left(self, new_left):
        self.left = new_left

    # Method to set or reset the value in a node on the left hand side.
    def set_right(self, new_right):
        self.right = new_right

    # This method gets the number of levels a BST
    def _get_no_of_levels_dfs(self, node):

        # This helps track the furthest (deepest) level in the BST.
            # If the length of the address tracker is 1 i.e if it contains only "root" and in summary, the deepest
            # _level tracker is empty ...
        if len(self.address_tracker) == 1 and len(self.address_tracker) > len(self.deepest_level_tracker):
            # ... add "root" to self.deepest level tracker
            self.deepest_level_tracker.append(self.address_tracker[0])

        # If the current node has a left child...
        if node.left:
            # ... append "left" to the address tracker
            self.address_tracker.append("left")

            # if the number of contents in the address tracker is now greater than the number of contents in the deepest
            # level tracker...
            if len(self.address_tracker) > len(self.deepest_level_tracker):
                # ... make the contents of the deepest level tracker equal to that of the address tracker
                self.deepest_level_tracker.clear()
                for item in self.address_tracker:
                    self.deepest_level_tracker.append(item)

            # Now, apply the _get_no_of_levels_dfs method on the left node.
            self._get_no_of_levels_dfs(node.left)

        # If the current node has a left child...
        if node.right:
            # ... append "left" to the address tracker
            self.address_tracker.append("right")

            # if the number of contents in the address tracker is now greater than the number of contents in the deepest
            # level tracker...
            if len(self.address_tracker) > len(self.deepest_level_tracker):
                # ... make the contents of the deepest level tracker equal to that of the address tracker
                self.deepest_level_tracker.clear()
                for item in self.address_tracker:
                    self.deepest_level_tracker.append(item)

            # Now, apply the _get_no_of_levels_dfs method on the left node.
            self._get_no_of_levels_dfs(node.right)

        # This ensures that the address represented in the address tracker is correct for every node when the current
        # _get_no_of_levels_dfs process in python's stack has been completed. By deleting the last item in the address
        # tracker, we are left with the address of the node being treated within the previous _get_no_of_levels_dfs
        # process in python's stack.
        # Note that when the _get_no_of_levels_dfs method is completed for all  the nodes in the BST, the first item
        # in the address tracker "root" will be deleted due to the code below. It will be later be added using in the
        # get_no_of_levels_dfs interface
            # Delete the last string | item in the address tracker.
        self.address_tracker.pop()

    # This serves as the user interface for the _get_no_of_levels_dfs method
    def get_no_of_levels_dfs(self, node):
        self._get_no_of_levels_dfs(node)

        # This adds "root" if it was previously deleted while running the _get_no_of_levels_dfs method
        if "root" not in self.address_tracker:
            self.address_tracker.append("root")

        # By getting the length of self.deepest_level after running self._get_no_of_levels_dfs, we are able to determine
        # number of levels in the BST
        deepest_level = len(self.deepest_level_tracker)

        print(f"The number of levels in the BST is {deepest_level}.")


    # This helps populate the model list with values in the BST.
    # The model list serves as a container of all values the BST holds or can hold i.e dots. Dot(.) represents positions
    # in the BST that can hold a value but are empty. In this method, we have to account for the dots.
    def inorder_traversal(self, node):

        # If there is a left node ...
        if node.left:
            # ... append left to address tracker and run the inorder_traversal method on the left node
            self.address_tracker.append("left")
            self.inorder_traversal(node.left)

        # if there isn't a left node, it and its children - if any - have to be accounted so we may know the correct
        # number of the next node to be visited.
            # else if there isn't a left node ...
        elif not node.left:
            # Calculate the number of levels to the deepest level first. This helps know how many levels were affected.
            # We do this by how much difference exists between the deepest level and the current level.
            levels_to_deepest_level = len(self.deepest_level_tracker) - len(self.address_tracker)

            # Get the number of nodes levels_to_deepest_level can accomodate. We can calculate this by summing the first
            # 'level_to_deepest_level' items in the geometric series since the series contains max number of nodes each
            # level can contain in chronological order.
            no_of_absent_nodes = sum(self.geometric_series[0:levels_to_deepest_level])
            # Increment the traversal number tracker with the number of absent nodes
            self.traversal_no_tracker += no_of_absent_nodes



        # What were doing now is converting some of the dots to values where values exist for the dot's position.
        # Note that the model list has already been populated with dots for the total number items the BST can contain
        self.model_list[self.traversal_no_tracker] = node.get_val()

        # Increment traversal number tracker by one so we may focus on and account for the next value in the model list.
        self.traversal_no_tracker += 1



        # If there is a right node ...
        if node.right:
            # ... append right to address tracker and run the inorder_traversal method on the right node
            self.address_tracker.append("right")
            self.inorder_traversal(node.right)

        # if there isn't a right node, it and its children - if any - have to be accounted so we may know the correct
        # number of the next node to be visited.
        # else if there isn't a right node ...
        elif not node.right:
            # Calculate the number of levels to the deepest level first. This helps know how many levels were affected.
            # Again, we do this by how much difference exists between the deepest level and the current level.
            levels_to_deepest_level = len(self.deepest_level_tracker) - len(self.address_tracker)

            # Get the number of nodes levels_to_deepest_level can accomodate. We can calculate this by summing the first
            # 'level_to_deepest_level' items in the geometric series since the series contains max number of nodes each
            # level can contain in chronological order.
            no_of_absent_nodes = sum(self.geometric_series[0:levels_to_deepest_level])

            # Increment traversal number tracker by one so we may focus on and account for the next value in the model
            # list
            self.traversal_no_tracker += no_of_absent_nodes


        # This ensures that the address represented in the address tracker is correct for every node when the current
        # inorder_traversal process in python's stack has been completed. By deleting the last item in the address
        # tracker, we are left with the address of the node being treated within the previous inorder_traversal process
        # in python's stack.
        # Note that when the inorder_traversal method is completed for all  the nodes in the BST, the first item
        # in the address tracker "root" will be deleted due to the code below. It will be later be added in the
        # construct_bst interface.
        # Delete the last string | item in the address tracker.
        self.address_tracker.pop()

    def construct_bst(self, node):

        # Get the number of levels in the BST
        self.get_no_of_levels_dfs(node)

        # Calculating the items in the geometric series consisting of max number of items each BST level can contain
            # a * (r**(n - 1))
            # a = first in the geometric series consisting of max number of items each BST level can contain
            # r = is the multiplier factor
            # n = number of levels in the BST
        deepest_level = len(self.deepest_level_tracker)

            # for each level present in the BST...
        for num in range(deepest_level):
            # ... calculate the number of item the level can contain using the geometric series formula above ...
            series_item = 1 * (2 ** ((deepest_level - (deepest_level - (num)))))
            # ... and append it to the geometric series list.
            self.geometric_series.append(series_item)

        # 'max_items' equals the total number of values the BST can contain.
        max_items = sum(self.geometric_series)
        print(f"Maximum number of items the BST can hold = {max_items}")

        
        # Generating the model list and indices both of which symbolise each item in the BST and their position.
        self.model_list = []
        self.index_of_model_list = []  # This later on allows for tracking the position of dot('.') that has been added
                                       # to the tree_construct. The list helps to avoid the issue of same index for 
                                       # different dots in the list.

        # Populate the model list with dots
        for num in range(max_items):
            self.model_list.append(".")
            self.index_of_model_list.append(num)

        # self.traversal_no_tracker = 0

        # Populate the model list with values in the BST using inorder_traversal.
        self.inorder_traversal(node)


        # Restore "root" which was previously deleted while running self.inorder_traversal method
        self.address_tracker.append("root")

        # GETTING THE VALUES IN EACH LEVEL

        tree_construct = []  # tree_construct is a list within which the BST's visuals will be built and printed in 2D.
        track_added = []  # To track items other than dots('.') in the BST that have been added to the tree_construct.
        track_dots_added = []  # To track dots('.') that have been added to the tree_construct.


            # Populate the tree_construct with list objects that represent levels in the BST
        for level in range(deepest_level):
            tree_construct.append([])

            # Each value in the reverse of self.geometric_series serves as effective factors for tracking
            # the values in each level of the BST starting from the least level.
        for num, value in enumerate(self.geometric_series[::-1]):
            pin_point = value
            
            # A value to be increased by the value of 'pinpoint' in the while loop below where the condition remains
            # valid in order to aid the tracking of each value in each level
            new_pinpoint = pin_point


            # While new_pinpoint is not greater than the length of the maximum number of item the BST can hold...
            while new_pinpoint < len(self.model_list) + 1:

                # Make value_to_be_added equal the value to be appended to a level in the tree_construct.
                value_to_be_added = self.model_list[new_pinpoint - 1]

                # Due to errors from figuring out and working with the index of different dots in the self.model_list,
                # index_of_dot helps to know accurately the index of each dot in the model list by looking through the
                # index_of_model_list.
                index_of_dot = new_pinpoint - 1

                # If the value to be added into a level in the tree construct has not already been added or if the
                # value to be added into a level in the tree construct is a dot i.e "." ... 
                if value_to_be_added not in track_added or value_to_be_added == ".":
                    
                    # ... if the value is not a dot ".", add it to the concerned level in the tree construct
                    # in a list format

                    if value_to_be_added != ".":
                        tree_construct[num].append([value_to_be_added])

                    # The else statement below is to solve the issue of similar indices faced while trying to determine
                    # the index of different dots in the self.model_list using self.model_list.index(".")

                    # ...if the value to be added is a dot and its index signified by index_of_dot is in the
                    # index_of_model_list, it means the dot in that index has not been added to the tree construct.
                    # Therefore, add it to the concerned level in the tree construct and remove the dot's
                    # index from the index_of_model_list.

                    else:
                        if index_of_dot in self.index_of_model_list:
                            tree_construct[num].append([value_to_be_added])
                            self.index_of_model_list.remove(index_of_dot)


                # Add the value to be added to the list of added values and dots.
                # This way, we are able to know in the next loop that the value was previously added and doesn't
                # need to be added to the tree structure again.
                track_added.append(value_to_be_added)

                # As earlier mentioned, new_pinpoint will be increased by the value of pin_point in order to have a
                # precursor for tracking the next value or dot in a level.
                new_pinpoint += pin_point

        # Depopulate and repoplulate index_of_model_list with index of each item in the model list.
        self.index_of_model_list.clear()

        for num, value in enumerate(self.model_list):
            self.index_of_model_list.append(num)



        # ADDING LEFT AND RIGHT PADDING TO BST ITEMS | proper formatting to the tree_construct

            # factor below was created to serve as a user defined integer that determines the extent to
            # which 'extra_padding_if_any' adds extra left and right padding to elements / items in different levels of the BST
        factor = 2


            # Containing values, potential or actual, and their indices using a generator
        bst_items_and_their_indices = []

        for x, y in zip(self.model_list, self.index_of_model_list):
            bst_items_and_their_indices.append([x, y])


            # Accounting for increase in lower level spacing
            # Walking up the BST levels, we notice that as the levels in the BST decrease, for each
            # item in a lower level, the spacing required to center such an item against items directly below it in the
            # higher level is equal to the number of items directly below it down to the deepest level.

            # It is in this moment we account for increase in left and right spacing required for item(s) in each level
            # while considering each level in descending order.
            # By reversing the geometric series list, decreasing each of its values by 1 and choosing each item in order
            # of its corresponding level, we are able to adequately represent the increase in left and right padding
            # required for items in a lower level.
        normal_padding = [] # i.e lower level padding

        for max_content_of_level in self.geometric_series[::-1]:
            normal_padding.append(max_content_of_level - 1)


        # The loops below implement the left and right padding  of elements in the BST, for which the variables above
        # where setup for.

        # Go through each level in the BST and the items (values and dots) they hold...
        for level, construct in enumerate(tree_construct):
            for num, value in enumerate(construct):

                # Due to the fact that spacing required for each item in a lower level is higher than that in an
                # immediately higher level, padding_length was created to indicate that fact by using items in the
                # geometric series rightly.

                padding_length = (self.geometric_series[::-1][level])
                extra_padding_if_any = " " * padding_length * factor

                # If the level is the last level in the BST, add extra_padding_if_any without accounting for
                # normal_padding since the level doesn't have items in a lower level below it tht have to be accounted
                # for.
                if level == len(tree_construct) - 1:
                    value.insert(0, extra_padding_if_any)
                    value.append(extra_padding_if_any)

                # If the level is not the last level in the BST, it has a level higher than itself, therefore add
                # extra_padding_if_any as calculated above to the concerned item (value or dot) and account for all the items
                # directly below it in the BST using normal_padding.
                else:
                    value.insert(0, (" " * (normal_padding[level])) + extra_padding_if_any)
                    value.append((" " * (normal_padding[level])) + extra_padding_if_any)


                tree_construct[level][num] = "".join(item for item in value)

            tree_construct[level] = " ".join(item for item in tree_construct[level])

        print("")


        # AESTHETICALLY PRESENTING THE BST TO THE USER
            # This section is meant to center the levels in the tree against the deepest level so that the visual
            # presentation of the tree may be as pleasing to the user's eyes as possible

        title = "B I N A R Y  S E A R C H  T R E E"

            # Determine the number of characters in the deepest level and subtract the number of characters in the
            # 'title' from it, afterwards splitting the difference two ways. By spllitting the difference, the left and
            # right padding needed to center the title is determined.

        diff = int((len(tree_construct[-1]) - (len(title))))
        _padding = (diff / 2)

            # Padding required for centering the title after accounting for presentation of "Lvl' below
        padding = int(_padding + 3) * " "


            # Applying calculated padding to the title and it's underlining text
        print(padding + "B I N A R Y  S E A R C H  T R E E")
        print(padding + "=================================")
        print(padding + "     Author : Oyebolu Daniel     ")
        print(padding + "       github.com/satonoti       ")
        #print(padding + "         =================       ")


        # Creating the levelpresentation area
            # The left level title plus center space, calculated using the length of the deepest item, plus the right
            # level title
        print("Lvl" + (" " * len(tree_construct[-1])) + "Lvl")
        print("===" + (" " * len(tree_construct[-1])) + "===")

            # This algorithm presents each level in descending order while indicating the number of the level
        for num, level in enumerate(tree_construct):
            print(f"{(num + 1):03}{level}{(num + 1):03}")

            # Applying spacing between level
            # if the level in focus is the first level in the GST, add a one line space between it and the second level.
            if num == 0:
                for num in range(1):
                    print("")

            # if the level is not the first level or the last level, add spacing between it and the next level according
            # to the extent defined by the total amount of numbers preceding the level's index (in the tree_construct)
            # starting fom zero
            elif num != 0 and num != (len(tree_construct) - 1):
                for num in range(num):
                    print("")





class BST:

    def __init__(self, root=None):
        self.root = root

    # Method to add a node to the BST.
    # Note that each node holds a alue
    def add_node(self, val):
        new_node = Node(val)


        # if there is no node in the BST, make the newly created node the root node ...
        if not self.root:
            self.root = new_node

        # Otherwise, go through the BST and determine where to place the value
        else:
            self._add_node(self.root, val)

    # This method was devised cos I didn't want to put the method in the Node class
    # The method goes through the BST to determine the appropriate location to place the value
    def _add_node(self, node, val):

        # If the current node value is equal to the value to be added to the BST, if allowed, let the user know the
        # value is already in the BST and exit the value adding operation.
        if node.get_val() == val:
            # print("The value you entered is already in the BST!")
            return False

        # If the value is not equal to that of the current node and ...
        # i. the value to be added to the BST is lesser than value of the current node, check for a left node. ....
        elif val < node.get_val():
            # .... If a 'left' node exists within the current node, apply the current _add_node method to the 'left'
            # node
            if node.left:
                self._add_node(node.left, val)

            # .... If a 'left' node doesn't exist within the current node, add one to the current node with 'val' as its
            # value
            else:
                new_node = Node(val)
                node.set_left(new_node)

        # ii. the value to be added to the BST is greater than the value of the current node, check for a right node.
        # ....
        elif val > node.get_val():
            # .... If a 'right' node exists within the current node, apply the current _add_node method to the 'right'
            # node
            if node.right:
                self._add_node(node.right, val)

            # .... If a right node doesn't exist within the current node, add one to the current node with 'val' as its
            # value
            else:
                new_node = Node(val)
                node.set_right(new_node)

    # The method below serves as an interface for get_no_of_levels_dfs in a Node object
    # This finds the number of levels in a binary search tree.
    # Took two and a half hours to devise this from mind without previous know-how.

    def get_no_of_levels_dfs(self):
        if self.root:
            print(self.root.get_no_of_levels_dfs(self.root))

        if not self.root:
            return False

    # The method below enables you to visualise the BST you have created
    def visualise_bst(self):
        self.root.construct_bst(self.root)

binary = BST()

from random import randint
from string import ascii_uppercase, ascii_letters

# Automatically populating the BST with values
for num in range(20):
    case = ascii_letters[randint(0, 51)]
    # num = randint(1, 9)

    binary.add_node(case)
    # binary.add_node(f"{num}")

binary.visualise_bst()




# UNDERSTANDING HOW IT'S GONNA WORK

#                                                               f                                                               1       1     = 1
#                               c                                                               h                               2       1 . 2 = 2
#               b                               d                               g                               i               3       2 x 2 = 4
#       a               x               x               e               x               x               x               x       4       4 x 2 = 8

#       a       b       x       c       x       d       e       f       x       g       x        h      x       i       x       z


#                                                               1

#                               2                                                                2

#               3                               3                               3                               3


#       4               4               4               4               4               4               4               4

# Always pretend the last level is complete

# You'd have to find no of items in a each level by observing the number of items in the geometric
# series within each level

# Find the last level by finding the last item using DFS.

# UNDERSTANDING HOW IT'S GONNA WORK CONTD


#                                                               f                                                               1       1     = 1
#                               c                                                               h                               2       1 . 2 = 2
#               b                               d                               g                               i               3       2 x 2 = 4
#       a               x               x               e               x               x               x               p       4       4 x 2 = 8
#   x       x       x       x       x       x       x       x       x       x       x       x       x       x       m       x   5       8 x 2 = 16
# x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   k   o   x   x 6       16x 2 = 32

# x x x a x x x b x x x x x x x c x x x x x x x d x x x e x x x f x x x x x x x g x x x x x x x h x x x x x x x i k m o p x x x
