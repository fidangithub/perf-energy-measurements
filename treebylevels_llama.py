from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        

def tree_by_levels(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


tree_by_levels(None)

tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))