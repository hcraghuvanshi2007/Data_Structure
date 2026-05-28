class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Creating Tree
root = TreeNode('A')

root.left = TreeNode('B')
root.right = TreeNode('C')

root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

root.right.right = TreeNode('F')


# Inorder Traversal
def inorder(node):
    if not node:
        return

    inorder(node.left)            # LEFT
    print(node.val, end=" ")      # ROOT
    inorder(node.right)           # RIGHT


# Preorder Traversal
def preorder(node):
    if not node:
        return

    print(node.val, end=" ")      # ROOT
    preorder(node.left)           # LEFT
    preorder(node.right)          # RIGHT


# Postorder Traversal
def postorder(node):
    if not node:
        return

    postorder(node.left)          # LEFT
    postorder(node.right)         # RIGHT
    print(node.val, end=" ")      # ROOT


print("Inorder Traversal:")
inorder(root)

print("\n")

print("Preorder Traversal:")
preorder(root)

print("\n")

print("Postorder Traversal:")
postorder(root)