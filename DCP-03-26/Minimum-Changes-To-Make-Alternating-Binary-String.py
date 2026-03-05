1class Solution:
2    def minOperations(self, s: str) -> int:
3        count1 = 0
4        count2 = 0
5
6        for i, c in enumerate(s):
7            if i % 2 == 0:
8                if c != '0':
9                    count1 += 1
10                if c != '1':
11                    count2 += 1
12            else:
13                if c != '1':
14                    count1 += 1
15                if c != '0':
16                    count2 += 1
17
18        return min(count1, count2)
19