"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""

class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time: O(n)
    Space: O(1)
    """
    if head is None or head.next is None: return None
    
    right = head
    left = head
    prev = None
    
    for _ in range(n):
        right = right.next
        
    while right:
        right = right.next
        prev = left
        left = left.next
        
    if prev:
        prev.next = left.next if left else None
    else:
        head = head.next
        
    return head


if __name__ == "__main__":
    # Test 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(removeNthFromEnd(head, 2))

    # Test 2
    head = ListNode(1, ListNode(2))
    print(removeNthFromEnd(head, 1))

    # Test 3
    head = ListNode(1)
    print(removeNthFromEnd(head, 1))
