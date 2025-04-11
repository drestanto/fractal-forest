# fractal-forest

**fractal-forest** is a Python library designed for efficient management and analysis of hierarchical numerical data structures. It supports recursive tree structures where each node contains a tuple of an integer and a generic value. The library is optimized for real-time distributed processing and OLAP compatibility.

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
