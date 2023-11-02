import unittest

from lab_3.find_successor_inorder import find_successor, BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(10)
        self.root.left = BinaryTree(5, parent=self.root)
        self.root.right = BinaryTree(15, parent=self.root)
        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.root.left.right = BinaryTree(7, parent=self.root.left)
        self.root.right.left = BinaryTree(12, parent=self.root.right)
        self.root.right.right = BinaryTree(18, parent=self.root.right)

    def test_find_successor_left_child(self):
        node = self.root.left
        successor = find_successor(self.root, node)
        self.assertEqual(successor.value, 7)

    def test_find_successor_left_child_no_right_subtree(self):
        node = self.root.left.left
        successor = find_successor(self.root, node)
        self.assertEqual(successor.value, 5)

    def test_find_successor_right_child(self):
        node = self.root.right
        successor = find_successor(self.root, node)
        self.assertEqual(successor.value, 18)

    def test_find_successor_right_child_no_right_subtree(self):
        node = self.root.right.right
        successor = find_successor(self.root, node)
        self.assertIsNone(successor)

    def test_find_successor_leaf_node(self):
        node = self.root.left.right
        successor = find_successor(self.root, node)
        self.assertEqual(successor.value, 10)

    def test_find_successor_nonexistent_node(self):
        node = BinaryTree(99)
        successor = find_successor(self.root, node)
        self.assertIsNone(successor)

    def test_find_successor_root_node(self):
        node = self.root
        successor = find_successor(self.root,  node)
        self.assertEqual(successor.value, 12)