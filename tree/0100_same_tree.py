"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from typing import Optional


class TreeNode:
    """
    Tree node class representation
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    if p is None and q is None:
        return True
    elif p is None and q:
        return False
    elif p and q is None:
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    # Test 1
    p = TreeNode(1, TreeNode(2, TreeNode(3)))
    q = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(isSameTree(p, q))

    # Test 2
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    print(isSameTree(p, q))

    # Test 3
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    print(isSameTree(p, q))
