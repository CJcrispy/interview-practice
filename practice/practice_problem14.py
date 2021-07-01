"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: TreeNode) -> int:
    q = [root]
    while q:
        pre, q = q, [child for p in q for child in [p.left, p.right] if child]
    return sum(node.val for node in pre)

roots = [1,2,3,4,5,None,6,7,None,None,None,None,8]
print(deepestLeavesSum(root=roots))

"""
Explanation
pre are nodes in the previous level.
q are node in the current level.

When current level are empty,
the previous level are the deepest leaves.


Complexity
Time O(N)
Space O(N)


line: 
    pre, q = q, [child for p in q for child in [p.left, p.right] if child]

can be expanded into:
    pre = q
    current = []
    for p in q:
        for child in [p.left, p.right] :
            if child:
                current.append(child)
    q = current
"""