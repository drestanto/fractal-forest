import unittest
from fractal_forest import Node, Tree

class TestFractalForest(unittest.TestCase):
    def test_node_creation(self):
        node = Node((5, "root"))
        self.assertEqual(node.value, (5, "root"))
    
    def test_adding_children(self):
        parent = Node((10, "parent"))
        child = Node((5, "child"))
        parent.add_child(child)
        self.assertEqual(len(parent.children), 1)
    
    def test_integrity_check(self):
        root = Node((10, "root"))
        child1 = Node((5, "child1"))
        child2 = Node((7, "child2"))
        root.add_child(child1)
        root.add_child(child2)
        self.assertEqual(root.value, (22, "root"))
        
    def test_tree_structure(self):
        root = Node((10, "root"))
        tree = Tree(root)
        child = Node((5, "child"))
        tree.add_node(root, child)
        self.assertEqual(len(root.children), 1)
