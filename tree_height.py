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
    current = root.left
    depth = 0
    maxdepth = [0]
    #track the value and whether it has a branchpoint or not (bool)
    seen = dict()

    #do the left side first, then the right

    while current is not None:
        if current.val not in seen:
            if (current.left is not None) and (current.right is not None):
                seen.update({current.val:True})
            else:
                seen.update({current.val:False})
            depth +=1
            maxdepth.append(depth)
            if current.left is not None:
                current = current.left
            elif current.right is not None:
                current = current.right
        else:
            current = None

    print(' maxdepth left so far is {}'.format(maxdepth))

    current = root.right
    depth = 0

    while current is not None:
        if current.val not in seen:
            if (current.left is not None) and (current.right is not None):
                seen.update({current.val: True})
            else:
                seen.update({current.val: False})
            depth +=1
            maxdepth.append(depth)
            if current.right is not None:
                current = current.right
            elif current.left is not None:
                current = current.left
        else:
            current = None
    print(' maxdepth right so far is {}'.format(maxdepth))

    return max(maxdepth)


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))