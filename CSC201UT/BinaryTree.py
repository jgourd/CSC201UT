class BinaryTree:
    def __init__(self, val):
        self._value = val
        self._left = None
        self._right = None

    def insert_left(self, val):
        n = BinaryTree(val)
        # this node doesn't have a left child
        if (self._left == None):
            self._left = n
        # this node already has a left child
        else:
            n._left = self._left
            self._left = n

    def insert_right(self, val):
        n = BinaryTree(val)
        # this node doesn't have a right child
        if (self._right == None):
            self._right = n
        # this node already has a left child
        else:
            n._right = self._right
            self._right = n

    def get_value(self):
        return self._value

    def set_value(self, val):
        self._value = val

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    value = property(get_value, set_value)
    left = property(get_left)
    right = property(get_right)

    def print_tree(self, level=0):
        if (self != None):
            if (self.right):
                self.right.print_tree(level + 1)
            print(f"{'    ' * level}{self.value}")
            if (self.left):
                self.left.print_tree(level + 1)

