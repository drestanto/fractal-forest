# fractal_forest/fractal.py

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
            self.update_value()

    def remove_child(self, child):
        """Removes a child from the current Fractal."""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            self.update_value()

    def is_root(self):
        """Checks if the Fractal is the root of all (i.e., parent is None)."""
        return self.parent is None

    def update_value(self):
        """Updates the value of this Fractal to the sum of its own value and its children's values."""
        total = self.value[0]  # Start with the integer value of this Fractal
        for child in self.children:
            total += child.update_value()  # Recursively sum up the children's values
        self.value = (total, self.value[1])  # Update the value as a tuple (sum, label)
        return total

    def print_tree(self, level=0):
        """Prints the tree structure recursively."""
        print("  " * level + f"{self.value}")
        for child in self.children:
            child.print_tree(level + 1)

    def __repr__(self):
        """A simple string representation for debugging."""
        return f"Fractal(value={self.value}, children_count={len(self.children)})"
