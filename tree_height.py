class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.val)

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def create(self, val:int):
        """
        Attach node to tree by assigning to node, left, or right
        based on value
        if val < current, it goes on the left
        if val > current, it goes on the right
        if there's no root yet, the first value becomes the root by default
        :param val: integer value 
        """
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root:Node) -> int:
    """
    Find the longest path (DFS) from root to farthest-most leaf
    
    :param root: root node info
    :return: tree height (int)
    """
    depth = 0
    maxdepth = []

    current = root
    print(' current node is {}'.format(current))

    print(' current.left is {}'.format(current.left))

    while True:
        if (current.left is None) and (current.right is None):
            maxdepth.append(0)
            return max(maxdepth)
        else:
            if current.left is not None:
                depth +=1
                current = current.left
            elif current.right is not None:
                depth += 1
                current = current.right
            maxdepth.append(depth)

            print(' maxdepth so far is {}'.format(maxdepth))
            print(' current.right is {}'.format(current.right))

    print(maxdepth)

    return max(maxdepth)


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))