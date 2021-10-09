"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4. 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

class TreeNode:
    """
    Tree node class representation
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def checkValid(root: TreeNode, last_visited: int) -> bool:
    if root is None:
        return True

    if root.left and not checkValid(root.left, last_visited):
        return False

    if last_visited is not None and root.val <= last_visited:
        return False

    last_visited = root.val

    if root.right and not checkValid(root.right, last_visited):
        return False

    return True


def isValidBST(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    return checkValid(root, None)


def isValidBSTIter(root: TreeNode) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    if root is None:
        return True

    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, lower_bound, upper_bound = stack.pop()

        if node.val <= lower_bound or node.val >= upper_bound:
            return False

        if node.left:
            stack.append((node.left, lower_bound, node.val))
        if node.right:
            stack.append((node.right, node.val, upper_bound))

    return True


if __name__ == '__main__':
    # Test 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(isValidBST(root))
    print(isValidBSTIter(root))

    # Test 2
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(isValidBST(root))
    print(isValidBSTIter(root))
