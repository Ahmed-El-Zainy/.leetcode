1class Solution:
2    def minPartitions(self, n: str) -> int:
3        return max(int(digit) for digit in n)
4