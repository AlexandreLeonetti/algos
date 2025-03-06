# demonstrate all 3 basic traversals of binary trees
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inorder traversal: Left -> Root -> Right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Preorder traversal: Root -> Left -> Right
def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder traversal: Left -> Right -> Root
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")

# Example Usage
if __name__ == "__main__":
    # Creating a simple tree
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal:")
    inorder_traversal(root)  # Output: 4 2 5 1 3

    print("\nPreorder traversal:")
    preorder_traversal(root)  # Output: 1 2 4 5 3

    print("\nPostorder traversal:")
    postorder_traversal(root)  # Output: 4 5 2 3 1
