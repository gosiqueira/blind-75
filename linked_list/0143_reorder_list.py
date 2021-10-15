"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
 
Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from typing import Optional


class ListNode:
    """
    List node class representation
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


def reorderList(head: Optional[ListNode]) -> None:
    """
    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next:
        return
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev, slow.next, slow = None, None, slow.next
    while slow:
        prev, prev.next, slow = slow, prev, slow.next

    slow = head
    while prev:
        slow.next, slow = prev, slow.next
        prev.next, prev = slow, prev.next


if __name__ == '__main__':
    # Test 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reorderList(head)
    print(head)

    # Test 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorderList(head)
    print(head)