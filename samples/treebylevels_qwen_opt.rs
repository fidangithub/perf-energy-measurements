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
    let tree1 = Node::new(1)
    .left(Node::new(2)
        .left(Node::new(4)
            .left(Node::new(8)
                .left(Node::new(16))
                .right(Node::new(17)))
            .right(Node::new(9)
                .left(Node::new(18))
                .right(Node::new(19))))
        .right(Node::new(5)
            .left(Node::new(10)
                .left(Node::new(20))
                .right(Node::new(21)))
            .right(Node::new(11)
                .left(Node::new(22))
                .right(Node::new(23)))))
    .right(Node::new(3)
        .left(Node::new(6)
            .left(Node::new(12)
                .left(Node::new(24))
                .right(Node::new(25)))
            .right(Node::new(13)
                .left(Node::new(26))
                .right(Node::new(27))))
        .right(Node::new(7)
            .left(Node::new(14)
                .left(Node::new(28))
                .right(Node::new(29)))
            .right(Node::new(15)
                .left(Node::new(30))
                .right(Node::new(31)))));


let tree2 = Node::new(50)
    .right(Node::new(49)
    .right(Node::new(48)
    .right(Node::new(47)
    .right(Node::new(46)
    .right(Node::new(45)
    .right(Node::new(44)
    .right(Node::new(43)
    .right(Node::new(42)
    .right(Node::new(41)
    .right(Node::new(40)
    .right(Node::new(39)
    .right(Node::new(38)
    .right(Node::new(37)
    .right(Node::new(36)))))))))))))));


let tree3 = Node::new(100)
    .left(Node::new(50)
        .left(Node::new(25)
            .left(Node::new(12))
            .right(Node::new(13)))
        .right(Node::new(30)
            .left(Node::new(14))
            .right(Node::new(15))))
    .right(Node::new(75)
        .left(Node::new(60)
            .left(Node::new(40))
            .right(Node::new(41)))
        .right(Node::new(90)
            .left(Node::new(80)
                .left(Node::new(70))
                .right(Node::new(71)))
            .right(Node::new(95)
                .right(Node::new(99)))));

    for _ in 0..10000 {
        tree_by_levels(&tree1);
        tree_by_levels(&tree2);
        tree_by_levels(&tree3);
    }
}
