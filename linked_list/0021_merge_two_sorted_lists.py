"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0] 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'{self.val} -> {self.next}'


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ans = ListNode(0)
    cur = ans
    
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
            
        cur = cur.next
        
    while l1:
        cur.next = l1
        l1 = l1.next
        cur = cur.next
        
    while l2:
        cur.next = l2
        l2 = l2.next
        cur = cur.next
        
    return ans.next


if __name__ == '__main__':
    # Test 1
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    print(mergeTwoLists(l1, l2))

    # Test 2
    l1 = None
    l2 = None
    print(mergeTwoLists(l1, l2))

    # Test 3
    l1 = None
    l2 = ListNode(0)
    print(mergeTwoLists(l1, l2))
