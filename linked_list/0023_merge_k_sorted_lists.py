"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it. 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

from typing import List, Optional


class ListNode:
    """
    List node class representation
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time: O(nlogk)
    Space: O(k)
    """
    if not lists:
        return None

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(mergeList(list1, list2))
            
        lists = merged_lists
        
    return lists[0]
            

def mergeList(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    while list1:
        tail.next = list1
        list1 = list1.next
        tail = tail.next

    while list2:
        tail.next = list2
        list2 = list2.next
        tail = tail.next

    return dummy.next


if __name__ == '__main__':
    # Test 1
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    lists = [list1, list2, list3]
    print(mergeKLists(lists))
    print(mergeKListsHeap(lists))

    # Test 2
    lists = []
    print(mergeKLists(lists))
    print(mergeKListsHeap(lists))

    # Test 3
    list1 = None
    lists = [list1]
    print(mergeKLists(lists))
    print(mergeKListsHeap(lists))