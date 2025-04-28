from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    if not root:
        return []

    result, queue = [], deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)
        queue.extend(filter(None, [node.left, node.right]))

    return result
    

tree1 = Node(1,
    Node(2,
        Node(4,
            Node(8,
                Node(16),
                Node(17)
            ),
            Node(9,
                Node(18),
                Node(19)
            )
        ),
        Node(5,
            Node(10,
                Node(20),
                Node(21)
            ),
            Node(11,
                Node(22),
                Node(23)
            )
        )
    ),
    Node(3,
        Node(6,
            Node(12,
                Node(24),
                Node(25)
            ),
            Node(13,
                Node(26),
                Node(27)
            )
        ),
        Node(7,
            Node(14,
                Node(28),
                Node(29)
            ),
            Node(15,
                Node(30),
                Node(31)
            )
        )
    )
)


tree2 = Node(50,
    None,
    Node(49,
        None,
        Node(48,
            None,
            Node(47,
                None,
                Node(46,
                    None,
                    Node(45,
                        None,
                        Node(44,
                            None,
                            Node(43,
                                None,
                                Node(42,
                                    None,
                                    Node(41,
                                        None,
                                        Node(40,
                                            None,
                                            Node(39,
                                                None,
                                                Node(38,
                                                    None,
                                                    Node(37,
                                                        None,
                                                        Node(36)
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)


tree3 = Node(100,
    Node(50,
        Node(25,
            Node(12),
            Node(13)
        ),
        Node(30,
            Node(14),
            Node(15)
        )
    ),
    Node(75,
        Node(60,
            Node(40),
            Node(41)
        ),
        Node(90,
            Node(80,
                Node(70),
                Node(71)
            ),
            Node(95,
                None,
                Node(99)
            )
        )
    )
)


for _ in range(10000):
    tree_by_levels(tree1)
    tree_by_levels(tree2)
    tree_by_levels(tree3)
