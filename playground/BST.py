class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_val(self):
        return self.val

    def get_left(self):
        return self.left.val if self.left else self.left

    def get_right(self):
        return self.right.val if self.right else self.right

    def set_left(self, data):
        self.left.val = data

    def insert_node(self, data):
        if self.val == data:
            return False

        else:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)

    def find(self, data):
        if self.val == data:
            return True
        else:
            if data < self.get_val():
                if self.left is None:
                    return False
                elif self.left:
                    return self.left.find(data)
            elif data > self.get_val():
                if self.right is None:
                    return False
                elif self.right:
                    return self.right.find(data)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val)

    def levelorder(self):

        to_traverse = [self]
        result = ""

        while to_traverse:
            node = to_traverse.pop(0)

            if node.left:
                to_traverse.append(node.left)
            if node.right:
                to_traverse.append(node.right)

            print(node.val)





class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def insert_node(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            self.root.insert_node(data)

    def find(self, data):
        if self.root is None:  #
            return False
        else:
            return self.root.find(data)

    def inorder(self):
        print("Inorder\n")
        if self.root:
            return self.root.inorder()
        else:
            return False

    def preorder(self):
        print("Preorder\n")
        if self.root:
            self.root.preorder()

        else:
            return False

    def postorder(self):
        print("Postorder\n")
        if self.root:
            self.root.postorder()
        else:
            return False

    def levelorder(self):
        print("Level Order")
        if not self.root:
            return False
        else:
            return self.root.levelorder()


Ti = BinarySearchTree()

# Ti.insert_node(5)
# Ti.insert_node(3)
# Ti.insert_node(4)
# Ti.insert_node(2)
# Ti.insert_node(1)
# Ti.insert_node(6)
# Ti.insert_node(8)
# Ti.insert_node(7)

Ti.insert_node(10)
Ti.insert_node(5)
Ti.insert_node(3)
Ti.insert_node(7)
Ti.insert_node(1)
Ti.insert_node(4)
Ti.insert_node(6)
Ti.insert_node(8)
Ti.insert_node(16)
Ti.insert_node(14)
Ti.insert_node(17)
Ti.insert_node(18)
Ti.insert_node(12)
Ti.insert_node(15)

# print(Ti.root.left.get_right())
# print(Ti.root.find(0))
# Ti.inorder()

# Ti.levelorder()