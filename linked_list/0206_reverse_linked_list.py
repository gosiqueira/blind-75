"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: [] 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + ' -> ' + str(self.next)


# Solution 1: Recursive
def reverseList(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    if head is None or head.next is None:
        return head

    nxt = head.next
    head.next = None

    new_head = reverseList(nxt)
    nxt.next = head

    return new_head


# Solution 2: Iteractive
def reverseListIter(head: ListNode) -> ListNode:
    """
    Time: O(n)
    Space: O(1)
    """
    if head is None:
        return head

    cur = head
    prev = None

    while cur.next:
        nxt = cur.next
        cur.next = prev

        prev = cur
        cur = nxt

    cur.next = prev

    head = cur

    return head



if __name__ == '__main__':
    # Test 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverseList(head))
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverseListIter(head))

    # Test 2
    head = ListNode(1, ListNode(2))
    print(reverseList(head))
    head = ListNode(1, ListNode(2))
    print(reverseListIter(head))

    # Test 3
    head = None
    print(reverseList(head))
    head = None
    print(reverseListIter(head))
