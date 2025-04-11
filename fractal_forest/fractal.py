class Fractal:
    def __init__(self, value):
        """Initializes a Fractal with a value (a tuple: (int, label))."""
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Adds a child Fractal to the current Fractal."""
        if child not in self.children:
            self.children.append(child)
            child.parent = self

            child_value = child.value[0]
            if len(self.children) == 1:
                # First child: set parent value to child value, throw away own initial value
                self.value = (child_value, self.value[1])
            else:
                # Subsequent child: just add child value to it's own value
                self.value = (self.value[0] + child_value, self.value[1])

            if self.parent:
                self.parent.update_value()

    def remove_child(self, child):
        """Removes a child from the current Fractal."""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            self.value = (self.value[0] - child.value[0], self.value[1])
            if self.parent:
                self.parent.update_value()

    def is_root(self):
        """Checks if the Fractal is the root of all (i.e., parent is None)."""
        return self.parent is None

    def update_value(self):
        """Updates the value of this Fractal to the sum of its own value and its children's values."""
        total = sum(child.value[0] for child in self.children)
        self.value = (total, self.value[1])
        if self.parent:
            self.parent.update_value()
        return total

    def find_root(self):
        """Finds the root of the fractal tree."""
        node = self
        while node.parent is not None:
            node = node.parent
        return node

    def integrity_check(self):
        """Checks if the fractal tree is consistent (each node's value equals sum of children values)."""
        def check_node(node):
            if not node.children:
                return node.value[0]
            child_sum = sum(check_node(child) for child in node.children)
            return child_sum

        root = self.find_root()
        expected = check_node(root)
        return expected == root.value[0]

    def print_tree(self, level=0):
        """Prints the tree structure recursively."""
        print("  " * level + f"{self.value}")
        for child in self.children:
            child.print_tree(level + 1)

    def __repr__(self):
        return f"Fractal(value={self.value}, children_count={len(self.children)})"
