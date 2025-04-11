class Node:
    def __init__(self, value, children=None):
        self.value = value  # Tuple (int, Any)
        self.children = children if children else []
    
    def add_child(self, child_node):
        self.children.append(child_node)
        self._update_parent_integrity()
    
    def _update_parent_integrity(self):
        """Ensure that updates propagate through the tree."""
        total = sum(child.value[0] for child in self.children) + self.value[0]
        self.value = (total, self.value[1])  # Aggregating int value in the tuple
        if hasattr(self, 'parent') and self.parent:
            self.parent._update_parent_integrity()
    
    def set_parent(self, parent_node):
        """Link this node to a parent, which will affect updates."""
        self.parent = parent_node
        parent_node.add_child(self)
    
    def __repr__(self):
        return f"Node(value={self.value}, children={len(self.children)})"


class Tree:
    def __init__(self, root_node):
        self.root = root_node
    
    def add_node(self, parent_node, child_node):
        child_node.set_parent(parent_node)
    
    def __repr__(self):
        return f"Tree(root={self.root})"
