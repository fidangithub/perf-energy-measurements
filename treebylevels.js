class Node { 
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left  = left;
    this.right = right;
  }
}

function treeByLevels (rootNode) {
  if(!rootNode) return []
  const nodes = [rootNode]
  const result = []
  while(nodes.length > 0) {
    const node = nodes.shift()
    if(node.left) {
      nodes.push(node.left)
    }
    if(node.right) {
      nodes.push(node.right)
    }
    result.push(node.value)
  }
  return result;
}

treeByLevels(null)

const treeOne =
  new Node(2,
    new Node(8,
      new Node(1),
      new Node(3)
    ),
    new Node(9,
      new Node(4),
      new Node(5)
    )
  );

treeByLevels(treeOne)

const treeTwo =
  new Node(1,
    new Node(8,
      null,
      new Node(3)
    ),
    new Node(4,
      null,
      new Node(5,
        null,
        new Node(7)
      )
    )
);

treeByLevels(treeTwo)