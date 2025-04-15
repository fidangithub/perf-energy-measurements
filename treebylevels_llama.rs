mod preloaded;
use preloaded::Node;
use std::collections::VecDeque;

pub struct Node {
    pub val: i32,
    pub left: Option<Box<Node>>,
    pub right: Option<Box<Node>>,
}

impl Node {
    #[inline]
    pub fn new(val: i32) -> Self {
        Node {
            val,
            left: None,
            right: None,
        }
    }
}

pub fn tree_by_levels(root: Option<Box<Node>>) -> Vec<i32> {
    let mut result = Vec::new();
    if let Some(node) = root {
        let mut queue = std::collections::VecDeque::new();
        queue.push_back(node);
        while let Some(current_node) = queue.pop_front() {
            result.push(current_node.val);
            if let Some(left) = current_node.left {
                queue.push_back(*left);
            }
            if let Some(right) = current_node.right {
                queue.push_back(*right);
            }
        }
    }
    result
}

let tree2 = Node::new(1)
        .left(Node::new(2)
            .left(Node::new(4))
            .right(Node::new(5)))
        .right(Node::new(3)
            .left(Node::new(6)));


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



fn main() {
    tree_by_levels(&tree2)
    tree_by_levels(&tree3);
    tree_by_levels(&tree4);
}