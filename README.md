# fractal-forest

**fractal-forest** is a Python library designed for efficient management and analysis of hierarchical numerical data structures. It supports recursive tree structures where each node contains a tuple of an integer and a generic value. The library can be optimized for real-time distributed processing and OLAP compatibility.

## Features

- Recursive tree structures with multiple children per node
- Node values as tuples: `(int, Any)` for numerical aggregation and associated data
- Automated tree creation and child addition
- Integrity checks with automatic propagation of updates to parent and child nodes
- Designed for hierarchical structured data such as:
  - Financial data (e.g., budgeting, accounting hierarchies)
  - Inventory systems (e.g., product categories, stock levels)
  - Organizational charts
  - Nested project management tasks
  - Any domain requiring structured aggregation and integrity validation

## Installation

```bash
pip install fractal-forest
```

## Usage

```python
from fractal_forest import Node, Tree

# Create the root node with a value (int, label)
root = Node((10, "root"))

# Create children
child1 = Node((5, "child1"))
child2 = Node((7, "child2"))

# Add children to root
root.add_child(child1)
root.add_child(child2)

# Add grandchild
grandchild = Node((3, "grandchild"))
child1.add_child(grandchild)

# Print the tree
tree = Tree(root)
tree.print_tree()

# Access the updated value at root
print(root.value)  # Output will be (25, 'root') after aggregation
```

## License
MIT License