#
# @lc app=leetcode id=3507 lang=python3
#
# [3507] Minimum Pair Removal to Sort Array I
#
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/
#
# algorithms
# Easy (55.78%)
# Likes:    470
# Dislikes: 81
# Total Accepted:    136.7K
# Total Submissions: 208.7K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array nums, you can perform the following operation any number of
# times:
# 
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs
# exist, choose the leftmost one.
# Replace the pair with their sum.
# 
# 
# Return the minimum number of operations needed to make the array
# non-decreasing.
# 
# An array is said to be non-decreasing if each element is greater than or
# equal to its previous element (if it exists).
# 
# 
# Example 1:
# 
# 
# Input: nums = [5,2,3,1]
# 
# Output: 2
# 
# Explanation:
# 
# 
# The pair (3,1) has the minimum sum of 4. After replacement, nums =
# [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# 
# 
# The array nums became non-decreasing in two operations.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,2]
# 
# Output: 0
# 
# Explanation:
# 
# The array nums is already sorted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50
# -1000 <= nums[i] <= 1000
# 
# 

from typing import List
# @lc code=start
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
        
# @lc code=end

