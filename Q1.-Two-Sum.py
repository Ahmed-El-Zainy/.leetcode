1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        res = {}
4        for i, num in enumerate(nums):
5            if target - num in res:
6                return [res[target - num], i]
7            res[num] = i