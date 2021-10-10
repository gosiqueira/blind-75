"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.

Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

from typing import List


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


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """
    if len(preorder) == 0 or len(inorder) == 0:
        return None

    val = preorder.pop(0)
    inorder_idx = inorder.index(val)

    left, right = None, None

    if inorder_idx > 0:
        left = buildTree(preorder, inorder[:inorder_idx])

    if inorder_idx < len(inorder):
        right = buildTree(preorder, inorder[inorder_idx + 1:])

    return TreeNode(val, left, right)


if __name__ == '__main__':
    # Test 1
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = buildTree(preorder, inorder)
    print(root)

    # Test 2
    preorder = [-1]
    inorder = [-1]
    root = buildTree(preorder, inorder)
    print(root)
