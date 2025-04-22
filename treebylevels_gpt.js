class Node { 
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left  = left;
    this.right = right;
  }
}

function treeByLevels(root) {
  if (!root) return [];

  const result = [];
  const queue = [root];

  while (queue.length > 0) {
    const current = queue.shift();
    result.push(current.value);

    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
  }

  return result;
}

const tree1 = new Node(1,
  new Node(2,
    new Node(4,
      new Node(8,
        new Node(16),
        new Node(17)
      ),
      new Node(9,
        new Node(18),
        new Node(19)
      )
    ),
    new Node(5,
      new Node(10,
        new Node(20),
        new Node(21)
      ),
      new Node(11,
        new Node(22),
        new Node(23)
      )
    )
  ),
  new Node(3,
    new Node(6,
      new Node(12,
        new Node(24),
        new Node(25)
      ),
      new Node(13,
        new Node(26),
        new Node(27)
      )
    ),
    new Node(7,
      new Node(14,
        new Node(28),
        new Node(29)
      ),
      new Node(15,
        new Node(30),
        new Node(31)
      )
    )
  )
);


const tree2 = new Node(50,
  null,
  new Node(49,
    null,
    new Node(48,
      null,
      new Node(47,
        null,
        new Node(46,
          null,
          new Node(45,
            null,
            new Node(44,
              null,
              new Node(43,
                null,
                new Node(42,
                  null,
                  new Node(41,
                    null,
                    new Node(40,
                      null,
                      new Node(39,
                        null,
                        new Node(38,
                          null,
                          new Node(37,
                            null,
                            new Node(36)
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
);


const tree3 = new Node(100,
  new Node(50,
    new Node(25,
      new Node(12),
      new Node(13)
    ),
    new Node(30,
      new Node(14),
      new Node(15)
    )
  ),
  new Node(75,
    new Node(60,
      new Node(40),
      new Node(41)
    ),
    new Node(90,
      new Node(80,
        new Node(70),
        new Node(71)
      ),
      new Node(95,
        null,
        new Node(99)
      )
    )
  )
);


for (let i = 0; i < 10000; i++) {
  treeByLevels(tree1);
  treeByLevels(tree2);
  treeByLevels(tree3);
}
