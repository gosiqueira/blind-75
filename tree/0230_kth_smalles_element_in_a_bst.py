"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

from typing import Optional


class TreeNode:
    """
    Tree Node class representation
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = [root]
    
    while root.left:
        stack.append(root.left)
        root = root.left
        
    cur = root
    for i in range(k):
        cur = stack.pop()
        
        if cur.right:
            right = cur.right
            stack.append(right)
            while right.left:
                stack.append(right.left)
                right = right.left
                
    return cur.val


if __name__ == '__main__':
    # Test 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    print(kthSmallest(root, 1))

    # Test 2
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(kthSmallest(root, 3))