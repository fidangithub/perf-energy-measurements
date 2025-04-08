from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        

def tree_by_levels(node):
    if not node:
        return []
    res, queue = [], deque([node,])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res


tree_by_levels(None)

tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))