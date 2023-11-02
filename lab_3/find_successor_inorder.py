class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent



def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:

    if node.parent == None and node.left == None and node.right == None:
        return None

    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current

    if node.value < tree.value and node.value < node.parent.value:
        return node.parent

    if node.value < tree.value and node.value > node.parent.value:
        return tree

    if tree.value < node.value and node.parent.value > node.value:
        return node.parent