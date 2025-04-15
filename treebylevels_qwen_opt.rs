use std::collections::VecDeque;

struct Node {
  value: u32,
  left: Option<Box<Node>>,
  right: Option<Box<Node>>
}


impl Node {
    pub fn new(value: u32) -> Self {
        Node {
            value,
            left: None,
            right: None,
        }
    }

    pub fn left(mut self, node: Node) -> Self {
        self.left = Some(Box::new(node));
        self
    }

    pub fn right(mut self, node: Node) -> Self {
        self.right = Some(Box::new(node));
        self
    }
}

fn tree_by_levels(root: &Node) -> Vec<u32> {
    let mut result = Vec::new();
    let mut queue = VecDeque::from([root]);

    while let Some(node) = queue.pop_front() {
        result.push(node.value);

        if let Some(left) = &node.left {
            queue.push_back(left);
        }
        if let Some(right) = &node.right {
            queue.push_back(right);
        }
    }

    result
}

fn main() {
    let tree2 = Node::new(1)
        .left(Node::new(2).left(Node::new(4)).right(Node::new(5)))
        .right(Node::new(3).left(Node::new(6)));

    let tree3 = Node::new(45)
        .right(Node::new(35)
            .left(Node::new(38)
                .right(Node::new(40)
                    .left(Node::new(1)
                        .left(Node::new(20)))
                    .right(Node::new(44)
                        .left(Node::new(38))
                        .right(Node::new(41)))))
            .right(Node::new(3)
                .right(Node::new(23)
                    .left(Node::new(2)
                        .left(Node::new(46))
                        .right(Node::new(2)))
                    .right(Node::new(36)))));

    let tree4 = Node::new(42).right(Node::new(1)
        .right(Node::new(3)
        .right(Node::new(1)
        .right(Node::new(2)
        .right(Node::new(1)
        .right(Node::new(5)
        .right(Node::new(1)
        .right(Node::new(4)
        .right(Node::new(1)
        .right(Node::new(7)
        .right(Node::new(1)
        .right(Node::new(6)
        .right(Node::new(1)
        .right(Node::new(9)
        .right(Node::new(1))))))))))))))));

    tree_by_levels(&tree2);
    tree_by_levels(&tree3);
    tree_by_levels(&tree4);
}