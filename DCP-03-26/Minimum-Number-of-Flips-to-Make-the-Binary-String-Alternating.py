1class Solution:
2    def minFlips(self, s: str) -> int:
3        n = len(s)
4        s += s
5        alt1 = ''.join('0' if i % 2 == 0 else '1' for i in range(2 * n))
6        alt2 = ''.join('1' if i % 2 == 0 else '0' for i in range(2 * n))
7
8        diff1 = sum(1 for i in range(n) if s[i] != alt1[i])
9        diff2 = sum(1 for i in range(n) if s[i] != alt2[i])
10
11        ans = min(diff1, diff2)
12
13        for i in range(n, 2 * n):
14            if s[i] != alt1[i]:
15                diff1 += 1
16            if s[i - n] != alt1[i - n]:
17                diff1 -= 1
18
19            if s[i] != alt2[i]:
20                diff2 += 1
21            if s[i - n] != alt2[i - n]:
22                diff2 -= 1
23
24            ans = min(ans, diff1, diff2)
25
26        return ans