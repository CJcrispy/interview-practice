## Red/Black Tree
-  a self-balancing Binary Search Tree (BST) where every node follows the following rules:
    1. Root property: Root of tree is always black
    2. External property: Every external node is black
    3. Red property: The children of a red node are black
    4. Depth property: All external node have the same black depth

- Most of the BST operations (search, max, min, insert, delete, etc) take O(h) time where h = height of the BST
    - The cost of the operations may become O(n) for a skewed tree

- The height of a Red-Black tree is always O(log*n), where n = # of nodes in the tree

- If we make sure that h = O(log(n)) for every insertion and deletion, then we can guarantee
an upper bound of O(log(n)) for all these operations

###### height
- Black height is # of black nodes on a path from root to leaf
    - black_height >= h/2

- Every Red-Black tree with *n* node has height <= 2 * log2(n+1)
    1. let K be the minimum # of nodes on all root to NULL paths, then n >= 2^k-1
        - Also written as K <= log2(n+1)
    2. a red-black tree with n nodes, there is a root to leaf path with at most 
    log2(n+1) black nodes
    3. The number of black nodes in a red-black tree is at least n/2 (n = # of nodes)

###### insert
Tools used to do balancing
1. Recoloring
    - Recoloring is the change in colour of the node 
        - i.e. if it is red then change it to black and vice versa. It must be noted that the colour of the NULL node is always black
2. Rotation

- The algorithms has mainly two case depending upon the color of the uncle node
    - if uncle is red, we do recoloring
    - if uncle is black, do rotations and/or recoloring 

NOTE: Color of a null is considered black

NOTE:
    - The left subtree of a node contains only nodes with keys lesser than the node's key
    - The right subtree contains only the greater
    - The left & right subtree must also be a binary search tree
    - No duplicate nodes

Red/Black insert
1) perform standard BST insertion and make the color of the newly inserted nodes as RED
2) if x is root, change color of x as BLACK (Black height of complete tree increases by 1)
3) Do following if color od x's parent is not BLACK nd x is not root
    a) if x's uncle is RED
        - Change color of parent and uncle as BLACK
        - color of grandparent as RED
        - change x =x's grandparent, repeat 2 & 3 for new x
    b) if x's uncle is BLACK, then there can be four configurations for x, x's parent(p) and x's grandparent (g)
        - left left case (p is the left child of g and x is the left child of p)
        - left right case (p is left child of g and x is right child of p)
        - right right case (mirror case 1)
        - right left case (mirror case 2)

Red/Black delete
- The man violated property is, change of black height in subtrees as deletion of
a black node may cause reduced black height in one root to leaf path

- when a black node is deleted and replaced by a black child, the child is marked as double black

## AVL Tree
- A binary search tree in which the difference of heights of left and right subtrees of any node >= 1

- Left T be a non-empty binary tree with Tl and Tr as its left and right subtrees.
the tree is height balanced if:
    - Tl and Tr are height balanced
    - Hl - Hr <= 1, where hl - hr are the heights of Tl and Tr

Advantages of AVL trees
- insert/delete have have low time complexity

## Tree Traversal

###### Depth First Traversal (DFS)
- algorithm traverses a graph in a depthward motion and uses a stack to remember to get the next vertex to start a search, when a dead end occurs in any iteration.
It employs the following rules.
```
Rule 1 − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Push it in a stack.
Rule 2 − If no adjacent vertex is found, pop up a vertex from the stack. (It will pop up all the vertices from the stack, which do not have adjacent vertices.)
Rule 3 − Repeat Rule 1 and Rule 2 until the stack is empty.
```

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3 
    - the left subtree is visited first, then the root and later the right sub-tree. We should always remember that every node may represent a subtree itself.
    - If a binary tree is traversed in-order, the output will produce sorted key values in an ascending order.
(b) Preorder (Root, Left, Right) : 1 2 4 5 3 
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

###### Breadth First Traversal (BFS)
- Breadth First Search (BFS) algorithm traverses a graph in a breadthward motion and uses a queue to remember to get the next vertex to start a search, when a dead end occurs in any iteration.
It employs the following rules.
```
Rule 1 − Visit the adjacent unvisited vertex. Mark it as visited. Display it. Insert it in a queue.
Rule 2 − If no adjacent vertex is found, remove the first vertex from the queue.
Rule 3 − Repeat Rule 1 and Rule 2 until the queue is empty.
```

Breadth First or Level Order Traversal : 1 2 3 4 5 