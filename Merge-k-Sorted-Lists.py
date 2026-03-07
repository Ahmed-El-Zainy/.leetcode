1from typing import List, Optional
2import heapq
3
4# Definition for singly-linked list.
5class ListNode:
6    def __init__(self, val=0, next=None):
7        self.val = val
8        self.next = next
9
10class Solution:
11    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
12        if not lists:
13            return None
14
15        while len(lists) > 1:
16            merged = []
17            for i in range(0, len(lists), 2):
18                l1 = lists[i]
19                l2 = lists[i + 1] if i + 1 < len(lists) else None
20                merged.append(self.mergeTwoLists(l1, l2))
21            lists = merged
22
23        return lists[0]
24
25    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
26        dummy = ListNode(0)
27        curr = dummy
28
29        while l1 and l2:
30            if l1.val <= l2.val:
31                curr.next = l1
32                l1 = l1.next
33            else:
34                curr.next = l2
35                l2 = l2.next
36            curr = curr.next
37
38        curr.next = l1 if l1 else l2
39        return dummy.next