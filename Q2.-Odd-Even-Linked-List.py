1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return head
10
11        odd = head
12        even = head.next
13        even_head = even
14
15        while even and even.next:
16            odd.next = even.next
17            odd = odd.next
18            even.next = odd.next
19            even = even.next
20
21        odd.next = even_head
22
23        return head