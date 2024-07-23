class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def build_tree(nodes):
    if not nodes or nodes[0] == 'N':
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] != 'N':
            current.left = TreeNode(int(nodes[i]))
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] != 'N':
            current.right = TreeNode(int(nodes[i]))
            queue.append(current.right)
        i += 1
    return root

def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result
nodes = input().strip().split()
root = build_tree(nodes)
inverted_root = invert_tree(root)
inorder_result = inorder_traversal(inverted_root)
print(" ".join(map(str, inorder_result)))