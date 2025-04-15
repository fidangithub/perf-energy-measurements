use std::collections::VecDeque;
use std::rc::Rc;
use std::cell::RefCell;

struct Node {
  value: u32,
  left: Option<Box<Node>>,
  right: Option<Box<Node>>
}

fn tree_by_levels(root: Option<Rc<RefCell<Node>>>) -> Vec<i32> {
    let mut result = Vec::new();

    if root.is_none() {
        return result;
    }

    let mut queue = VecDeque::new();
    queue.push_back(root.unwrap());

    while let Some(current) = queue.pop_front() {
        let node = current.borrow();
        result.push(node.value);

        if let Some(left) = &node.left {
            queue.push_back(Rc::clone(left));
        }

        if let Some(right) = &node.right {
            queue.push_back(Rc::clone(right));
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