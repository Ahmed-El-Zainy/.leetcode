1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev = None
9        current = head
10
11        while current:
12            next_node = current.next
13            current.next = prev
14            prev = current
15            current = next_node
16
17        return prev
18