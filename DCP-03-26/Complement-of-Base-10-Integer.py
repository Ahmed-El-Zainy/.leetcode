1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        if n == 0:
4            return 1
5        
6        mask = 1
7        while mask <= n:
8            mask <<= 1
9        
10        return mask - 1 - n