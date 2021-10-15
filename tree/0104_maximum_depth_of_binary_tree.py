"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
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


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if root is None: return 0
    
    max_depth = 1
    stack = [(root, 1)]
    
    while stack:
        node, depth = stack.pop()
        
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
            
        if depth > max_depth:
            max_depth = depth
            
    return max_depth


if __name__ == '__main__':
    # Test 1
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maxDepth(root))

    # Test 2
    root = TreeNode(1, TreeNode(2))
    print(maxDepth(root))

    # Test 3
    root = None
    print(maxDepth(root))
    
    # Test 4
    root = TreeNode(0)
    print(maxDepth(root))
