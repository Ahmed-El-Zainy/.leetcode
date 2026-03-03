1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        if n == 1:
4            return '0'
5        
6        mid = (1 << (n - 1)) - 1
7        if k == mid + 1:
8            return '1'
9        elif k <= mid:
10            return self.findKthBit(n - 1, k)
11        else:
12            return '0' if self.findKthBit(n - 1, (1 << n) - k) == '1' else '1'
13