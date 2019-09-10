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
        tree = BinarySearchTree()
        tree.create(1)
        assert height(tree.root) == 0

    def test_left_only(self):
        tree = BinarySearchTree()
        tree.create(1)
        tree.create(0)
        assert tree.root.val == 1
        assert tree.root.left is not None
        assert tree.root.left.val == 0
        assert tree.root.right is None
        assert height(tree.root) == 1

    def test_right_only(self):
        tree = BinarySearchTree()
        tree.create(0)
        tree.create(1)
        assert height(tree.root) == 1

    def test_branching(self):
        tree = BinarySearchTree()
        for val in [int(x) for x in "3 5 2 1 4 6 7".split(" ")]:
            tree.create(val)
        assert tree.root.val == 3
        assert tree.root.right.val == 5
        assert tree.root.left.val == 2
        assert height(tree.root) == 3

    def test_branching2(self):
        tree = BinarySearchTree()
        for val in [int(x) for x in "3 1 7 5 4".split(" ")]:
            tree.create(val)
        assert height(tree.root) == 3

if __name__ == '__main__':
    unittest2.main()