import unittest2

from tree_height import height, Node, BinarySearchTree

class TestCreateBST(unittest2.TestCase):

    def test_root_only(self):
        root = Node(0)
        assert root.left is None
        assert root.right is None

    def test_left_only(self):
        tree = BinarySearchTree()
        tree.create(1)
        assert tree.root.val == 1
        tree.create(0)
        assert tree.root.left.val == 0
        assert tree.root.right is None

    def test_right_only(self):
        tree = BinarySearchTree()
        tree.create(0)
        assert tree.root.val == 0
        tree.create(1)
        assert tree.root.right.val == 1
        assert tree.root.left is None

    def test_balanced_tree(self):
        tree = BinarySearchTree()
        tree.create(1)
        assert tree.root.val == 1
        tree.create(0)
        tree.create(2)
        assert tree.root.right.val == 2
        assert tree.root.left.val == 0

    def test_almost_balanced_tree(self):
        pass

class TestHeight(unittest2.TestCase):

    def test_root_only(self):
        root = Node(0)
        assert height(root) == 0

    def test_left_only(self):
        root = Node(1)
        tree = BinarySearchTree()
        tree.create(root.val)
        tree.create(0)
        assert height(root) == 1

if __name__ == '__main__':
    unittest2.main()