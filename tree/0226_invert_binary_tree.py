"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

class TreeNode:
    """
    Tree node class representation
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'[{self.val} [{self.left}, {self.right}]]'


def invertTree(root: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    if root is None:
        return
    
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left, root.right = right, left
    
    return root


if __name__ == "__main__":
    # Test 1
    root = TreeNode(4, TreeNode(2, TreeNode(7, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(9))), None)
    print(invertTree(root))

    # Test 2
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(invertTree(root))

    # Test 3
    root = None
    print(invertTree(root))