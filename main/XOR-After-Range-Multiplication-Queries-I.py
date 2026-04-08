1from typing import List
2
3class Solution:
4    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
5        MOD = 10**9 + 7
6        
7        for l, r, k, v in queries:
8            idx = l
9            while idx <= r:
10                nums[idx] = (nums[idx] * v) % MOD
11                idx += k
12        
13        # compute XOR
14        result = 0
15        for num in nums:
16            result ^= num
17        
18        return result