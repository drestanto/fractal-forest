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
# usage_example.py
from fractal_forest import Fractal

# Create the root fractal
root = Fractal((10, "root"))

# Create child fractals
child1 = Fractal((5, "child1"))
child2 = Fractal((7, "child2"))

# Add children to root
root.add_child(child1)
root.add_child(child2)

# Print the tree
root.print_tree()

# Access the updated value at root
print(root.value)  # Output will be (22, 'root') after aggregation
```

## License
MIT License