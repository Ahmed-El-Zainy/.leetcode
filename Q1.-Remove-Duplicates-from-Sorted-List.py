1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return head
10
11        current = head
12        while current.next:
13            if current.val == current.next.val:
14                current.next = current.next.next
15            else:
16                current = current.next
17
18        return head