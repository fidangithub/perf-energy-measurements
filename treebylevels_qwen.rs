mod preloaded;
use preloaded::Node;
use std::collections::VecDeque;

// struct Node {
//   value: u32,
//   left: Option<Box<Node>>,
//   right: Option<Box<Node>>
// }

fn tree_by_levels(root: &Node) -> Vec<u32> {
    let mut result = vec![];
    let mut queue: VecDeque<&Node> = VecDeque::from([root]);
    while let Some(n) = queue.pop_front() {
        result.push(n.value);
        if let Some(ref l) = n.left {
            queue.push_back(&*l);
        }
        if let Some(ref r) = n.right {
            queue.push_back(&*r);
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

tree_by_levels(&tree2)

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

tree_by_levels(&tree3);

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

tree_by_levels(&tree4)