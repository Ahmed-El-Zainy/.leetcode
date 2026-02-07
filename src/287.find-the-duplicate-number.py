#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = sum(nums)
        unique_nums = set(nums)
        actual_set_nums = sum(unique_nums)
        extra_num = len(nums) - len(unique_nums)
        
        res = (actual_sum - actual_set_nums) // extra_num
        return res
    
# @lc code=end

