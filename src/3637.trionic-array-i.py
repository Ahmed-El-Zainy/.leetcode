#
# @lc app=leetcode id=3637 lang=python3
#
# [3637] Trionic Array I
#
# https://leetcode.com/problems/trionic-array-i/description/
#
# algorithms
# Easy (39.62%)
# Likes:    375
# Dislikes: 34
# Total Accepted:    156.4K
# Total Submissions: 316.7K
# Testcase Example:  '[1,3,5,4,2,6]'
#
# You are given an integer array nums of length n.
# 
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
# 
# 
# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# 
# 
# Return true if nums is trionic, otherwise return false.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,4,2,6]
# 
# Output: true
# 
# Explanation:
# 
# Pick p = 2, q = 4:
# 
# 
# nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
# nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
# nums[4...5] = [2, 6] is strictly increasing (2 < 6).
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,1,3]
# 
# Output: false
# 
# Explanation:
# 
# There is no way to pick p and q to form the required three segments.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= n <= 100
# -1000 <= nums[i] <= 1000
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        i = 0

        # Ascending phase
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # Check if we have at least one element in the ascending phase
        if i == 0:
            return False

        # Descending phase
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1

        # Check if we have at least one element in the descending phase
        if j == i:
            return False

        # Final ascending phase
        k = j
        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1

        # Check if we have at least one element in the final ascending phase
        if k == j:
            return False

        # If we reached the end of the array, it's trionic
        return k == n - 1
        
        
# @lc code=end

