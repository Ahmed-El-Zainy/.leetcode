1class Solution:
2    def findDifferentBinaryString(self, nums: List[str]) -> str:
3        n = len(nums)
4        ans = []
5        for i in range(n):
6            ans.append('1' if nums[i][i] == '0' else '0')
7        return "".join(ans)